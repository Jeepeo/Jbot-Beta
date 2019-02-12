from time import sleep

from telethon import events
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest

from telethon.tl.types import ChatAdminRights, ChatBannedRights

from userbot import (BRAIN_CHECKER, LOGGER, LOGGER_GROUP, bot)


@bot.on(events.NewMessage(outgoing=True, pattern="^.promote$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.promote$"))
async def promote(promt):
    """ For .promote command, do promote targeted person """
    if not promt.text[0].isalpha() \
            and promt.text[0] not in ("/", "#", "@", "!"):
        chats = await promt.get_chat()
        admin = chats.admin_rights
        creator = chats.creator
        new_rights = ChatAdminRights(
            add_admins=True,
            invite_users=True,
            change_info=True,
            ban_users=True,
            delete_messages=True,
            pin_messages=True
        )

        # Self explanatory
        if not await promt.get_reply_message():
            await promt.edit("`Give a reply message`")
        elif not admin and creator:
            rights = new_rights
        elif not admin and not creator:
            rights = None
<<<<<<< HEAD
        await promt.edit("`Bitch! You are being promoted.....`")
        time.sleep(3)
=======
        await promt.edit("`Promoting...`")
>>>>>>> 21e9b94... [REFACTOR]: module: admin: Cleanups

        # Try to promote if current user is admin or creator
        try:
            await bot(
                EditAdminRequest(promt.chat_id,
                                 (await promt.get_reply_message()).sender_id,
                                 rights)
            )

        # If Telethon spit BadRequestError, assume
        # we don't have Promote permission
        except BadRequestError:
            await promt.edit(
                "`Ooof ! Jeepeo😎 ,You are not admin in this **CANCEROUS** group `"
                )
            return
        await promt.edit("`You Promoted Successfully!`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.demote$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.demote$"))
async def demote(dmod):
    """ For .demote command, do demote targeted person """
    if not dmod.text[0].isalpha() and dmod.text[0] not in ("/", "#", "@", "!"):
        # Get targeted chat
        chat = await dmod.get_chat()
        # Grab admin status or creator in a chat
        admin = chat.admin_rights
        creator = chat.creator

        # If there's no reply, return
        if not await dmod.get_reply_message():
            await dmod.edit("`Give a reply message`")
            return
        # If not admin and not creator, also return
        if not admin and not creator:
            await dmod.edit("`You aren't an admin!`")
            return

        # If passing, declare that we're going to demote
        await dmod.edit("`Demoting...`")

        # New rights after demotion
        newrights = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None
        )
        # Edit Admin Permission
        try:
            await bot(
                EditAdminRequest(dmod.chat_id,
                                 (await dmod.get_reply_message()).sender_id,
                                 newrights)
            )

        # If we catch BadRequestError from Telethon
        # Assume we don't have permission to demote
        except BadRequestError:
            await dmod.edit("`You Don't have sufficient permissions to demhott`")
            return
        await dmod.edit("`Demoted Successfully!`")


@bot.on(events.NewMessage(outgoing=True, pattern="^.ban$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.ban$"))
async def thanos(bon):
    """ For .ban command, do "thanos" at targeted person """
    if not bon.text[0].isalpha() and bon.text[0] not in ("/", "#", "@", "!"):
        banned_rights = ChatBannedRights(
            until_date=None,
            view_messages=True,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
        )

<<<<<<< HEAD
        reply_id = await bon.get_reply_message().sender_id
=======
        # For dealing with reply-at-ban
        sender = await bon.get_reply_message()

        # If the user is a sudo
>>>>>>> 21e9b94... [REFACTOR]: module: admin: Cleanups
        try:
            if reply_id in BRAIN_CHECKER:
                await bon.edit("`Ban Error! I am not supposed to ban this user`")
                return

        # This exception handled if the user doesn't
        # Specifying any target (reply in this case)
        except AttributeError:
            return

        # Announce that we're going to whacking the pest
        await bon.edit("`Whacking the pest!`")
        try:
            await bot(
                EditBannedRequest(
<<<<<<< HEAD
                    bon.chat_id, reply_id, rights
                )
            )
        except AttributeError:
            await bon.edit("`Y u no give target`")
=======
                    bon.chat_id,
                    sender.sender_id,
                    banned_rights
                )
            )

        # ExceptionHandling if the user is a Sudo
>>>>>>> 21e9b94... [REFACTOR]: module: admin: Cleanups
        except BadRequestError:
            if bon.sender_id in BRAIN_CHECKER:
                await bon.respond(
                    "<triggerban> " +
                    str((await bon.get_reply_message()).sender_id)
                )
                return

        # Delete message and then tell that the command
        # is done gracefully
        await bon.delete()
        await bon.respond("`Banned!`")

        # Announce to the logging group if we done a banning
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await bon.get_reply_message()).sender_id) + " was banned.",
            )


