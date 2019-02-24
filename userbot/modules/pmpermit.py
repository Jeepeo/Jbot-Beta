import sqlite3
import time

from telethon import events
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest

from userbot import COUNT_PM, LOGGER, LOGGER_GROUP, NOTIF_OFF, PM_AUTO_BAN
from userbot.events import register


@register(incoming=True)
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
                ("`Don't Afraid!😳 This is Jeepeo😎's BOT \n\n`"
                 "`Jeepeo😎 hasn't approved you to PM😢.`"
                 "`Please wait for Jeepeo😎 to look in, he would mostly approve PMs😲.`\n\n"
                 "`As I know , He doesn't reply to shit/retards😤.`"):

                await e.reply(
                    "`Don't Afraid!😳 This is Jeepeo😎's BOT \n\n`"
                    "`Jeepeo😎 hasn't approved you to PM😢.`"
                    "`Please wait for Jeepeo😎 to look in, he would mostly approve PMs😲.`\n\n"
                    "`As I know , He doesn't reply to shit/retards😤.`"
                )

                if NOTIF_OFF:
                    await e.client.send_read_acknowledge(e.chat_id)
                if e.chat_id not in COUNT_PM:
                    COUNT_PM.update({e.chat_id: 1})
                else:
                    COUNT_PM[e.chat_id] = COUNT_PM[e.chat_id] + 1
                if COUNT_PM[e.chat_id] > 4:
                    await e.respond(
                        "`You were spamming my Master's PM, which I don't like.`"
                        "`I'mma Report Spam.`"
                    )
                    del COUNT_PM[e.chat_id]
                    await e.client(BlockRequest(e.chat_id))
                    await e.client(ReportSpamRequest(peer=e.chat_id))
                    if LOGGER:
                        name = await e.client.get_entity(e.chat_id)
                        name0 = str(name.first_name)
                        await e.client.send_message(
                            LOGGER_GROUP,
                            "["
                            + name0
                            + "](tg://user?id="
                            + str(e.chat_id)
                            + ")"
                            + " was just another retarded nibba",
                        )


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern="^.notifoff$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifoff$"))
=======
@register(outgoing=True, pattern="^.notifoff$")
>>>>>>> 5a5621a... Merge pull request #38 from YouTwitFace/staging
async def notifoff(e):
    global NOTIF_OFF
    NOTIF_OFF = True
    await e.edit("`Notifications silenced!`")


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern="^.notifon$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.notifon$"))
=======
@register(outgoing=True, pattern="^.notifon$")
>>>>>>> 5a5621a... Merge pull request #38 from YouTwitFace/staging
async def notifon(e):
    global NOTIF_OFF
    NOTIF_OFF = False
    await e.edit("`Notifications unmuted!`")


@register(outgoing=True, pattern="^.approve$")
async def approvepm(apprvpm):
    if not apprvpm.text[0].isalpha() and apprvpm.text[0] not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.pm_permit_sql import approve
        except:
            await apprvpm.edit("`Running on Non-SQL mode!`")
            return

        if apprvpm.reply_to_msg_id:
            reply = await apprvpm.get_reply_message()
            replied_user = await apprvpm.client(GetFullUserRequest(reply.from_id))
            aname = replied_user.user.id
            name0 = str(replied_user.user.first_name)
            approve(replied_user.user.id)
        else:
            approve(apprvpm.chat_id)
            aname = await apprvpm.client.get_entity(apprvpm.chat_id)
            name0 = str(aname.first_name)

        await apprvpm.edit(
            f"[{name0}](tg://user?id={apprvpm.chat_id}) `Approved to PM!`"
            )

        if LOGGER:
            await apprvpm.client.send_message(
                LOGGER_GROUP,
                f"[{name0}](tg://user?id={apprvpm.chat_id})"
                " was approved to PM you.",
            )


<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern="^.block$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.block$"))
=======
@register(outgoing=True, pattern="^.block$")
>>>>>>> 5a5621a... Merge pull request #38 from YouTwitFace/staging
async def blockpm(block):
    if not block.text[0].isalpha() and block.text[0] not in ("/", "#", "@", "!"):

        await block.edit("`You are gonna be blocked from PM-ing my Master!`")

        if block.reply_to_msg_id:
            reply = await block.get_reply_message()
            replied_user = await block.client(GetFullUserRequest(reply.from_id))
            aname = replied_user.user.id
            name0 = str(replied_user.user.first_name)
            await block.client(BlockRequest(replied_user.user.id))
            try:
                from userbot.modules.sql_helper.pm_permit_sql import dissprove
                dissprove(replied_user.user.id)
            except Exception:
                pass
        else:
            await block.client(BlockRequest(block.chat_id))
            aname = await block.client.get_entity(block.chat_id)
            name0 = str(aname.first_name)
            try:
                from userbot.modules.sql_helper.pm_permit_sql import dissprove
                dissprove(block.chat_id)
            except Exception:
                pass

        if LOGGER:
            await block.client.send_message(
                LOGGER_GROUP,
                f"[{name0}](tg://user?id={block.chat_id})"
                " was blocc'd!.",
            )

<<<<<<< HEAD
@bot.on(events.NewMessage(outgoing=True,pattern="^.unblock$"))
@bot.on(events.MessageEdited(outgoing=True,pattern="^.unblock$"))
=======

@register(outgoing=True, pattern="^.unblock$")
>>>>>>> 5a5621a... Merge pull request #38 from YouTwitFace/staging
async def unblockpm(unblock):
    if not unblock.text[0].isalpha() and unblock.text[0] \
            not in ("/", "#", "@", "!") and unblock.reply_to_msg_id:

        await unblock.edit("`My Master has forgiven you to PM now`")

        if unblock.reply_to_msg_id:
            reply = await unblock.get_reply_message()
            replied_user = await unblock.client(GetFullUserRequest(reply.from_id))
            name0 = str(replied_user.user.first_name)
            await unblock.client(UnblockRequest(replied_user.user.id))

        if LOGGER:
            await unblock.client.send_message(
                LOGGER_GROUP,
                f"[{name0}](tg://user?id={unblock.chat_id})"
                " was unblocc'd!.",
            )
