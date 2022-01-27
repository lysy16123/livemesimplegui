import requests

def get_token(access_token, sso_token, email):
    headers = {
        'Host': 'apipro.liveme.com',
        'smid': '',
        'd': '3a43512a1f3a6333',
        't': '1631238291881',
        'xd': '3a43512a1f3a6333',
        'afid': '1625713710364-2109860241678449590',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'user-agent': 'okhttp/3.12.12',
    }

    params = (
        ('ver', '4.4.15'),
        ('mnc', '2'),
        ('data', '1'),
        ('ptvn', '2'),
        ('mcc', '724'),
        ('alias', 'lmpro'),
        ('api', '30'),
        ('vercode', '44151688'),
        ('channelid', '200001'),
    )

    data = 'sso_token='+sso_token+'&status=0&access_token='+access_token+'&data[uid]=&data[sso_token]='+sso_token+'&data[email]='+email+'&data[mobile]=&data[smid]='

    response = requests.post('https://apipro.liveme.com/sns/appLoginCM', headers=headers, params=params, data=data)
    data = response.json()
    return data['data']['token']