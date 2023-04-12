#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Module
import os, sys, requests, bs4, re, time, datetime, random
try: from crack import crack
except Exception as e: import crack
from datetime import datetime
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor as TPE

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

#--> Tanggal
skrng = datetime.now()
tahun, bulan, hari = skrng.year, skrng.month, skrng.day
bulan_cek = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
tanggal = ("%s-%s-%s"%(hari,bulan_cek[bulan-1],tahun))

#--> Animasi
def animasi():
    print('\r%s[%s•%s] %sSedang Dump %s%s %sID'%(M,P,M,P,M,str(len(dump)),P),end=''); sys.stdout.flush()

#--> Global Variable
pemisah = '|'

#--> Convert
def user_to_id(username):
    try:
        req = bs(requests.Session().get('https://mbasic.facebook.com/%s'%(username), cookies={'cookie':open('login/cookie.json','r').read()}).content, 'html.parser')
        kut = req.find('a',string='Lainnya')
        id = str(kut['href']).split('=')[1].split('&')[0]
        # id = re.search('owner_id=(.*?)"',str(kut)).group(1)
        return(id)
    except Exception as e:return(username)
def group_to_id(username):
    try:
        req = bs(requests.Session().get('https://mbasic.facebook.com/groups/%s'%(username), cookies={'cookie':open('login/cookie.json','r').read()}).content, 'html.parser')
        kut = req.find('a',string='Lihat Postingan Lainnya')
        id = str(kut['href']).split('?')[0].split('/')[2]
        return(id)
    except Exception as e:return(username)

#--> Menu Utama
class main_menu:
    def __init__(self):
        self.border = M
        self.konten = P
        self.title  = P
        self.menu()
        self.pilih_menu()
    def menu(self):
        y, z, q = self.border, self.konten, self.title
        print('%s╭──────────────────────────── [ %sMenu Utama %s] ────────────────────────────╮%s'%(y,q,y,P))
        print('%s│%s│'%(y,' '*72))
        print('%s│         %s[%s1%s] %sCrack           %s[%s3%s] %sCek Opsi         %s[%s5%s] %sLangganan         %s│'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y))
        print('%s│         %s[%s2%s] %sCek Hasil       %s[%s4%s] %sUser-Agent       %s[%s6%s] %sLogout            %s│'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y))
        print('%s│%s│'%(y,' '*72))
        print('%s╰─ ┌─ [ %sPilih %s] ─────────────────────────────────────────────────────────╯%s'%(y,P,y,P))
    def pilih_menu(self):
        xo = input('   %s└──> %s'%(M,P))
        if xo in   ['1', '01' ,'a']: main_menu_dump()
        elif xo in ['2', '02' ,'b']: pass
        elif xo in ['3', '03' ,'c']: pass
        elif xo in ['4', '04' ,'d']: pass
        elif xo in ['5', '05' ,'e']: pass
        elif xo in ['6', '06' ,'f']: pass

