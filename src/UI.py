import PySimpleGUI as sg
import pytube


# Main class where UI of downloader is implemented
class UserInterface:
    # PySimpleGUI.Window(title="YT Downloader", layout=[[]], margins=(500, 300)).read()

    # Basic Layout of Application
    layout = [[sg.Text("Insert link")],
              [sg.Input(key='LINK')],
              [sg.Text("Insert directory")],
              [sg.Input(key='DIRECTORY')],
              [sg.Button('Download'), sg.Button('Close')]]

    # Initiator
    window = sg.Window('YT Downloader', layout)

    # Program loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Close':
            break

        # Initiates download from user inputted link and directory
        if event == 'Download':
            youtube = pytube.YouTube(values['LINK'])
            video = youtube.streams.get_highest_resolution()
            video.download(values['DIRECTORY'])

    window.close()
