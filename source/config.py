import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME","AgCFoxZmFiS11zcF7-v-iwtwUdD39ElyVbw-yd7eprxcYJMTsn7J0Qdx9hRe-ro9mifsoI0G9tmUTSjkseYoTRhMezV_J7tX6uv4W5V-2EwBIPO9NPYX_3uDVc7E17lIKGYHEgSQXjEiiLx05aHZptjpKO61cAm0QOZbfb7O7X45U2iH2kkblgCeky3cr_HO0HIdGTIuc0ID2ufq8Dk0x_JL__s_GpNiZG_iPChgDXlpUFUMlxbL3juxB9mGxXW9uBORSMlcUh-iDv7Kj9trTV0iKEIYOfTQqvVflCG1ndZ_ghdLWFIVmLehMhDZLYsUwMZbwQGNuHyaqkr1OK4fhaSAAAAAATT5m38A")
BOT_TOKEN = getenv("BOT_TOKEN","5708160276:AAEOM8VzZtlLQcZUJAWoT-C07tp94cYSI-M")
API_ID = int(getenv("API_ID","16407047"))
API_HASH = getenv("API_HASH","dc1788e5e1a0db7563cf5204a865dba8")
OWNER_NAME = getenv("OWNER_NAME", "Ronylion")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vlorantt")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://lucifer:ASShaw96@lucifer.vuows.mongodb.net/lucifer?retryWrites=true&w=majority")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4c7636b9c50116387d9f6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
FORCE_SUBSCRIBE_TEXT = getenv("SUBSCRIBE_TEXT", f"عليك الاشتراك في قناة البوت لتتمكن من استخدامة \n- @{UPDATES_CHANNEL}")
SUBSCRIBE = getenv("SUBSCRIBE", "no")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1221506767").split()))
