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

from userbot import LOGGER, LOGGER_GROUP, bot

langi = "en"


@bot.on(events.NewMessage(outgoing=True,pattern='.imdb (.*)'))
@bot.on(events.MessageEdited(outgoing=True,pattern='.imdb (.*)'))
async def imdb(e):
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


@bot.on(events.NewMessage(pattern=".lang", outgoing=True))
@bot.on(events.MessageEdited(pattern=".lang", outgoing=True))
async def lang(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        global langi
        message = await bot.get_messages(e.chat_id)
        langi = str(message[0].message[6:])
        if LOGGER:
            await bot.send_message(
                LOGGER_GROUP, "tts language changed to **" + langi + "**"
            )
            await e.edit("tts language changed to **" + langi + "**")    


#ASCII figlet fonts--->

@bot.on(events.NewMessage(pattern='^\.figlet (.+)'))
@bot.on(events.MessageEdited(pattern='^\.figlet (.+)'))
async def figlety(e):
	l=['figlet']
	l+=e.pattern_match.group(1).split(' ')
	p='```'
	p+=subprocess.run(l, stdout=subprocess.PIPE).stdout.decode()
	p+='```'
	await e.edit(p)            			


@bot.on(events.NewMessage(outgoing=True, pattern="^Oof$"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^Oof$"))
async def lol(e):
    t = "Oof"
    for j in range(10):
        t = t[:-1] + "of"
        await e.edit(t)


@bot.on(events.NewMessage(outgoing=True, pattern="^.smk"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.smk"))
async def tr(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        textx = await e.get_reply_message()
        message=e.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message)   
        faces += " ツ"
        reply_text = message + " " + faces
        await e.edit(reply_text)

 #duplicate of test smirk 5698
@bot.on(events.NewMessage(outgoing=True, pattern="^.tr"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.tr"))
async def smrk(e):       
        if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
            textx = await e.get_reply_message()
        message=e.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message) 
        reactor = [
                "ツ",
                "ツ",
                "ツ",
        ]
        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(reactor), reply_text)
        reply_text += " " + random.choice(reactor)
        await e.edit(reply_text)