@bot.on(events.NewMessage(outgoing=True, pattern="^.mute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.mute$"))
async def spider(spdr):
    """
    This function basically muting peeps
    """
    if not spdr.text[0].isalpha() and spdr.text[0] not in ("/", "#", "@", "!"):

        # If the targeted user is a Sudo
        if (await spdr.get_reply_message()).sender_id in BRAIN_CHECKER:
            await spdr.edit("`Mute Error! I am not supposed to mute this user`")
            return

        # Check if the function running under SQL mode
        try:
            from userbot.modules.sql_helper.spam_mute_sql import mute
        except Exception:
            await spdr.edit("`Running on Non-SQL mode!`")
            return

        # Get the targeted chat
        chat = await spdr.get_chat()
        # Check if current user is admin
        admin = chat.admin_rights
        # Check if current user is creator
        creator = chat.creator

        # If not admin and not creator, return
        if not admin and not creator:
            await spdr.edit("`You aren't an admin!`")
            return

        target = str(await spdr.get_reply_message().sender_id)
        # Else, do announce and do the mute
        mute(spdr.chat_id, target)
        await spdr.edit("`Gets a tape!`")

        # Announce that the function is done
        await spdr.delete()
        await spdr.respond("`Safely taped!`")

        # Announce to logging group
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await spdr.get_reply_message()).sender_id) +
                " was muted.",
            )


@bot.on(events.NewMessage(incoming=True, pattern="<triggerban>"))
async def triggered_ban(triggerbon):
    """
    This function is supposed to check if the banned person is a sudo
    If yes, revoke all the restricts
    """
    ban_id = int(triggerbon.text[13:])
    if triggerbon.sender_id in BRAIN_CHECKER:  # non-working module#
        rights = ChatBannedRights(
            until_date=None,
            view_messages=True,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True,
        )

        if ban_id in BRAIN_CHECKER:
            await triggerbon.edit("`Sorry Master!`")
            return

        sleep(5)
        await bot(EditBannedRequest(triggerbon.chat_id, ban_id, rights))
        await triggerbon.delete()
        await bot.send_message(triggerbon.chat_id,
                               "Job was done, Master! Gimme Cookies!")


@bot.on(events.NewMessage(outgoing=True, pattern="^.unmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.unmute$"))
async def unmoot(unmot):
    if not unmot.text[0].isalpha() and unmot.text[0] not in ("/", "#", "@", "!"):
        rights = ChatBannedRights(
            until_date=None,
            send_messages=None,
            send_media=None,
            send_stickers=None,
            send_gifs=None,
            send_games=None,
            send_inline=None,
            embed_links=None,
            )
        from userbot.modules.sql_helper.spam_mute_sql import unmute
        unmute(unmot.chat_id, str((await unmot.get_reply_message()).sender_id))
        await bot(EditBannedRequest(
            unmot.chat_id,
            unmot.sender_id,
            rights
            ))
        await unmot.edit("```Unmuted Successfully```")


@bot.on(events.NewMessage(incoming=True))
@bot.on(events.MessageEdited(incoming=True))
async def muter(moot):
    try:
        from userbot.modules.sql_helper.spam_mute_sql import is_muted
        from userbot.modules.sql_helper.gmute_sql import is_gmuted
    except:
        return
    muted = is_muted(moot.chat_id)
    gmuted = is_gmuted(moot.sender_id)
    rights = ChatBannedRights(
                until_date=None,
                send_messages=True,
                send_media=True,
                send_stickers=True,
                send_gifs=True,
                send_games=True,
                send_inline=True,
                embed_links=True,
                )
    if muted:
        for i in muted:
            if str(i.sender) == str(moot.sender_id):
                await moot.delete()
                await bot(EditBannedRequest(
                    moot.chat_id,
                    moot.sender_id,
                    rights
                    ))
    for i in gmuted:
        if i.sender == str(moot.sender_id):
            await moot.delete()


@bot.on(events.NewMessage(outgoing=True, pattern="^.ungmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.ungmute$"))
async def ungmoot(ungmoot):
    if not ungmoot.text[0].isalpha() and ungmoot.text[0] \
            not in ("/", "#", "@", "!"):
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            await ungmoot.edit('`Running on Non-SQL Mode!`')
        ungmute(str((await ungmoot.get_reply_message()).sender_id))
        await ungmoot.edit("```Ungmuted Successfully```")


@bot.on(events.NewMessage(outgoing=True, pattern="^.gmute$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.gmute$"))
async def gspider(gspdr):
    if not gspdr.text[0].isalpha() and gspdr.text[0] not in ("/", "#", "@", "!"):
        if (await gspdr.get_reply_message()).sender_id in BRAIN_CHECKER:
            await gspdr.edit("`Mute Error! Couldn't mute this user`")
            return
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except Exception as err:
            print(err)
            await gspdr.edit("`Running on Non-SQL mode!`")
            return

        gmute(str((await gspdr.get_reply_message()).sender_id))
        await gspdr.edit("`Grabs a huge, sticky duct tape!`")
        sleep(5)
        await gspdr.delete()
        await gspdr.respond("`Taped!`")

        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                str((await gspdr.get_reply_message()).sender_id)
                + " was muted.",
            )
