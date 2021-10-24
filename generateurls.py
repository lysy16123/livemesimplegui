import datetime, requests
import pytz

#generate date from vtime and change to liveme(vod.oc) timezone
def generate_date(vdoid):
    response = requests.get('https://lvapi.liveme.com/live/queryinfo?h5=1&videoid=%s&vali=BktwlkCebmtmWRp' % vdoid)
    dados = response.json()
    vtime = dados['data']['video_info']['vtime']


    data = datetime.datetime.fromtimestamp(float(vtime), tz=pytz.timezone("Asia/Shanghai"))

    #data = data + datetime.timedelta(hours=3)

    return data

#returns a list of "probable" urls from the returned date, from the old url and the new url, adding 1 second and stops at +10 seconds 
def generate_url_list(vdoid):
    start_date = generate_date(vdoid)
    end_date = start_date + datetime.timedelta(seconds=20)

    urls = []

    if datetime.datetime.timestamp(start_date) < 1630986656:
        fixed_url = 'http://record.linkv.fun/oc/yolo-'
    else:
        fixed_url = 'http://vod.oc.linkv.fun/yolo-'

    delta = datetime.timedelta(seconds=1)
    
    if 'record' in fixed_url:
        sdate = start_date.astimezone(tz=pytz.timezone("GMT"))
    else:
        sdate = start_date
    edate = end_date
    while sdate <= edate:
        datastr = sdate.strftime("%Y%m%d%H%M%S")
        final_url = "%s%s--%s.m3u8" % (fixed_url, vdoid, datastr)
        urls.append(final_url)
        sdate += delta

    return urls