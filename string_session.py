# Note this only for this repo with latest
# First replace api id and hash with yours
# Then run this python file locally command "python -m string_session.py"
# Then login your TG account
# You will get random numbers and letters(string) , Ending with '=' 
# Now copy that 
# In heroku config-vars :-
# In column 1 enter 'STRING_SESSION' and in column 2 paste random letters n numbers (string) there
# Now u need not need userbot.session

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(StringSession(), "your-api-id", "your-api-hash") as client:
    print(client.session.save())

