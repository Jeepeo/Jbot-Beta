import sqlite3
import subprocess
import sys
import os
import logging
import time
import dotenv
from alchemysession import AlchemySessionContainer
from sqlalchemy import create_engine
from telethon import TelegramClient, events

def is_bool(a):
    if a == "True":
        return True
    elif a == "False":
        return False

dotenv.load_dotenv("config.env")
UPDATER = os.environ.get("UPDATER", None)
BUILD_CHOICE = os.environ.get("BUILD_CHOICE", "stable")
subprocess.run(["rm", "-rf", "brains.check"], stdout=subprocess.PIPE)
subprocess.run(
    [
        "curl",
        "-sLo",
        "brains.check",
        "https://storage.googleapis.com/project-aiml-bot/brains.check",
    ],
    stdout=subprocess.PIPE,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
LOGS = logging.getLogger(__name__)

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGS.error(
        "You MUST have a python version of at least 3.6." \
        "Multiple features depend on this. Bot quitting."
    )
    quit(1)
try:
    print(___________PLOX_______REMOVE_____THIS_____LINE__________)
except NameError:
    API_KEY = os.environ.get("API_KEY", None)

    API_HASH = os.environ.get("API_HASH", None)

    LOGGER_GROUP = int(os.environ.get("LOGGER_GROUP", "0"))

    LOGGER = is_bool(os.environ.get(
        "LOGGER", None
    ))  # Incase you want to turn off logging, put this to false

    PM_AUTO_BAN = is_bool(os.environ.get("PM_AUTO_BAN", None))

    CONSOLE_LOGGER_VERBOSE = is_bool(os.environ.get("CONSOLE_LOGGER_VERBOSE", None))

    DB_URI = os.environ.get("DATABASE_URL", None)

    SCREENSHOT_LAYER_ACCESS_KEY = os.environ.get("SCREENSHOT_LAYER_ACCESS_KEY", None)

    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)

    SUDO = os.environ.get("SUDO", None)
    if CONSOLE_LOGGER_VERBOSE:
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            level=logging.DEBUG,
        )
        LOGS = logging.getLogger(__name__)
else:
    LOGS.error(
        "Your config file seems to be un-edited."
        "Doing so is not allowed. Bot exiting!"
    )
    quit(1)
bot = TelegramClient("userbot", API_KEY, API_HASH)

# Global Variables
SNIPE_TEXT = ""
COUNT_MSG = 0
BRAIN_CHECKER = []
USERS = {}
GROUPS = {}
SPAM = False
WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000
COUNT_PM = {}
ISAFK = False
ENABLE_KILLME = True
SNIPE_ID = 0
MUTING_USERS = {}
MUTED_USERS = {}
AFKREASON = "No Reason "
SPAM_ALLOWANCE = 3
SPAM_CHAT_ID = []
DISABLE_RUN = False
NOTIF_OFF = False
