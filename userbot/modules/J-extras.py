import bs4
import requests
import os
import re
import subprocess
import time
import random
from datetime import datetime, timedelta

import urbandict
import wikipedia
from google_images_download import google_images_download
from googletrans import Translator
from gtts import gTTS
from telethon import TelegramClient, events
from pyfiglet import Figlet

from userbot import LOGGER, LOGGER_GROUP
from userbot.events import register

langi = "en"

#kanged from Blank-x ;---;
@register(outgoing=True, pattern="^.imdb (.*)")
async def imdb(e):
 try:
    movie_name = e.pattern_match.group(1)
    remove_space = movie_name.split(' ')
    final_name = '+'.join(remove_space)
    page = requests.get("https://www.imdb.com/find?ref_=nv_sr_fn&q="+final_name+"&s=all")
    lnk = str(page.status_code)
    soup = bs4.BeautifulSoup(page.content,'lxml')
    odds = soup.findAll("tr","odd")
    mov_title = odds[0].findNext('td').findNext('td').text
    mov_link = "http://www.imdb.com/"+odds[0].findNext('td').findNext('td').a['href']
    page1 = requests.get(mov_link)
    soup = bs4.BeautifulSoup(page1.content,'lxml')
    if soup.find('div','poster'):
    	poster = soup.find('div','poster').img['src']
    else:
    	poster = ''
    if soup.find('div','title_wrapper'):
    	pg = soup.find('div','title_wrapper').findNext('div').text
    	mov_details = re.sub(r'\s+',' ',pg)
    else:
    	mov_details = ''
    credits = soup.findAll('div', 'credit_summary_item')
    if len(credits)==1:
    	director = credits[0].a.text
    	writer = 'Not available'
    	stars = 'Not available'
    elif len(credits)>2:
    	director = credits[0].a.text
    	writer = credits[1].a.text
    	actors = []
    	for x in credits[2].findAll('a'):
    		actors.append(x.text)
    	actors.pop()
    	stars = actors[0]+','+actors[1]+','+actors[2]
    else:
    	director = credits[0].a.text
    	writer = 'Not available'
    	actors = []
    	for x in credits[1].findAll('a'):
    		actors.append(x.text)
    	actors.pop()
    	stars = actors[0]+','+actors[1]+','+actors[2]
    if soup.find('div', "inline canwrap"):
    	story_line = soup.find('div', "inline canwrap").findAll('p')[0].text
    else:
    	story_line = 'Not available'
    info = soup.findAll('div', "txt-block")
    if info:
    	mov_country = []
    	mov_language = []
    	for node in info:
    		a = node.findAll('a')
    		for i in a:
    			if "country_of_origin" in i['href']:
    				mov_country.append(i.text)
    			elif "primary_language" in i['href']:
    				mov_language.append(i.text)
    if soup.findAll('div',"ratingValue"):
    	for r in soup.findAll('div',"ratingValue"):
    		mov_rating = r.strong['title']
    else:
    	mov_rating = 'Not available'
    await e.edit('<a href='+poster+'>&#8203;</a>'
    			'<b>Title : </b><code>'+mov_title+
    			'</code>\n<code>'+mov_details+
    			'</code>\n<b>Rating : </b><code>'+mov_rating+
    			'</code>\n<b>Country : </b><code>'+mov_country[0]+
    			'</code>\n<b>Language : </b><code>'+mov_language[0]+
    			'</code>\n<b>Director : </b><code>'+director+
    			'</code>\n<b>Writer : </b><code>'+writer+
    			'</code>\n<b>Stars : </b><code>'+stars+
    			'</code>\n<b>IMDB Url : </b>'+mov_link+
    			'\n<b>Story Line : </b>'+story_line,
    			link_preview = True , parse_mode = 'HTML'
    			)
 except IndexError:
     await e.edit("Plox enter **Valid movie name** kthx")


@register(outgoing=True, pattern="^Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(10):
        t = t[:-1] + "of"
        await e.edit(t)


#∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆ Below module is completely copyrighted to Jepeeo ∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆

@register(outgoing=True, pattern="^.smk (.*)")
async def smrk(smk):
        if not smk.text[0].isalpha() and smk.text[0] not in ("/", "#", "@", "!"):
            textx = await smk.get_reply_message()
            message = smk.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message)
        smirk = " ツ"
        reply_text = message + smirk
        await smk.edit(reply_text)
        
# =======================================================================================

@register(outgoing=True, pattern="^.repeat (.*) (.*)")
async def repeat(rep):
    if not rep.text[0].isalpha() and rep.text[0] not in ("/", "#", "@", "!"):
        replyCount = int(rep.pattern_match.group(1))
        toBeRepeated = rep.pattern_match.group(2)

        replyText = toBeRepeated

        for i in range(0, replyCount-1):
            replyText += toBeRepeated[-1:]

        await rep.edit(replyText)


@register(outgoing=True, pattern="^.lfy",)
async def let_me_google_that_for_you(lmgtfy_q):
    if not lmgtfy_q.text[0].isalpha() and lmgtfy_q.text[0] not in ("/", "#", "@", "!"):
        textx = await lmgtfy_q.get_reply_message()
        query = lmgtfy_q.text
        if query[8:]:
            query = str(query[8:])
        elif textx:
            query = str(textx.message)
        reply_text = 'http://lmgtfy.com/?s=g&iie=1&q=' + query.replace(" ", "+")
        await lmgtfy_q.edit(reply_text)
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP,
                "LMGTFY query " + query + " was executed successfully",
            )
