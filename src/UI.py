import PySimpleGUI as sg
import pytube


# from pytube.cli import on_progress


# Main class where UI of downloader is implemented
class UserInterface:
    vid_quality_list = ['Max', 'Audio']

    # Basic Layout of Application
    layout = [[sg.Text("Insert link")],
              [sg.Input(key='-LINK-')],
              [sg.Text("Insert directory")],
              [sg.Input(key='-DIRECTORY-', readonly=True), sg.FolderBrowse()],
              [sg.OptionMenu(vid_quality_list, default_value='Max', key='-QUALITY-'),
               sg.Button('Download'), sg.Button('Preview')]]

    # right_column = [[sg.Image('Thumbnail', key='-IMG-')],
    #                 [sg.Text('Length', key='-Length-')],
    #                 [sg.Text('Title', key='-Title-')],
    #                 [sg.Text('Views', key='-Views-')],
    #                 [sg.Text('Date', key='-Date-')],
    #                 [sg.Text('Rating', key='-Rating-')],
    #                 [sg.Text('Creator', key='-Creator-')]]

    # Initiator
    # sg.theme()
    window = sg.Window('YT Downloader', layout)

    # Program loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        # Initiates download from user inputted link and directory
        if event == 'Download' and values['-LINK-'] != '' and values['-DIRECTORY-'] != '':
            youtube = pytube.YouTube(values['-LINK-'])

            # Selected video property control
            if values['-QUALITY-'] == 'Max':
                video = youtube.streams.get_highest_resolution().download(values['-DIRECTORY-'])
            elif values['-QUALITY-'] == 'Audio':
                video = youtube.streams.get_audio_only().download(values['-DIRECTORY-'])

            # youtube.register_on_progress_callback(on_progress)
        else:
            sg.popup("Please insert link and choose a directory")

    window.close()
