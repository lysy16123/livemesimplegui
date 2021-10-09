import PySimpleGUI as sg   
from generatetimes import generateUrls
from async_url import getUrl

sg.theme('Dark Black')

# 1- the layout
layout = [
        [sg.Frame(layout=[
            [sg.Text('Video ID:'), sg.Input(key='videoid')],
            [sg.Text('Video M3u8:'), sg.Input(key='m3u8url', text_color='black')],
            [sg.Button('Show URL', key="showurl")]
        ], title='Show Video URL',title_color='White', relief=sg.RELIEF_SUNKEN)],

        [sg.Button('Exit')]]

# 2 - the window
window = sg.Window('Live.me M3u8 URL -- by tetudin', layout, finalize=True)

window['m3u8url'].update(disabled=True)

# 3 - the event loop
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'showurl':
        videoid = values['videoid']
        try:
            if videoid.isdecimal():
                urls = generateUrls(videoid)
                correct_url = getUrl(urls)
                window['m3u8url'].update(correct_url)
            else:
                raise Exception
        except Exception as e:
            print (e)
            window['m3u8url'].update("Error, check video id.")


# 4 - the close
window.close()