#--> Menu Utama Dump
class main_menu_dump:
    def __init__(self):
        self.menu()
        self.pilih_menu()
    def menu(self):
        y, z, q = M, P, P
        print('%s╭──────────────────────────── [ %sMenu  Dump %s] ────────────────────────────╮%s'%(y,q,y,P))
        print('%s│%s│'%(y,' '*72))
        print('%s│  %s[ %sAccount %s] %s[%s05%s] %sMessage  %s[%s10%s] %sFriendlist %s[ %sGroup %s]     %s[ %sPost %s]      %s│%s'%(y,y,z,y,y,z,y,z,y,z,y,z,y,z,y,y,z,y,y,z))
        print('%s│  %s[%s01%s] %sName   %s[%s06%s] %sUsername %s[%s11%s] %sFollowers  %s[%s15%s] %sTimeline %s[%s19%s] %sComment  %s│%s'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z))
        print('%s│  %s[%s02%s] %sEmail  %s[%s07%s] %sTimeline %s[%s12%s] %sID Random  %s[%s16%s] %sMembers  %s[%s20%s] %sReact    %s│%s'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z))
        print('%s│  %s[%s03%s] %sPhone  %s[%s08%s] %sHashtag  %s[%s13%s] %sSuggestion %s[%s17%s] %sComment                %s│%s'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z))
        print('%s│  %s[%s04%s] %sReact  %s[%s09%s] %sComment  %s[%s14%s] %sFL Dari FL %s[%s18%s] %sReact                  %s│%s'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z))
        print('%s│%s│'%(y,' '*72))
        print('%s╰─ ┌─ [ %sPilih %s] ─────────────────────────────────────────────────────────╯%s'%(y,P,y,P))
    def pilih_menu(self):
        xo = input('   %s└──> %s'%(M,P))
        print('')
        if xo in   ['1', '01' ,'a']: dump_owner_account('NM')
        elif xo in ['2', '02' ,'b']: dump_random('EM')
        elif xo in ['3', '03' ,'c']: dump_random('PO')
        elif xo in ['4', '04' ,'d']: dump_react_comment('A_R')
        elif xo in ['5', '05' ,'e']: dump_owner_account('PS')
        elif xo in ['6', '06' ,'f']: dump_random('US')
        elif xo in ['7', '07' ,'g']: dump_owner_account('TL')
        elif xo in ['8', '08' ,'h']: dump_owner_account('HS')
        elif xo in ['9', '009','i']: dump_react_comment('A_K')
        elif xo in ['10','010','j']: dump_friendlist()
        elif xo in ['11','011','k']: dump_followers()
        elif xo in ['12','012','l']: dump_random('ID')
        elif xo in ['13','013','m']: dump_owner_account('SU')
        elif xo in ['14','014','n']: dump_fl_fl()
        elif xo in ['15','015','o']: dump_react_comment('TL')
        elif xo in ['16','016','p']: dump_react_comment('MB')
        elif xo in ['17','017','q']: dump_react_comment('G_K')
        elif xo in ['18','018','r']: dump_react_comment('G_R')
        elif xo in ['19','019','s']: dump_react_comment('P_K')
        elif xo in ['20','020','t']: dump_react_comment('P_R')
        crack.main(dump)

