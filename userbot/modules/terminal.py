from telethon import events
from telethon.errors import FloodWaitError
from userbot import SUBPROCESS_ANIM, bot
from userbot.events import register
import time
import asyncio


@register(outgoing=True, pattern="^.term")
async def terminal(event):

    split_text = event.text.split(None, 1)

    if len(split_text) == 1:
        await event.edit(event, TERM_HELP)
        return

    cmd = split_text[1]

    await event.edit("`Connecting..`")

    start_time = time.time() + 10
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    OUTPUT = f"**Jeepeo55@MSi:**\n\n`{cmd}`\n\n**Result:**\n\n"

    if not SUBPROCESS_ANIM:
        stdout, stderr = await process.communicate()

        if len(stdout) > 4096:
            await event.reply(f"{OUTPUT}\n__Process killed:__ `Messasge too long`")
            return

        if stderr.decode():
            await event.edit(f"{OUTPUT}`{stderr.decode()}`")
            return

        await event.edit(f"{OUTPUT}`{stdout.decode()}`")
        return

    while process:
        if time.time() > start_time:
            if process:
                process.kill()
            await event.edit(f"{OUTPUT}\n__Process killed__: `Time limit reached`")
            break

        stdout = await process.stdout.readline()

        if not stdout:
            _, stderr = await process.communicate()
            if stderr.decode():
                OUTPUT += f"`{stderr.decode()}`"
                try:
                    await event.edit(event, OUTPUT)
                except Exception:
                    break
                break

        if stdout:
            OUTPUT += f"`{stdout.decode()}`"

        if len(OUTPUT) > 4096:
            if process:
                process.kill()
            await event.reply(f"{OUTPUT}\n__Process killed:__ `Messasge too long`")
            break
        try:
            await event.edit(OUTPUT)
        except FloodWaitError:
            stdout, stderr = await process.communicate()
            if stderr:
                await event.edit(f"{OUTPUT}`{stderr}`")
                break
            await event.edit(f"{OUTPUT}`{stdout}`")
            break
