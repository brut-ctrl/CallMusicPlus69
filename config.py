# Don't ask me why this looks like a fucking shit! Just go and make a fukcking PR as i'm fucking lazy to do these things! Fuck Off!

import os
from os import getenv

from pyrogram import Client
from dotenv import load_dotenv
from helpers.modhelps import fetch_heroku_git_url

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQCsHOo9DtXewJC0VCFhmYD3sREEYZHAbLuckjF6RWv_28hzKX9Y-P3y-Yi2jXABEvRNCodtOHDa9Jbu33JsXTQYwwRKlR4PQUEtXmbyRxCdhzRMP6AwlDoFNO0gxi0S2bI0yl0XbhnJKLE43KEgHAjX9XyJfIbyxrQurde7RxwmKRJ2jUSHgMMmZEegeDIJyn4jA5TLDqnKwHW51Bqg9CMytcvvCrEEbxOgne9zdxjIhpH8M3PXmnHbgm9z3wAAO4KsMngggDYwZP2-L_kQDnV3qyxGB1ilhehO6sNX2LzA7f-CHvGAIylaAdTKGFotxILbPwUd5bOKuo3gQyv2a8CrbIeuqQA")
BOT_TOKEN = getenv("1941313517:AAFsKQ46fS8BgUz1bjDFAo8dmO_62r_UQdI")

API_ID = int(getenv("7341107"))
API_HASH = getenv("881759527a6576b21c5fc632c2472de3")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "18"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

# Your Telegram User ID
BOT_OWNER = int(os.environ.get("1408440765"))
# Sudo users IDs, They are admins everywhere
SUDO_USERS = list(map(int, getenv("1408440765 712147852 1820831401 1605366945").split()))
# Your Bot's Username without "@"
BOT_USERNAME = os.environ.get("CallMusicPlusBot")
# Your MongoDB url
DATABASE_URL = os.environ.get("mongodb+srv://brut69:HWxGlBegyXXq62Jv@cluster0.l50db.mongodb.net/brut69@admin?retryWrites=true&w=majority")
# Your Log Channel! Make a private channel and get it's ID
LOG_CHANNEL = int(os.environ.get("-1001510441068"))
# If you need to broadcast messages as a copy or Forwarded Message
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
# Thumbnail URL
THUMB_URL = os.environ.get("THUMB_URL", "https://telegra.ph/file/1abf425f2015c0f28d3fa.png")
# Your Updates Channel! Don't Put Anything If you don't have one
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "queengemoy_project")

# Your ARQ API Key
ARQ_API_KEY = getenv("ARQ_API_KEY")
# Don't Change Anything Here
ARQ_API_URL = "https://thearq.tech/"

# Updator Configs
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/brut-crtl/CallMusicPlus69")
U_BRANCH = "main"
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)

# Versions
cp_version = "v2.9.3.2"
nexaub_version = "v0.4"
