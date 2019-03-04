import urllib
import emoji
import aiohttp
from userbot.events import register
from telethon import events


@register(outgoing=True, pattern="^.gstfy$")
async def gangstafy_text(event):
    message = None
    split_text = event.text.split(None, 1)
    if event.reply_to_msg_id:
        rep_msg = await event.get_reply_message()
        message = rep_msg.text
    elif len(split_text) == 1:
        await client.update_message(event, "...")
        return

    elif not message:
        await client.update_message(event, "`Unsuported message`")
        return
    else:
        message = split_text[1]
    await client.update_message(event, await __gangsafy(message))

#===============FUNCTION HELPERS=================================#
async def __gangsafy(text):
    urls = ("http", "www.", "https")
    if text.startswith(urls):
        params = {"search": __remove_emojis(text)}
        return "http://www.gizoogle.net/tranzizzle.php?{}".format(urllib.parse.urlencode(params))
    params = {"translatetext": __remove_emojis(text)}
    target_url = "http://www.gizoogle.net/textilizer.php"
    async with aiohttp.ClientSession() as session:
        async with session.post(target_url, data=params) as response:
            soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', await response.text())
    soup = bs4.BeautifulSoup(soup_input, "lxml")
    giz = soup.find_all(text=True)
    giz_text = giz[39].strip("\r\n")
    return giz_text

def __remove_emojis(text):
    clean_text = text
    for char in text:
        if char in list(emoji.EMOJI_UNICODE.values()):
            clean_text = re.sub(char, "", clean_text)
    return clean_text
