import aiohttp
from pyrogram import Client
from var import *
import alpha.__version__
from alpha.__version__ import __copyright__ as cr
from telethon.sync import TelegramClient, events

__version__ = __version__.__version__
__copyright__ = cr

plugins = dict(root="alpha/plugins")

Client = Client("Alpha-Pyrogram", bot_token=BOT_TOKEN,
             api_hash=API_HASH, api_id=API_ID,
             plugins=plugins)

