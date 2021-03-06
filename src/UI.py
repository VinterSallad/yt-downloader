import PySimpleGUI as sg
import pytube


# from pytube.cli import on_progress


# Main class where UI of downloader is implemented
class UserInterface:
    # Basic Layout of Application
    layout = [[sg.Text("Insert link")],
              [sg.Input(key='-LINK-')],
              [sg.Text("Insert directory")],
              [sg.Input(key='-DIRECTORY-', readonly=True), sg.FolderBrowse()],
              [sg.Button('Download')]]

    # Initiator
    window = sg.Window('YT Downloader', layout)

    # Program loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        # Initiates download from user inputted link and directory
        if event == 'Download' and values['-LINK-'] != '' and values['-DIRECTORY-'] != '':
            youtube = pytube.YouTube(values['-LINK-'])
            video = youtube.streams.get_highest_resolution()
            video.download(output_path=values['-DIRECTORY-'])
            # youtube.register_on_progress_callback(on_progress)
        else:
            sg.popup("Please insert link and choose a directory")

    window.close()
