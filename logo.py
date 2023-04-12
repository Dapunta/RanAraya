#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = '082245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> oImprt Module
import sys, time

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

#--> Animasi
def urut(i,t):
    for e in i + '\n': sys.stdout.write(e); sys.stdout.flush(); time.sleep(t)

#--> Logo
def logo():
    sp = ' '*7
    print('   %s%s_____                                         %s_____'%(sp,M,M))
    print('  %s%s/  _  \___________________ ___  __            %s/  _  \\'%(sp,M,M))
    print(' %s%s/  /_\  \_  __ \_  __ \__  \\\  \|  |  %s______  %s/  / \  \\'%(sp,M,P,M))
    print('%s%s/    |    \  | \/|  | \// __ \\\  |  | %s/_____/ %s/  /___\  \\'%(sp,M,P,M))
    print('%s%s\____|____/__|   |__|  (______\\\_   |        %s/  _______  \\'%(sp,M,M))
    print('   %s%sMulti Brute Force FB  %s/__________/       %s/__/  %s0.1  %s\__\\\n'%(sp,P,M,M,P,M))
    urut('       %s%s─────────────── %s• %sRan_Arraya %s• %s───────────────\n%s'%(sp,Z,M,P,M,Z,P),0.005)