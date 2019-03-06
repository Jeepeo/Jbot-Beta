import asyncio
import inspect
import subprocess
from getpass import getuser

import hastebin
from telethon import TelegramClient, events
from userbot import bot
from telethon.events import StopPropagation

from userbot import *
from userbot.events import register


@register(outgoing=True, pattern="^.eval")
async def evaluate(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.is_channel and not e.is_group:
            await e.edit("`Eval isn't permitted on channels`")
            return
        evaluation = eval(e.text[6:])
        if evaluation:
            if isinstance(evaluation) == "str":
                if len(evaluation) > 4096:
                    f = open("output.txt", "w+")
                    f.write(evaluation)
                    f.close()
                await e.client.send_file(
                    e.chat_id,
                    "output.txt",
                    reply_to=e.id,
                    caption="`Output too large, sending as file`",
                )
                subprocess.run(["rm", "sender.txt"], stdout=subprocess.PIPE)
        await e.edit(
            "**Query: **\n`"
            + e.text[6:]
            + "`\n**Result: **\n`"
            + str(evaluation)
            + "`"
        )
    else:
        await e.edit(
            "**Query: **\n`"
            + e.text[6:]
            + "`\n**Result: **\n`No Result Returned/False`"
        )
    if LOGGER:
        await e.client.send_message(
            LOGGER_GROUP, "Eval query " +
            e.text[6:] + " was executed successfully"
        )


@register(outgoing=True, pattern=r"^.exec (.*)")
async def run(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        if e.is_channel and not e.is_group:
            await e.edit("`Exec isn't permitted on channels`")
            return
        code = e.raw_text[5:]
        exec(f"async def __ex(e): " + "".join(f"\n {l}" for l in code.split("\n")))
        result = await locals()["__ex"](e)
        if result:
            if len(result) > 4096:
                f = open("output.txt", "w+")
                f.write(result)
                f.close()
                await e.client.send_file(
                    e.chat_id,
                    "output.txt",
                    reply_to=e.id,
                    caption="`Output too large, sending as file`",
                )
                subprocess.run(["rm", "output.txt"], stdout=subprocess.PIPE)
            await e.edit(
                "**Query: **\n`" + e.text[5:] + "`\n**Result: **\n`" + str(result) + "`"
            )
        else:
            await e.edit(
                "**Query: **\n`"
                + e.text[5:]
                + "`\n**Result: **\n`"
                + "No Result Returned/False"
                + "`"
            )
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "Exec query " + e.text[5:] + " was executed successfully"
            )


#=====YOU FOUND EASTER EGG ===========
 
        #Geg is gei
