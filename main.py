import PySimpleGUI as sg   
from generateurls import generate_url_list
from async_url import get_correct_url

sg.theme('Dark Black')

layout = [
        [sg.Frame(layout=[
            [sg.Text('Video ID:'), sg.Input(key='videoid')],
            [sg.Text('Video M3u8:'), sg.Input(key='m3u8url', text_color='black')],
            [sg.Button('Show URL', key="showurl")]
        ], title='Show Video URL',title_color='White', relief=sg.RELIEF_SUNKEN)],

        [sg.Button('Exit')]]

window = sg.Window('Live.me M3u8 URL - by tetudin', layout, finalize=True)

window['m3u8url'].update(disabled=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'showurl':
        videoid = values['videoid']
        try:
            if videoid.isdecimal():
                urls = generate_url_list(videoid)
                correct_url = get_correct_url(urls)
                window['m3u8url'].update(correct_url)
            else:
                raise Exception
        except Exception as e:
            print (e)
            window['m3u8url'].update("Error, check video id.")


# 4 - the close
window.close()