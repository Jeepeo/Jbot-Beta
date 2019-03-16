# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD

from random import randint
from subprocess import PIPE
from subprocess import run as runapp
from time import sleep

import hastebin
import pybase64
from requests import get, post

from userbot import LOGGER, LOGGER_GROUP, HELPER
from userbot.events import register


@register(outgoing=True, pattern="^.random")
async def randomise(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        r = (e.text).split()
        index = randint(1, len(r) - 1)
        await e.edit("**Query: **\n`" + e.text + "`\n**Output: **\n`" + r[index] + "`")


@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(e):
    message = e.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in e.pattern_match.group(1):
            await e.reply("Syntax: `.sleep [seconds]`")
        else:
            counter = int(e.pattern_match.group(1))
            await e.edit("`I am sulking and snoozing....`")
            sleep(2)
            if LOGGER:
                await e.client.send_message(
                    LOGGER_GROUP,
                    "You put the bot to sleep for " + str(counter) + " seconds",
                )
            sleep(counter)


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(e):
    if not e.text[0].isalpha():
        await e.edit("`Goodbye *Windows XP shutdown sound*....`")
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#SHUTDOWN \n"
                "Bot shutted down")
        await e.client.disconnect()


@register(outgoing=True, pattern="^.support$")
async def bot_support(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
<<<<<<< HEAD
        await e.edit("Report Damn bugs here: @userbot_support")
=======
        await e.edit("Link Portal: @userbot_support")
>>>>>>> 6c5b29d... Helper: Adding helpers at all modules, also split up misc


@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
<<<<<<< HEAD
        await e.edit("https://github.com/jeepeo/")


@register(outgoing=True, pattern="^.supportchannel$")
async def support_channel(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("t.me/maestro_userbot_channel")


@register(outgoing=True, pattern="^.userid$")
async def chatidgetter(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = await e.get_reply_message()
        if message:
            if not message.forward:
                user_id = message.sender.id
                if message.sender.username:
                    name = "@" + message.sender.username
                else:
                    name = "**" + message.sender.first_name + "**"

            else:
                user_id = message.forward.sender.id
                if message.forward.sender.username:
                    name = "@" + message.forward.sender.username
                else:
                    name = "*" + message.forward.sender.first_name + "*"
            await e.edit(
                "**Name:** {} \n**User ID:** `{}`"
                .format(name, user_id)
            )


@register(outgoing=True, pattern="^.unmutechat$")
async def unmute_chat(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.keep_read_sql import unkread
        except:
            await e.edit('`Running on Non-SQL Mode!`')
        unkread(str(e.chat_id))
        await e.edit("```Unmuted this chat Successfully```")


@register(outgoing=True, pattern="^.mutechat$")
async def mute_chat(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.keep_read_sql import kread
        except Exception as er:
            print(er)
            await e.edit("`Running on Non-SQL mode!`")
            return
        await e.edit(str(e.chat_id))
        kread(str(e.chat_id))
        await e.edit("`Shush! This chat will be silenced!`")
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                str(e.chat_id) + " was silenced.")


@register(incoming=True)
async def keep_read(e):
    try:
        from userbot.modules.sql_helper.keep_read_sql import is_kread
    except:
        return
    K = is_kread()
    if K:
        for i in K:
            if i.groupid == str(e.chat_id):
                await e.client.send_read_acknowledge(e.chat_id)
=======
        await e.edit("https://github.com/baalajimaestro/Telegram-UserBot/")
>>>>>>> 6c5b29d... Helper: Adding helpers at all modules, also split up misc
