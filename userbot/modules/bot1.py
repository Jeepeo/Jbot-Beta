from userbot import bot
from telethon import events


@bot.on(events.NewMessage(outgoing=True, pattern="^.bot$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.bot$"))
async def amialive(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")


@bot.on(events.NewMessage(outgoing=True, pattern="^.lol$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.lol$"))
async def amialive(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")

@bot.on(events.NewMessage(outgoing=True, pattern="^.hey$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.hey$"))
async def amialive(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HEY!┊😀`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HEY!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.bover$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.bover$"))
async def amialive(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
<<<<<<< HEAD
        await e.edit("`UserBot version : 2.2-a\nBranch : Staging\nAt commit : 689`"
                      "`\nLast update ------\n  Jeepeo😎 Edition 2.1`")
=======
        await e.edit("`UserBot version : 2.2-a\nBranch : Staging\nAt commit : 691`"
                      "`\nLast update ------\n  Jeepeo😎 Edition 2.0`")
>>>>>>> db583b2fed49318882411a31c8a8c3762829c108
