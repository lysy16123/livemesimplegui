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
    end_date = start_date + datetime.timedelta(seconds=10)

    urls = []

    fixed_urls = ['http://vod.oc.linkv.fun/yolo-', 'http://record.linkv.fun/oc/yolo-']

    delta = datetime.timedelta(seconds=1)
    
    for orig_url in fixed_urls:
        if 'record' in orig_url:
            sdate = start_date.astimezone(tz=pytz.timezone("GMT"))
        else:
            sdate = start_date
        edate = end_date
        while sdate <= edate:
            datastr = sdate.strftime("%Y%m%d%H%M%S")
            final_url = "%s%s--%s.m3u8" % (orig_url, vdoid, datastr)
            urls.append(final_url)
            sdate += delta

    return urls