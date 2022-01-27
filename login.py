import requests, sys, json
from applogin import get_token

def login(email_in, password_in):
    tokens = []

    def encode_multipart_formdata(fields):
        boundary = '3i2ndDfv2rTHiSisAbouNdArYfORhtTPEefj3q2f'

        body = (
            "".join("--%s\r\n"
                    "Content-Disposition: form-data; name=\"%s\"\r\n"
                    "\r\n"
                    "%s\r\n" % (boundary, field, value)
                    for field, value in fields.items()) +
            "--%s--\r\n" % boundary
        )


        return body


    headers = {
        'User-Agent': 'FBAndroidSDK.0.0.1',
        'Content-Type': 'multipart/form-data; boundary=3i2ndDfv2rTHiSisAbouNdArYfORhtTPEefj3q2f',
        'ver': '4.4.15',
        'appstyle': 'lmpro',
        'appid': '135301',
        'sid': '9469C0239535A9E579F8D20E5A4D5C3C',
        'sig': 'fp1bO-aJwHKoRB0jnsW4hQ6nor8',
    }

    files = encode_multipart_formdata({"cmversion": "44151688", 
    "name": email_in,
    "extra": "userinfo",
    "password": password_in})

    response = requests.post('https://iag.liveme.com/1/cgi/login', headers=headers, data=files)
    data = response.json()
    if (data['ret'] != 1):
        raise
    email = email_in
    sso_token = data['data']['sso_token']
    access_token = data['data']['access_token']
    uid = data['data']['extra']['data']['uid_str']
    token = get_token(access_token, sso_token, email)

    tokens = { 
        'uid': uid,
        'email': email,
        'sso_token': sso_token,
        'access_token': access_token,
        'token': token
    }

    with open('tokens.json', 'w') as outfile:
        json.dump(tokens, outfile)