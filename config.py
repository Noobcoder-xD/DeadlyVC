import os
from os import listdir, mkdir
from os import getenv
from dotenv import load_dotenv




""" config area """

load_dotenv()
admins = {}

#REQUIRED
API_ID = int(getenv("API_ID", "29400566"))
API_HASH = getenv("API_HASH", "8fd30dc496aea7c14cf675f59b74ec6f")
BOT_TOKEN = getenv("BOT_TOKEN", "6935496455:AAGndnOEhoNwWrtMzfGCEipdIQruucVVWdg") 
DB_URL = getenv("DB_URL", "mongodb+srv://developervro:developerrapuka@cluster9.gcj9754.mongodb.net/?retryWrites=true&w=majority&appName=Cluster9") 
LOG_ID = int(getenv("LOG_ID", "-1001959134296")) 
OWNER_ID = int(getenv("OWNER_ID", "6903041211"))

GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/MusicSycoSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/MusicSycoSupport")
ALIVE_NAME = getenv("ALIVE_NAME", "Bellala Music")
OWNER_NAME = getenv("OWNER_NAME", "Bellala pavan")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5937170640").split()))


if str(getenv("STRING_SESSION1")).strip() == "BQHBxJYAdnLlQ9ZQp_D-E7vP8beasWshUchGgxH-1mHHNBgtiJ0cP8NLqKTWK62OFtl5agF4gdn20Ts6o25__HNNVfl8ObN3T0SUOKbjB4miHid9iCmLzsVV2RsGvon2mdP-6wHGX7Rnn78yZTWD3v7NsY7q19n0o2JRGYHiJJzJ3woJ6uPc5BKBK1GLsSHm_QKyQkNbIvHK4kTMN6-bub4Y3PWYMoJxlQ-3IKB8wesizEkP0qrbEVau66VKMD7kAaRaSwmdzl9VvkSHXWsNCY0UnU4lHdBVmprjUmHONkd0BRyjDp6BOcmiaIfKMv4occIWi_qzKh4DDzNBEvTxrvjs1yZkgQAAAAGksOwYAA":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))


#EXTRA
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Noobcoder-xD/DeadlyVC")


#IMAGES
START_IMG = getenv("START_IMG", None) 
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/1fe6ea0b46335debc49e6.png") # FOR TELEGRAM STREAMING
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
PING_URL = getenv(" PING_URL", "https://te.legra.ph/file/abfcbebb3d9d8efbb7762.jpg") 
