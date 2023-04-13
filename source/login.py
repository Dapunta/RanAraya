#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Module
import os, sys, requests, bs4, re, time, datetime
from datetime import datetime
import logo
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor

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
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

#--> Ubah Bahasa
def language(cookie):
    try:
        with requests.Session() as xyz:
            req = xyz.get('https://mbasic.facebook.com/language/',cookies=cookie)
            pra = bs(req.content,'html.parser')
            for x in pra.find_all('form',{'method':'post'}):
                if 'Bahasa Indonesia' in str(x):
                    bahasa = {
                        "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                        "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                        "submit"  : "Bahasa Indonesia"}
                    url = 'https://mbasic.facebook.com' + x['action']
                    exec = xyz.post(url,data=bahasa,cookies=cookie)
    except Exception as e:pass

#--> Login
class login:
    def __init__(self):
        self.fty    = {}
        self.border = M
        self.konten = P
        self.title  = P
        self.xyz    = requests.Session()
        self.make_dir()
        get_publickey()
        proxyscrape()
        self.cek_cookies()
        self.get_tahun_pembuatan()
        self.prof()
        self.fty.update(license.main_license(self))
        self.show_dasbor_akun()
    def make_dir(self):
        try:os.mkdir('login')
        except Exception as e :pass
        try:os.mkdir('proxy')
        except Exception as e :pass
        try:os.mkdir('OK')
        except Exception as e :pass
        try:os.mkdir('CP')
        except Exception as e :pass
    def cek_cookies(self):
        try:
            self.cookie     = {'cookie':open('login/cookie.json','r').read()}
            self.token_eaag = open('login/token_eaag.json','r').read()
            self.token_eaat = open('login/token_eaat.json','r').read()
            language(self.cookie)
            req1 = self.xyz.get('https://graph.facebook.com/me?fields=name,id&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()     
            if 'Sepertinya Anda menyalahgunakan' in str(req1):
                clear()
                logo.logo()
                print('\n%sCookie Invalid !%s'%(M,P))
                print('%sAkunmu Terkena Spam, Coba Ganti Akun Lain%s'%(P,P))
                print('%sAtau Ubah Jaringanmu %s( %sMode Pesawat %s)%s'%(P,M,P,M,P))
                exit('')
            req2 = self.xyz.get('https://graph.facebook.com/me?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(self.token_eaat),cookies=self.cookie).json()['friends']
            self.fty.update({'Akun':req1['name'], 'ID':req1['id']})
            clear()
            logo.logo()
        except Exception as e:
            self.insert_cookie()
    def insert_cookie(self):
        print('\n%sCookie Invalid !%s'%(M,P))
        time.sleep(2)
        clear()
        logo.logo()
        print('%s[%s!%s] %sApabila Akun A2F On, Pergi Ke'%(M,P,M,P))
        print('%s[%s-%s] %shttps://business.facebook.com/business_locations'%(H,P,H,P))
        print('%s[%s-%s] %sUntuk Memasukkan Kode Autentikasi\n'%(H,P,H,P))
        ciko = input('%sMasukkan Cookie %s: %s'%(P,M,H))
        self.token_eaag = self.generate_token_eaag(ciko)
        self.token_eaat = self.generate_token_eaat(ciko)
        open('login/cookie.json','w').write(ciko)
        open('login/token_eaag.json','w').write(self.token_eaag)
        open('login/token_eaat.json','w').write(self.token_eaat)
        self.cek_cookies()
    def generate_token_eaag(self,cok):
        url = 'https://business.facebook.com/business_locations'
        req = self.xyz.get(url,cookies={'cookie':cok})
        tok = re.search('(\["EAAG\w+)', req.text).group(1).replace('["','')
        return(str(tok))
    def generate_token_eaat(self,cok):
        self.cookie = {'cookie':cok}
        data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}
        req  = self.xyz.post('https://graph.facebook.com/v16.0/device/login/',data=data).json()
        cd   = req['code']
        ucd  = req['user_code']
        url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd)
        req  = bs(self.xyz.get('https://mbasic.facebook.com/device',cookies=self.cookie).content,'html.parser')
        raq  = req.find('form',{'method':'post'})
        dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}
        rel  = 'https://mbasic.facebook.com' + raq['action']
        pos  = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        dat  = {}
        raq  = pos.find('form',{'method':'post'})
        for x in raq('input',{'value':True}):
            try:
                if x['name'] == '__CANCEL__' : pass
                else: dat.update({x['name']:x['value']})
            except Exception as e: pass
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(self.xyz.post(rel,data=dat,cookies=self.cookie).content,'html.parser')
        req = self.xyz.get(url,cookies=self.cookie).json()
        tok = req['access_token']
        return(str(tok))
    def get_tahun_pembuatan(self):
        try:
            bln    = {'01':'Januari', '02':'Februari', '03':'Maret', '04':'April', '05':'Mei', '06':'Juni', '07':'Juli', '08':'Agustus', '09':'September', '10':'Oktober', '11':'November', '12':'Desember'}
            req    = self.xyz.get('https://graph.facebook.com/me/albums?fields=id,name,created_time&limit=1000&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()
            t,m,h  = [x['created_time'].split('T')[0] for x in req['data'] if x['name']=='Foto Profil'][0].split('-')
            tb     = '%s %s %s'%(h,bln[m],t)
        except Exception as e:
            tb = 'Unknown'
        self.fty.update({'Pembuatan':tb})
    def prof(self):
        try: fren = str(self.xyz.get('https://graph.facebook.com/me?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(self.token_eaat),cookies=self.cookie).json()['friends']['summary']['total_count']); self.fty.update({'Teman':fren})
        except Exception as e: self.fty.update({'Teman':'-'})
        try: fols = str(self.xyz.get('https://graph.facebook.com/me/subscribers?limit=0&access_token=%s'%(self.token_eaag),cookies=self.cookie).json()['summary']['total_count']); self.fty.update({'Followers':fols})
        except Exception as e: self.fty.update({'Followers':'-'})
        try: ip = self.xyz.get('https://api.ipify.org/?format=json').json()['ip']; self.fty.update({'IP':ip})
        except Exception as e: self.fty.update({'IP':'-'})
    def show_dasbor_akun(self):
        x = self.fty
        y, z, q = self.border, self.konten, self.title
        print('%s╭───────── [ %sData Akun %s] ──────────╮  ╭───────── [ %sData User %s] ──────────╮%s'%(y,q,y,q,y,z))
        print('%s│%s│%s│%s│%s'%(y,' '*34,' '*2,' '*34,z))
        if len(x['Akun']) > 18: a_ = '%s│    %sAkun  : %s...    %s│'%(y,z,x['Akun'][:15],y)
        else: a_ = '%s│    %sAkun  : %s%s    %s│'%(y,z,x['Akun'],' '*(18-len(x['Akun'])),y)
        b_ = '%s│    %sID    : %s%s    %s│'%(y,z,x['ID'],' '*(18-len(x['ID'])),y)
        c_ = '%s│    %sBuat  : %s%s    %s│'%(y,z,x['Pembuatan'],' '*(18-len(x['Pembuatan'])),y)
        d_ = '%s│    %sTeman : %s%s    %s│'%(y,z,x['Teman'],' '*(18-len(x['Teman'])),y)
        e_ = '%s│    %sFolls : %s%s    %s│'%(y,z,x['Followers'],' '*(18-len(x['Followers'])),y)
        if len(x['User']) > 18: a__ = '%s  %s│    %sUser  : %s...    %s│'%(a_,y,z,x['User'][:15],y)
        else: a__ = '%s  %s│    %sUser  : %s%s    %s│'%(a_,y,z,x['User'], ' '*(18-len(x['User'])),y)
        b__ = '%s  %s│    %sPrem  : %s%s    %s│'%(b_,y,z, x['Premium'],' '*(18-len(x['Premium'])),y)
        c__ = '%s  %s│    %sAktif : %s%s    %s│'%(c_,y,z, x['Aktivasi'],' '*(18-len(x['Aktivasi'])),y)
        d__ = '%s  %s│    %sExprd : %s%s    %s│'%(d_,y,z, x['Kadaluwarsa'],' '*(18-len(x['Kadaluwarsa'])),y)
        e__ = '%s  %s│    %sIP    : %s%s    %s│'%(e_,y,z, x['IP'],' '*(18-len(x['IP'])),y)
        print('%s\n%s\n%s\n%s\n%s'%(a__,b__,c__,d__,e__))
        print('%s│%s│%s│%s│%s'%(y,' '*34,' '*2,' '*34,z))
        print('%s╰──────────────────────────────────╯  ╰──────────────────────────────────╯\n'%(y))

#--> Lisensi
class license:
    def __init__(self):
        self.main_license()
    def main_license(self):
        xd = {
            'User'        : 'Denventa Araya Dirgantara',
            'Premium'     : 'Ya',
            'Aktivasi'    : '1 Januari 2022',
            'Kadaluwarsa' : '1 Januari 2025'}
        return(xd)

def get_publickey():
    try:
        ua  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        hed = {
            'Host'                      : 'www.facebook.com',
            'Connection'                : 'Keep-Alive',
            'Keep-Alive'                : 'timeout=5, max=1000',
            'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding'           : 'gzip, deflate',
            'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control'             : 'max-age=0',
            'x-requested-with'          : 'XMLHttpRequest',
            'sec-ch-ua'                 : '" Not A;Brand";v="99", "Chromium";v="98"',
            'sec-ch-ua-mobile'          : '?1',
            'sec-ch-ua-platform'        : '"Windows"',
            'sec-fetch-dest'            : 'empty',
            'sec-fetch-mode'            : 'cors',
            'sec-fetch-site'            : 'same-origin',
            'sec-fetch-user'            : '?1',
            'upgrade-insecure-requests' : '1',
            'user-agent'                : ua}
        url = requests.Session().get('https://www.facebook.com/',headers=hed).text
        req = re.findall('\"publicKey\":\"(.*?)\",\"keyId\":([0-9]+)',url)
        for x,y in req:
            open('login/publickey.json','w').write('%s|%s'%(x,y))
    except Exception as e:
        open('login/publickey.json','w').write('Dapunta')

class proxyscrape:
    def __init__(self):
        self.xyz  = requests.Session()
        self.file = 'proxy/%s.json'%(waktu())
        if os.path.exists(self.file):
            pass
        else:
            self.scrap()
            clear()
    def scrap(self):
        url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=ID&ssl=yes&anonymity=all'
        try:
            xda = (self.xyz.get(url).text).splitlines()
            with ThreadPoolExecutor(max_workers=50) as TPE:
                for d in xda:
                    TPE.submit(self.check1,d)
        except Exception as e:
            pass
    def check1(self,prox):
        try:
            addr = str(prox.split(':')[0]) #--> Valid Proxy Address
            port = str(80)                 #--> Valid Proxy Port
            prox = '%s:%s'%(addr,port)
            url  = 'http://%s'%(addr)
            req  = self.xyz.get(url,timeout=2)
            if req.status_code == 200:
                self.check2(prox)
            else:
                pass
        except Exception as e:
            pass
    def check2(self,prox):
        try:
            proxy = {'http': f'socks4://{prox}'}
            url   = 'https://m.facebook.com/login/?email=4'
            req   = self.xyz.get(url,proxies=proxy)
            if req.status_code == 200:
                self.save(prox)
                pok = ('\r%s──> %s%s                              '%(H,prox,P))
                print(pok)
            else: pass
        except Exception as e:
            pass
        print('\rSedang Mendata Proxy...'%(),end=''); sys.stdout.flush()
    def save(self,prox):
        open(self.file,'a+').write('%s\n'%(prox))

def waktu(): # --- [ Jangan Ganti Keterangan Waktu ] --- #
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))
