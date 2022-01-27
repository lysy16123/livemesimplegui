import PySimpleGUI as sg   
import os, json
from login import login
from videoinfo import video_info


sg.theme('Dark Black')

def checkLogin():
    if os.path.isfile('./tokens.json'):
        with open('tokens.json') as json_file:
            tokens = json.load(json_file)
        email = str(tokens['email'])

        window['statusText'].update('Logged in as %s.' % email)
        window['email'].update(disabled=True)
        window['password'].update(disabled=True)
        window['login'].update(disabled=True)
        window['logout'].update(disabled=False)

        window['videoid'].update(disabled=False)
        window['showurl'].update(disabled=False)

    else:
        window['statusText'].update('Not logged.')
        window['email'].update("",disabled=False)
        window['password'].update("",disabled=False)
        window['logout'].update(disabled=True)

        window['login'].update(disabled=False)

        window['videoid'].update("",disabled=True)
        window['m3u8url'].update("")
        window['showurl'].update(disabled=True)

# 1- the layout
layout = [
        [sg.Frame(layout=[
            [sg.Text('Status:'), sg.Text(key='statusText')],
            [sg.Text('Email:'), sg.Input(key='email')],
            [sg.Text('Password:'), sg.Input(key='password', password_char='*')],
            [sg.Button('Login', key='login'), sg.Button('Logout', key="logout")]
        ], title='Login',title_color='White', relief=sg.RELIEF_SUNKEN)],

        [sg.Frame(layout=[
            [sg.Text('Video ID:'), sg.Input(key='videoid')],
            [sg.Text('Video M3u8:'), sg.Input(key='m3u8url', text_color='black')],
            [sg.Button('Show URL', key="showurl")]
        ], title='Show Video URL',title_color='White', relief=sg.RELIEF_SUNKEN)],

        [sg.Button('Exit')]]

# 2 - the window
window = sg.Window('Live.me M3u8 URL -- by tetudin', layout, finalize=True, icon='icon.png')

checkLogin()

window['m3u8url'].update(disabled=True)

# 3 - the event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'showurl':
        try:
            url = video_info(values['videoid'], 'tokens.json')
            window['m3u8url'].update(url)
        except Exception as e: 
            print(e)
            window['m3u8url'].update("Error, check video id.")


    if event == 'login':
        try:
            login(values['email'], values['password'])
            checkLogin()
        except:
            if os.path.isfile('./tokens.json'):
                os.remove('tokens.json')
            checkLogin()
            window['statusText'].update('Credentials error')

    if event == 'logout':
        os.remove('tokens.json')
        checkLogin()

# 4 - the close
window.close()