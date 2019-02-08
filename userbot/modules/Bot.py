from userbot import bot
from telethon import events


@bot.on(events.NewMessage(outgoing=True, pattern="^.alive$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.alive$"))
async def amialive(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`╲╲╭━━━━╮
                       ╭╮┃▆┈┈▆┃╭╮
                       ┃╰┫▽▽▽┣╯┃
                       ╰━┫△△△┣━╯
                       ╲╲┃┈┈┈┈┃
                       ╲╲┃┈┏┓┈┃ `")

