from pyrogram import filters, Client
from var import *
from alpha.helpers.db import *
from alpha import __version__ as version
from alpha.helpers.funcs import *

@Client.on_callback_query()
async def callback(bot, query):
        B = await  bot.get_me()
        if query.data == 'help':
            await query.message.edit_text(HELP_TEXT, reply_markup=HELP_KEY)
        elif query.data == 'home':
            await query.message.edit_text(START_TEXT.format(query.from_user.mention , version), reply_markup=START_KEY)
        elif query.data == 'about':
            await query.message.edit_text(ABOUT_TEXT.format(query.from_user.mention, B.first_name, B.username), reply_markup=ABOUT_KEY, disable_web_page_preview=True)
        elif query.data == 'close':
            await query.message.delete()
        elif query.data == "ref":
            await update.answer('♻️Refreshing......')
            await update.message.delete()
            if await Fsub( bot,update):
                return
            await bot.send_message(update.from_user.id ,'Okay ,Now you can use this bot')
            await bot.send_message(query.from_user.id ,START_TEXT.format(update.from_user.mention),
                                reply_markup=START_BUTTON  )