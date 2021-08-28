# Don't ask me why this looks like a fucking shit! Just go and make a fukcking PR as i'm fucking lazy to do these things! Fuck Off!

import os
from os import getenv

from pyrogram import Client
from dotenv import load_dotenv
from helpers.modhelps import fetch_heroku_git_url

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQC2Hm7LoMxH52ZSxo6uMfrfrLtkin6tNHLZpV_ripnwYBaxd6evFjtV-_3YqbsEQQeEYgHjTV-AytJJu38OaqYFwffBF8D9NVODqe0qmX3Es_S9UbFZFGqwGwEdDPhWjh5OEcOpNjukGMkMy3lBBbleM2ZR363KHu91m0UVgrIu05PW6HDJnMeB7AT18Y5gI1Brg2ASDtJguaCL2_esDSGn1vyPco8FIawt8T_qsNAvxRLWy-ooC5FADTdxq3RReDvUV6lnsWjjbFs3OIc32Iw85MORhFZ1i5kSQIWb0XD5qwx4U2CHk7JW_G3a5wBkszYJuE-eZ-ICRPwK6-ABSfMubIeuqQA)
BOT_TOKEN = getenv("BOT_TOKEN", "1941313517:AAFsKQ46fS8BgUz1bjDFAo8dmO_62r_UQdI")

API_ID = int(getenv("API_ID", "7341107"))
API_HASH = getenv("API_HASH", "881759527a6576b21c5fc632c2472de3")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())

# Your Telegram User ID
BOT_OWNER = int(os.environ.get("BOT_OWNER", "1408440765"))
# Sudo users IDs, They are admins everywhere
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# Your Bot's Username without "@"
BOT_USERNAME = os.environ.get("BOT_USERNAME", "CallMusicPlusBot")
# Your MongoDB url
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://brut69:HWxGlBegyXXq62Jv@cluster0.l50db.mongodb.net/brut69@admin?retryWrites=true&w=majority")
# Your Log Channel! Make a private channel and get it's ID
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001302544520"))
# If you need to broadcast messages as a copy or Forwarded Message
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
# Thumbnail URL
THUMB_URL = os.environ.get("THUMB_URL", "https://telegra.ph/file/1abf425f2015c0f28d3fa.png")
# Your Updates Channel! Don't Put Anything If you don't have one
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "dunottagme")

# Your ARQ API Key
ARQ_API_KEY = getenv("ARQ_API_KEY", "JKKWZI-AKBCEI-XIROOB-XQNIZI-ARQ")
# Don't Change Anything Here
ARQ_API_URL = "https://thearq.tech/"

# Updator Configs
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/brut-ctrl/CallMusicPlus69")
U_BRANCH = "main"
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

# Versions
cp_version = "v2.9.3.2"
nexaub_version = "v0.4"
