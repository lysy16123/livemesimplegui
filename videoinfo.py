import requests, sys, json



def video_info(videoid, tokens):
    with open('tokens.json') as json_file:
        tokens = json.load(json_file)

    uid = str(tokens['uid'])
    sso_token = str(tokens['sso_token'])
    token = str(tokens['token'])

    headers = {
        'Host': 'live.ksmobile.net',
        'smid': '',
        'd': '3a43512a1f3a6333',
        't': '1625855884985',
        'xd': '3a43512a1f3a6333',
        'afid': '1625713710364-2109860241678449590',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'user-agent': 'okhttp/3.12.12',
    }

    params = (
        ('mnc', '2'),
        ('data', '1'),
        ('ptvn', '2'),
        ('mcc', '724'),
        ('alias', 'lmpro'),
        ('api', '30'),
    )

    data = 'tuid='+uid+'&token='+token+'&sso_token='+sso_token+'&uid='+uid+'&videoid=%s&feed_id=&type=REPLAY' % videoid

    response = requests.post('https://live.ksmobile.net/live/queryinfo', headers=headers, params=params, data=data)

    dados = response.json()
    videourl = dados['data']['video_info']['videosource']
    print (dados)
    return videourl