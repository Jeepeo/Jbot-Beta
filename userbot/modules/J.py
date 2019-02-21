import bs4
import requests
import os
import re
import subprocess
import time
import random
from datetime import datetime, timedelta

import urbandict
import wikipedia
from google_images_download import google_images_download
from googletrans import Translator
from gtts import gTTS
from telethon import TelegramClient, events
from pyfiglet import Figlet

from userbot import LOGGER, LOGGER_GROUP, bot

langi = "en"


@bot.on(events.NewMessage(pattern=".lang", outgoing=True))
@bot.on(events.MessageEdited(pattern=".lang", outgoing=True))
async def lang(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        global langi
        message = await bot.get_messages(e.chat_id)
        langi = str(message[0].message[6:])
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP, "tts language changed to **" + langi + "**"
            )
            await e.edit("tts language changed to **" + langi + "**")


#ASCII figlet fonts--->

@bot.on(events.NewMessage(pattern='^\.figlet (.+)'))
@bot.on(events.MessageEdited(pattern='^\.figlet (.+)'))
async def figlety(e):
	l=['figlet']
	l+=e.pattern_match.group(1).split(' ')
	p='```'
	p+=subprocess.run(l, stdout=subprocess.PIPE).stdout.decode()
	p+='```'
	await e.edit(p)


@bot.on(events.NewMessage(outgoing=True, pattern="^Oof$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^Oof$"))
async def lol(e):
    t = "Oof"
    for j in range(10):
        t = t[:-1] + "of"
        await e.edit(t)



 #An sucking module, so leave it
@bot.on(events.NewMessage(outgoing=True, pattern="^.smk (.*)"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.smk (.*)"))
async def smrk(e):
        if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
            textx = await e.get_reply_message()
        message=e.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message)
        reactor = [
                "ツ",
                "ツ",
                "ツ",
        ]
        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(reactor), reply_text)
        reply_text += " " + random.choice(reactor)
        await e.edit(reply_text)