#--> Dump Friendlist
class dump_friendlist:
    def __init__(self):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaat  = open('login/token_eaat.json','r').read()
        self.main()
    def main(self):
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan ID : %s'%(M,P,M,P,M)).split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek(io)
        print('')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        with TPE(max_workers=30) as ABC:
            for s in id:
                if s == 'me': io = s
                elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
                else : io = s
                ABC.submit(self.requ,io)
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def cek(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['name'])
            teman = str(self.xyz.get('https://graph.facebook.com/%s?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['friends']['summary']['total_count'])
            print(' %s• %s%s %s--> %s%s Teman'%(M,P,nama,M,P,teman))
        except Exception as e:
            print(' %s• %s%s %s--> %sKesalahan/Private'%(M,P,id,M,P))
            self.fail.append(id)
    def requ(self,id):
        url = 'https://graph.facebook.com/%s?fields=friends.limit(5000).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat)
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for y in req['friends']['data']:
                try:
                    id, nama = y['id'], y['name']
                    format = '%s%s%s'%(id,self.pisah,nama)
                    self.dump.append(format)
                    animasi()
                except Exception as e: pass
        except Exception as e: pass

#--> Dump Followers
class dump_followers:
    def __init__(self):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaat  = open('login/token_eaat.json','r').read()
        self.token_eaag  = open('login/token_eaag.json','r').read()
        self.main()
    def main(self):
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan ID : %s'%(M,P,M,P,M)).split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek(io)
        print('')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        with TPE(max_workers=30) as ABC:
            for s in id:
                if s == 'me': io = s
                elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
                else : io = s
                url = 'https://graph.facebook.com/%s/subscribers?limit=1000&access_token=%s'%(io,self.token_eaag)
                ABC.submit(self.requ,url)
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def cek(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['name'])
            folls = str(self.xyz.get('https://graph.facebook.com/%s/subscribers?limit=0&access_token=%s'%(id,self.token_eaag),cookies=self.cookie).json()['summary']['total_count'])
            print(' %s• %s%s %s--> %s%s Folls'%(M,P,nama,M,P,folls))
        except Exception as e:
            print(' %s• %s%s %s--> %sKesalahan/Private'%(M,P,id,M,P))
            self.fail.append(id)
    def requ(self,url):
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            for y in req['data']:
                try:
                    id, nama = y['id'], y['name']
                    format = '%s%s%s'%(id,self.pisah,nama)
                    self.dump.append(format)
                    animasi()
                except Exception as e: pass
            self.requ(req['paging']['next'])
        except Exception as e: pass

#--> Dump Friendlist Dari Friendlist
class dump_fl_fl:
    def __init__(self):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaat  = open('login/token_eaat.json','r').read()
        self.main()
    def main(self):
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan ID : %s'%(M,P,M,P,M)).split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek(io)
        print('')
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        self.t1 = input('%s[%s•%s] %sPilih ID Tua/Muda %s[%st/m%s] %s: %s'%(M,P,M,P,M,P,M,P,M)).lower()
        self.t2 = input('%s[%s•%s] %sBerapa ID Per Masing" Akun %s: '%(M,P,M,P,M))
        print('')
        try:
            for s in id:
                if s == 'me': io = s
                elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
                else : io = s
                lid = self.requ(io,'1')
            try:
                with TPE(max_workers=30) as ABC:
                    for h in lid:
                        ABC.submit(self.requ,h.split(self.pisah)[0],'2')
            except Exception as e:
                pass
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def cek(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['name'])
            teman = str(self.xyz.get('https://graph.facebook.com/%s?fields=friends.limit(0).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['friends']['summary']['total_count'])
            print(' %s• %s%s %s--> %s%s Teman'%(M,P,nama,M,P,teman))
        except Exception as e:
            print(' %s• %s%s %s--> %sKesalahan/Private'%(M,P,id,M,P))
            self.fail.append(id)
    def requ(self,id,tp):
        url = 'https://graph.facebook.com/%s?fields=friends.limit(5000).fields(id,name,birthday)&access_token=%s'%(id,self.token_eaat)
        try:
            req = self.xyz.get(url,cookies=self.cookie).json()
            pen = [ '%s%s%s'%(y['id'],self.pisah,y['name']) for y in req['friends']['data']]
            sm_ = []
            sm  = []
            if self.t1 in ['1','01','t','tua']:
                for z in pen:
                    sm.append(z)
                    if len(sm) == int(self.t2): break
            else:
                for z in pen:
                    sm_.insert(0,z)
                for z_ in sm_:
                    sm.append(z_)
                    if len(sm) == int(self.t2): break
                if tp == '1':
                    return(sm)
                else:
                    for h in sm:
                        if h in self.dump:pass
                        else:self.dump.append(h)
                        animasi()
        except Exception as e: pass

#--> Dump React, Comment, Member, Photo, Timeline
class dump_react_comment:

    #--> Penampungan Awal
    def __init__(self,tp):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.limit       = '100'
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaat  = open('login/token_eaat.json','r').read()
        self.token_eaag  = open('login/token_eaag.json','r').read()
        if tp   == 'A_K': self.modul = 'K'; self.main_A() #--> Dump Comment Account
        elif tp == 'A_R': self.modul = 'R'; self.main_A() #--> Dump React Account
        elif tp == 'G_K': self.modul = 'K'; self.main_G() #--> Dump Comment Group
        elif tp == 'G_R': self.modul = 'R'; self.main_G() #--> Dump React Group
        elif tp == 'P_K': self.modul = 'K'; self.main_P() #--> Dump Comment Post
        elif tp == 'P_R': self.modul = 'R'; self.main_P() #--> Dump React Post
        elif tp == 'TL' : self.modul = 'T'; self.main_tl_mb() #--> Dump Timeline
        elif tp == 'MB' : self.modul = 'M'; self.main_tl_mb() #--> Dump Member
    
    #--> Dump Post Account
    def main_A(self):
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan ID : %s'%(M,P,M,P,M)).split(',')
        print('')
        for f in id:
            if f == 'me': io = f
            elif (re.findall("[a-zA-Z]",str(f))) : io = user_to_id(f)
            else : io = f
            self.cek_A(io)
        print('')
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        try:
            with TPE(max_workers=30) as ABC:
                for s in id:
                    if s == 'me': io = s
                    elif (re.findall("[a-zA-Z]",str(s))) : io = user_to_id(s)
                    else : io = s
                    ABC.submit(self.requ1_A,io)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def cek_A(self,id):
        try: 
            nama  = str(self.xyz.get('https://graph.facebook.com/%s?fields=name&access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()['name'])
            lisz  = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/posts?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
            post  = str(len(lisz))
            print(' %s• %s%s %s--> %s%s Post'%(M,P,nama,M,P,post))
        except Exception as e:
            print(' %s• %s%s %s--> %sKesalahan/Private'%(M,P,id,M,P))
            self.fail.append(id)
    def requ1_A(self,id):
        lisz  = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/posts?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
        try:
            with TPE(max_workers=30) as ABC:
                for pid in lisz:
                    if self.modul == 'K':
                        url = 'https://mbasic.facebook.com/' + pid
                        ABC.submit(self.main_requ_comment,url)
                    else:
                        ABC.submit(self.main_requ_react,pid)
        except Exception as e: pass
    
    #--> Dump Post Group
    def main_G(self):
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan ID Grup : %s'%(M,P,M,P,M)).split(',')
        print('')
        for f in id:
            if (re.findall("[a-zA-Z]",str(f))) : io = group_to_id(f)
            else : io = f
            self.cek_G(io)
        print('')
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        try:
            with TPE(max_workers=30) as ABC:
                for s in id:
                    if (re.findall("[a-zA-Z]",str(s))) : io = group_to_id(s)
                    else : io = s
                    ABC.submit(self.requ1_G,io)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def cek_G(self,id):
        try:
            req = self.xyz.get('https://graph.facebook.com/%s?access_token=%s'%(id,self.token_eaat),cookies=self.cookie).json()
            if req['privacy'] == 'OPEN':
                try:
                    raq = bs(self.xyz.get('https://mbasic.facebook.com/groups/%s?view=info'%(id),cookies=self.cookie).content,'html.parser')
                    agt = str([c.text for c in raq.find_all('tr') if 'Anggota' in str(c)][0].replace('Anggota',''))
                    pos = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/feed?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
                except Exception as e: pass
                print(' %s• %s%s %s--> %s%s Members & %s Posts'%(M,P,str(req['name']).replace('Grup Publik',''),M,P,agt,str(len(pos))))
            else:
                print(' %s• %s%s %s--> %sKesalahan/Private'%(M,P,id,M,P))
                self.fail.append(id)
        except Exception as e:
            print(' %s• %s%s %s--> %sKesalahan/Private'%(M,P,id,M,P))
            self.fail.append(id)
    def requ1_G(self,id):
        lisz  = [x['id'] for x in self.xyz.get('https://graph.facebook.com/%s/feed?fields=id&limit=%s&access_token=%s'%(id,self.limit,self.token_eaag),cookies=self.cookie).json()['data']]
        try:
            with TPE(max_workers=30) as ABC:
                for pid in lisz:
                    if self.modul == 'K':
                        url = 'https://mbasic.facebook.com/' + pid
                        ABC.submit(self.main_requ_comment,url)
                    else:
                        ABC.submit(self.main_requ_react,pid)
        except Exception as e: pass
    
    #--> Dump Post
    def main_P(self):
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan ID Post : %s'%(M,P,M,P,M)).split(',')
        print('')
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        try:
            with TPE(max_workers=30) as ABC:
                for pid in id:
                    if self.modul == 'K':
                        url = 'https://mbasic.facebook.com/' + pid
                        ABC.submit(self.main_requ_comment,url)
                    else:
                        ABC.submit(self.main_requ_react,pid)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))

    #--> Main Dump Comment
    def main_requ_comment(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for x in req.find_all('h3'):
                try:
                    v    = x.find('a',href=True)
                    nama = v.text
                    if 'profile.php' in v['href']: id = re.search('profile.php\?id\=(.*?)\&amp',str(v)).group(1)
                    else: id = user_to_id(v['href'].split('?')[0].replace('/',''))
                    format = '%s%s%s'%(id,self.pisah,nama)
                    if format in self.dump:pass
                    else:self.dump.append(format)
                    animasi()
                except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string=' Lihat komentar sebelumnya…')['href']
            self.main_requ_comment(nek)
        except Exception as e: pass

    #--> Main Dump React
    def main_requ_react(self,id):
        try:
            url = 'https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=' + id.split('_')[1]
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for y in req.find_all('a',href=True):
                try:
                    if '/ufi/reaction/profile/browser/fetch/?ft_ent_identifier' in y['href']:
                        if 'Semua' in y.text: pass
                        elif 'reaction_type=0' in str(y): pass
                        else:
                            lk1 = 'https://mbasic.facebook.com' + y['href'].replace('limit=10','limit=50')
                            self.scrap_react(lk1)
                except Exception as e: continue
        except Exception as e: pass
    def scrap_react(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for z in req.find_all('h3'):
                try:
                    v    = z.find('a',href=True)
                    nama = v.text
                    if 'profile.php' in v['href']: id = re.search('profile.php\?id\=(.*?)\&amp',str(v)).group(1)
                    else: id = v['href'].split('?')[0].replace('/','')
                    format = '%s%s%s'%(id,self.pisah,nama)
                    if format in self.dump:pass
                    else:self.dump.append(format)
                    animasi()
                except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Selengkapnya')['href'].replace('limit=10','limit=50')
            self.scrap_react(nek)
        except Exception as e: pass

    #--> Dump Timeline & Member Group
    def main_tl_mb(self):
        print('%s[%s•%s] %sBanyak ID, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan ID Grup : %s'%(M,P,M,P,M)).split(',')
        print('')
        for f in id:
            if (re.findall("[a-zA-Z]",str(f))) : io = group_to_id(f)
            else : io = f
            self.cek_G(io)
        print('')
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        for d in self.fail:
            try: id.remove(d)
            except Exception as e: continue
        try:
            with TPE(max_workers=30) as ABC:
                for s in id:
                    if (re.findall("[a-zA-Z]",str(s))) : io = group_to_id(s)
                    else : io = s
                    if self.modul == 'T':
                        ABC.submit(self.scrape_tl,'https://mbasic.facebook.com/groups/'+io)
                    elif self.modul == 'M':
                        ABC.submit(self.scrape_tl,'https://mbasic.facebook.com/browse/group/members/?id=%s&start=0'%(io))
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    
    #--> Dump Timeline Group
    def scrape_tl(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for z in req.find_all('h3'):
                for po in z.find_all('a',href=True):
                    try:
                        if 'mbasic.facebook.com' in po['href']:pass
                        elif 'story.php' in po['href']:pass
                        elif 'Halaman' in po.text:pass
                        elif 'profile.php' in po['href']:
                            id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                            nm = po.text
                        else:
                            id = user_to_id(re.findall('\/(.*?)\/\?refid',str(po['href']))[0])
                            nm = po.text
                        format = '%s%s%s'%(id,self.pisah,nm)
                        if format in self.dump:pass
                        else:self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Postingan Lainnya')['href']
            self.scrape_tl(nek)
        except Exception as e: pass
    
    #--> Dump Member Group
    def scrape_mb(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for z in req.find_all('h3'):
                for po in z.find_all('a',href=True):
                    try:
                        if 'a/friends/add' in po['href']:pass
                        elif 'profile.php' in po['href']:
                            id = re.findall('profile\.php\?id=(.*?)&',str(po['href']))[0]
                            nm = po.text
                        else:
                            fd = re.findall('\/(.*?)\/\?',str(po['href']))[0]
                            id = user_to_id(fd)
                            nm = po.text
                        format = '%s%s%s'%(id,self.pisah,nm)
                        if format in self.dump:pass
                        else:self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Selengkapnya')['href']
            self.scrape_mb(nek)
        except Exception as e: pass

#--> Dump Message, Name, Timeline, Hashtag, Suggestion
class dump_owner_account:
    
    #--> Penampungan Awal
    def __init__(self,tp):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        if tp   == 'PS': self.main_message()    #--> Dump ID From Message
        elif tp == 'NM': self.main_name()       #--> Dump ID From Name
        elif tp == 'TL': self.main_timeline()   #--> Dump ID From Timeline
        elif tp == 'HS': self.main_hashtag()    #--> Dump ID From Hashtag
        elif tp == 'SU': self.main_suggestion() #--> Dump ID From Suggestion
    
    #--> Dump ID From Message
    def main_message(self):
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        try: self.scrape_message('https://mbasic.facebook.com/messages')
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def scrape_message(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for p in req.find_all('a',href=True):
                if '/messages/read/?tid=cid.c' in p['href']:
                    try:
                        if p.text == 'Pengguna Facebook': continue
                        else:
                            id   = str(re.search('%3A(.*?)&',p['href']).group(1))
                            nama = p.text
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Pesan Sebelumnya')['href']
            self.scrape_message(nek)
        except Exception as e: pass

    #--> Dump ID From Name
    def main_name(self):
        lid = []
        print('%s[%s•%s] %sBanyak Nama, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan Nama : %s'%(M,P,M,P,M)).lower().split(',')
        common = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
        for x in id:
            for y in common:
                lid.append('%s %s'%(x,y))
                lid.append('%s %s'%(y,x))
        print('')
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        try:
            with TPE(max_workers=30) as ABC:
                for z in lid:
                    url = 'https://mbasic.facebook.com/search/people/?q=' + z
                    ABC.submit(self.scrape_name,url)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def scrape_name(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for p in req.find_all('a',href=True):
                try:
                    if "<img alt=" in str(p):
                        if "home.php" in str(p["href"]): continue
                        elif 'profile.php' in str(p["href"]):
                            id   = re.search('"/profile\.php\?id=(.*?)&"',str(p)).group(1)
                            nama = p.find("img")['alt'].replace(", profile picture","")
                        elif 'refid' in str(p["href"]):
                            id   = user_to_id(re.search("/(.*?)\?",str(p)).group(1))
                            nama = p.find("img")['alt'].replace(", profile picture","")
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                    animasi()
                except Exception as e: continue
            nek = req.find('a',string='Lihat Hasil Selanjutnya')['href']
            self.scrape_name(nek)
        except Exception as e: pass
    
    #--> Dump ID From Timeline
    def main_timeline(self):
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        try: self.scrape_timeline('https://mbasic.facebook.com/')
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def scrape_timeline(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for q in req.find_all('h3'):
                for p in q.find_all('a',href=True):
                    try:
                        if 'mbasic.facebook.com' in p['href']:pass
                        elif 'sub_view' in p['href']:pass
                        elif '/?' in p['href']:pass
                        elif 'profile.php' in str(p["href"]):
                            id   = str(re.search('\?id=(.*?)&',p['href']).group(1))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        else:
                            id   = user_to_id(str(re.search('\/(.*?)\?',p['href']).group(1)))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat Berita Lain')['href']
            self.scrape_timeline(nek)
        except Exception as e: pass

    #--> Dump ID From Hashtag
    def main_hashtag(self):
        print('%s[%s•%s] %sBanyak Hashtag, Pisahkan Dgn (,)'%(M,P,M,P))
        id = input('%s[%s•%s] %sMasukkan Hastag : %s'%(M,P,M,P,M)).split(',')
        print('')
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        try:
            with TPE(max_workers=30) as ABC:
                for z in id:
                    url = 'https://mbasic.facebook.com/hashtag/' + z
                    ABC.submit(self.scrape_hashtag,url)
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def scrape_hashtag(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for q in req.find_all('h3'):
                for p in q.find_all('a',href=True):
                    try:
                        if 'mbasic.facebook.com' in p['href']:pass
                        elif 'sub_view' in p['href']:pass
                        elif '/?' in p['href']:pass
                        elif 'profile.php' in str(p["href"]):
                            id   = str(re.search('\?id=(.*?)&',p['href']).group(1))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        else:
                            id   = user_to_id(str(re.search('\/(.*?)\?',p['href']).group(1)))
                            nama = str(re.search('>(.*?)<\/a>',str(p)).group(1))
                        format = '%s%s%s'%(id,self.pisah,nama)
                        if format in self.dump: pass
                        else: self.dump.append(format)
                        animasi()
                    except Exception as e: continue
            nek = req.find('a',string='Lihat Hasil Selanjutnya')['href']
            self.scrape_hashtag(nek)
        except Exception as e: pass
    
    #--> Dump ID From Suggestion
    def main_suggestion(self):
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        try: self.scrape_suggestion('https://mbasic.facebook.com/friends/center/suggestions')
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def scrape_suggestion(self,url):
        try:
            req = bs(self.xyz.get(url,cookies=self.cookie).content,'html.parser')
            for p in req.find_all('a',href=True):
                try:
                    if "friends/hovercard/mbasic" in str(p['href']):
                        id   = p['href'].split('&')[0].split('=')[1]
                        nama = p.text
                    format = '%s%s%s'%(id,self.pisah,nama)
                    if format in self.dump: pass
                    else: self.dump.append(format)
                    animasi()
                except Exception as e: pass
            nek = 'https://mbasic.facebook.com' + req.find('a',string='Lihat selengkapnya')['href']
            self.scrape_suggestion(nek)
        except Exception as e: pass

#--> Dump Random Email, Phone, Username, ID
class dump_random:
    
    #--> Penampungan Awal
    def __init__(self,tp):
        global dump
        dump = self.dump = []
        self.fail        = []
        self.pisah       = pemisah
        self.xyz         = requests.Session()
        self.cookie      = {'cookie':open('login/cookie.json','r').read()}
        self.token_eaat  = open('login/token_eaat.json','r').read()
        if tp   == 'EM': self.main_email()    #--> Random Email
        elif tp == 'PO': self.main_phone()    #--> Random Phone
        elif tp == 'US': self.main_username() #--> Random Username
        elif tp == 'ID': self.main_id()       #--> Random ID
    
    #--> Auto Generate Random Email
    def main_email(self):
        belum_bisa()

    #--> Auto Generate Random Phone
    def main_phone(self):
        belum_bisa()

    #--> Auto Generate Random Username
    def main_username(self):
        belum_bisa()

    #--> Auto Generate Random ID
    def main_id(self):
        aw = input('%s[%s•%s] %sMasukkan ID Awal Sbg Acuan : %s'%(M,P,M,P,M))
        print('')
        print('%s[%s•%s] %sTekan %sctrl+c %sUntuk Berhenti'%(M,P,M,P,M,P))
        try:
            self.tamp(int(aw))
        except KeyboardInterrupt: pass
        if len(self.dump) == 0: print('\r%s[%s✘%s] Dump ID Gagal%s'%(M,P,M,P))
        else: print('\r%s[%s✔%s] %sBerhasil Mendapat %s%s %sID'%(M,P,M,P,M,str(len(self.dump)),P))
    def tamp(self,a):
        t = a+10000
        r = random.sample(range(a,t), t-a)
        r.append(t)
        r.sort()
        with TPE(max_workers=30) as ABC:
            for n in r:
                ABC.submit(self.cek_id,n)
    def cek_id(self,id):
        url = 'https://mbasic.facebook.com/login/device-based/password/?uid=%s&flow=login_no_pin&refsrc=deprecated&_rdr'%(id)
        try:
            req = bs(self.xyz.get(url).content,'html.parser')
            if "Sorry, this content isn't available right now" in req: pass
            elif 'Temporarily Blocked' in str(req):
                print('\rAkunmu Kena Spam',end=''); sys.stdout.flush()
            else:
                nama = req.find_all('img')[1]['alt'].split(',')[0]
                if nama == 'Foto Profil Pengguna': pass
                elif nama == '': pass
                else:
                    format = '%s%s%s'%(id,self.pisah,nama)
                    self.dump.append(format)
                    animasi()
        except Exception as e: pass

#--> Simpan File Ke Perangkat
class simpan_file:
    def __init__(self):
        self.main()
    def main(self):
        print('')
        ty = input('Simpan File? [y/t] : ').lower()
        if ty in ['1','01','y','ya','iya']: self.main2()
        else: pass
    def main2(self):
        try:os.mkdir('dump')
        except:pass
        try:
            nm  = input('Tulis Nama File : ').replace(' ','_') + '.txt'
            lk  = input('Tulis Lokasi Penyimpanan : ')
            lok = '%s\%s'%(lk,nm)
            open(lok,'a+')
            for d in dump:
                try: open(lok,'a+').write(d+'\n')
                except Exception as e: pass
            print('\nFile Dump Tersimpan Di %s'%(lok))
        except Exception as e:
            print('\nGagal Menemukan Lokasi File')
            lok = 'dump/%s.txt'%(tanggal)
            open(lok,'a+')
            for d in dump:
                try: open(lok,'a+').write(d+'\n')
                except Exception as e: pass
            print('File Dump Tersimpan Di %s'%(lok))

#--> Warning
def belum_bisa():
    print('Sorry Bos, Fiturnya Belum Tersedia\nMasih Pusing Mikirin Logikanya\nDoakan Semoga Cepat Selesai Yaa!\nSemoga SC Ini Bisa Membantu Orang Banyak...\nTerima Kasih!\n\n- Dapunta Khurayra X')
    exit()

# 100090682164277,100085567128204,100088661097809
# 588896855173299,920198672138478