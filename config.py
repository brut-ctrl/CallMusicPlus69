# Don't ask me why this looks like a fucking shit! Just go and make a fukcking PR as i'm fucking lazy to do these things! Fuck Off!

import os
from os import getenv

from pyrogram import Client
from dotenv import load_dotenv
from helpers.modhelps import fetch_heroku_git_url

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQBW611u38-5R86xZ_xxjwl4ge4MJyevKAOea2_E6m7I_XAM6iE1tL70rlprNHCs5Zaun4sUSOVkqxeu9Mr93JWV8X9BVbH3cUBTwOdH2O-pgeaUSP-U2tAbQEInLvzjEjjAq3Ov9W-0SHIc5I7naYr_CCDERZBtHaOyBh1prPG-EqE7hYj4Z-69QEiEd2klI0vzXYZNy59GZX8G_fVmU-AWAurPEU_ORKr6ZnbG1S6Io0-_hGx_1RmLERAVzj2yb8NxIWWTX9eEvmzOR6F1xGxt0uUs0jisu1revi_ILQm3G_fifXfzy63QV_qSNzcQ12mLR-hLCz9VPUcSoYpBFJGJbIeuqQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1941313517:AAFsKQ46fS8BgUz1bjDFAo8dmO_62r_UQdI")

API_ID = int(getenv("API_ID", "7341107"))
API_HASH = getenv("API_HASH", "881759527a6576b21c5fc632c2472de3")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

# Your Telegram User ID
BOT_OWNER = int(os.environ.get("BOT_OWNER", "1408440765"))
# Sudo users IDs, They are admins everywhere
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "712147852 1408440765 1944787421 1820831401 1945910995 1909021805 1605366945").split()))
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
