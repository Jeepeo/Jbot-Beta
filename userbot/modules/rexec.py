import re
from userbot.modules.rextester.api import rexec, UnknownLanguage
from telethon import events
from userbot import bot
from userbot.events import register


@register(outgoing=True, pattern="^.rex$")
async def rextestercli(event):
    stdin = ""
    message = event.text.split("rex ", 1)
    chat = await event.get_chat()

    if len(message) < 2:
        await bot.update_message(event, REX_HELP)
        return

    regex = re.search(
        r"([\w.#+]+)\s+([\s\S]+?)(?:\s+\/stdin\s+([\s\S]+))?$",
        message[1],
        re.IGNORECASE,
    )
    language = regex.group(1)
    code = regex.group(2)
    stdin = regex.group(3)

    try:
        res = await rexec(language, code, stdin)
    except UnknownLanguage as exc:
        await bot.update_message(event, str(exc))
        return

    output = f"**Language:**\n\n```{language}```"
    output += f"\n\n**Source:** \n\n```{code}```"

    if res.results:
        output += f"\n\n**Result:** \n\n```{res.result}```"

    if res.warnings:
        output += f"\n\n**Warnings:** \n\n```{res.warnings}```\n"

    if res.errors:
        output += f"\n\n**Errors:** \n\n```{res.errors}```"


    if len(output) > 4096:
        with io.BytesIO(str.encode(output)) as out_file:
            out_file.name = "output.txt"
            await bot.send_file(chat.id, file=out_file)
            await bot.update_message(event, code)
        return

    await bot.update_message(event, output)
