from pyrogram import idle
from var import *
from alpha import Client
from alpha.__version__ import __version__, __copyright__



async def log():
    if LOG_CHNL:
       await Client.send_message(LOG_CHNL, BOT_STARTED.format(__version__, __copyright__))

Client.start()
Client.run(log())
print(BOT_STARTED.format(__version__, __copyright__))
idle()