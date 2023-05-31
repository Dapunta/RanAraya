#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

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

import os, sys, re, time, datetime, random

#--> Clear Terminal
def clear():
    if "linux" in sys.platform.lower():os.system('clear')
    elif "win" in sys.platform.lower():os.system('cls')

#--> Import Module & Run
def run():
    try                   : import requests
    except Exception as e : os.system('pip install requests'); import requests
    try                   : import bs4
    except Exception as e : os.system('pip install bs4'); import bs4
    try                   : from Cryptodome import Random as RDM
    except Exception as e : os.system('pip install pycryptodome'); os.system('pip install pycryptodomex')
    try                   : import nacl
    except Exception as e :
        clear()
        print('%sModule %spynacl %sBelum Terpasang !\n'%(P,M,P))
        if 'linux' in sys.platform.lower():
            print('%sAnda Menggunakan %sLinux %s( %sEx : Termux Android%s ),\nKetik :'%(P,M,P,M,P))
            print('   %s$ %spkg install libsodium'%(M,P))
            print('   %s$ %sSODIUM_INSTALL=system pip install pynacl'%(M,P))
        elif 'win' in sys.platform.lower():
            print('%sAnda Menggunakan %sWindows%s/%sMacOS%s,\nKetik :'%(P,M,P,M,P))
            print('   %s$ %spip install pynacl'%(M,P))
        exit('')
    try:
        from source import login, dump
    except Exception as e:
        print(e)
        exit('\n%sHayoo Mau %sNgoprek %sFile Yaa :v\n'%(P,M,P))
    clear()
    login.login()
    dump.main_menu()

if __name__ == '__main__':
    run()