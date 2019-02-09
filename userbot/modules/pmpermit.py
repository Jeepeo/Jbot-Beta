import sqlite3

from telethon import events
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.messages import ReportSpamRequest

from userbot import COUNT_PM, LOGGER, LOGGER_GROUP, NOTIF_OFF, PM_AUTO_BAN, bot


@bot.on(events.NewMessage(incoming=True))
@bot.on(events.MessageEdited(incoming=True))
async def permitpm(e):
    if PM_AUTO_BAN:
        global COUNT_PM
        if e.is_private and not (await e.get_sender()).bot:
            try:
                from userbot.modules.sql_helper.pm_permit_sql import is_approved
            except:
                return
            apprv = is_approved(e.chat_id)

            if not apprv and e.text != \
                ("`Don't Afraid!😳 This is Jeepeo😎's BOT\n\n`"
                 "`Jeepeo😎 hasn't approved you to PM😢.`"
                 "`Please wait for Jeepeo😎 to look in, he would mostly approve PMs😲.`\n\n"
                 "`As I know , He doesn't reply to shit/retards😤.`"):

                await e.reply(
                ("`Don't Afraid!😳 This is Jeepeo😎's BOT\n\n`"
                 "`Jeepeo😎 hasn't approved you to PM😢.`"
                 "`Please wait for Jeepeo😎 to look in, he would mostly approve PMs😲.`\n\n"
                 "`As I know , He doesn't reply to shit/retards😤.`"
                )

                if e.chat_id not in COUNT_PM:
                    COUNT_PM.update({e.chat_id: 1})
                else:
                    COUNT_PM[e.chat_id] = COUNT_PM[e.chat_id] + 1
                if COUNT_PM[e.chat_id] > 4:
                    await e.respond(
                        "`You were spamming Jeepeo😎's PM, which I don't like.`"
                        "`I'mma Report Spam.`"
                    )
                    del COUNT_PM[e.chat_id]
                    await bot(BlockRequest(e.chat_id))
                    await bot(ReportSpamRequest(peer='e.chat_id'))
                    if LOGGER:
                        name = await bot.get_entity(e.chat_id)
                        name0 = str(name.first_name)
                        await bot.send_message(
                            LOGGER_GROUP,
                            "["
                            + name0
                            + "](tg://user?id="
                            + str(e.chat_id)
                            + ")"
                            + " was just another retarded nibba",
                        )


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifoff$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifoff$"))
async def notifoff(e):
    global NOTIF_OFF
    NOTIF_OFF = True
    await e.edit("`Notifications silenced!`")


@bot.on(events.NewMessage(outgoing=True,pattern="^.notifon$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifon$"))
async def notifon(e):
    global NOTIF_OFF
    NOTIF_OFF = False
    await e.edit("`Notifications unmuted!`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.approve$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.approve$"))
async def approvepm(apprvpm):
    if not apprvpm.text[0].isalpha() and apprvpm.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except:
            await apprvpm.edit("`Running on Non-SQL mode!`")
            return
        approve(apprvpm.chat_id)
        await apprvpm.edit("`Great!😝 , You can now PM Jeepo😎.`")
        if LOGGER:
            aname = await bot.get_entity(apprvpm.chat_id)
            name0 = str(aname.first_name)
            await bot.send_message(
                LOGGER_GROUP,
                "["
                + name0
                + "](tg://user?id="
                + str(apprvpm.chat_id)
                + ")"
                + " Great!😝 , You can now PM Jeepeo😎",
            )
