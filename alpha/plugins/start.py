from pyrogram import Client , filters
from var import *
from alpha.helpers.db import *
from alpha.helpers.funcs import *
from alpha import __version__ as version
from alpha import __copyright__ as cr

@Client.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    try:
        all_users = GetUsers()
        if str(update.from_user.id) not in all_users:
            AddUser(update.from_user.id, update.from_user.username)
            all_users = GetUsers()
            await bot.send_message(LOG_CHNL, NEW_USER_TEXT.format(update.from_user.username, update.from_user.mention ,update.from_user.id, len(all_users)))
        if len(update.text.split()) > 1:
            text=update.text.split()[1]
            files = Getfiles()[text]
            for key, value in files.items():
                print(value['id'])
                #message = await bot.get_messages(-1001602351892, )
                await bot.copy_message(update.chat.id, -1001602351892,value['id'])
            
        else:
            await update.reply_text(
                START_TEXT.format(update.from_user.mention ,version ),
                reply_markup=START_KEY
            )
    except BaseException as e:
        print(e)
        await bot.send_message(LOG_CHNL, ERROR_CRASH_TEXT.format(update.from_user.mention ,
        update.chat.id,
        e))