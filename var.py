import os
from telethon import Button
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from alpha import __version__


# Main Details
API_ID = 19611094
API_HASH = "c5198b0dab5cdd8e0eaaf3e0c742fbd3"
#BOT_TOKEN = '5382719743:AAGkHzQWnX98N1Gp3SrEmI4yMllg_hQg6-4'
BOT_TOKEN = '5568470888:AAHXD5aNcriio13kZf7IUap5XlnlLqZ1vNg'
LOG_CHNL = -620013709

BOT_STARTED = '''
`
╭━━━┳╮╱╱╱╭╮
┃╭━╮┃┃╱╱╱┃┃
┃┃╱┃┃┃╭━━┫╰━┳━━╮
┃╰━╯┃┃┃╭╮┃╭╮┃╭╮┃
┃╭━╮┃╰┫╰╯┃┃┃┃╭╮┃
╰╯╱╰┻━┫╭━┻╯╰┻╯╰╯
╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╰╯`
{}
Powered By Pyrogram
Using Firebase as a Database
Developed By Team Alpha  

{}
'''

NEW_USER_TEXT = """#new_user 💥
🌴 UsᴇʀNᴀᴍᴇ : @{}
🌴 Permenet Link : {}
🌴 ID : {}
🌴 Aʟʟ Usᴇʀs : {}
"""

START_TEXT = """Hi {} [👋](https://telegra.ph/file/b0d47ccbff3d26f59678f.jpg)

I am {}, an  Advanced Games Setup Finder Bot For Finding Games.

Powered By [𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』](https://t.me/AlphaTm_Botz)


"""


ERROR_CRASH_TEXT = """🌷 Bot Crashed 🍇

To User ⚡️ {}
In Chat ⚡️ `{}`
Error Log 🌴
`{}`
"""

HELP_TEXT = """**Help Menu**

the format should be in this arrangement

`@{} @username your whisper`

✘ example :-
`@{} @UnknownB_o_y hello`

"""
ABOUT_TEXT = """hello {},

I am [{}](https://t.me/{}). I can Provide Some Games Setups.

• creator : [Team 𝙰𝙻𝙿𝙷𝙰 么](https://t.me/c/1662964583/10)
• Language : [python](https://www.python.org/)
• Database :  [Firebase](https://console.firebase.google.com/)
• Server : [Okteto](https://cloud.okteto.com)

Powered by [𝙰𝙻𝙿𝙷𝙰 么 ™ Bots 『🇱🇰』](https://t.me/AlphaTm_Botz)

"""

USER_NOT="""🚫 Access Denied
hey {} ,
you must join [my channel](https://t.me/AlphaTm_Botz).
so ,please join and try again 
"""


START_KEY = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🌴 Help", callback_data="help"),
            InlineKeyboardButton("🌷 About", callback_data="about"),
        ],
    ]
)

HELP_KEY = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("send a Example", switch_inline_query="@UnknownB_o_y hello"),
        ],
        [
            InlineKeyboardButton("« Back", callback_data="home"),
        ],
    ]
)


ABOUT_KEY = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🌴 Help", callback_data="help"),
            InlineKeyboardButton("🏡 Home", callback_data="home"),
        ],
        [
            InlineKeyboardButton("✖️ close", callback_data="close"),
        ],
    ]
)

print("var working.....")