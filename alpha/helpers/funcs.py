import enchant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from var import *
from alpha.helpers.db import *


CHANNEL_LINK = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('channel', url='https://t.me/AlphaTm_Botz'),
        InlineKeyboardButton('support group',url='https://t.me/AlphaTm_Botz_chat' )],
        
        [InlineKeyboardButton('Refresh', callback_data='ref')
        ]]
    ) 



force_channel='AlphaTm_Botz'


async def Fsub(bot, update):
        all_users = GetUsers()
        if str(update.from_user.id) not in all_users:
            AddUser(update.from_user.id, update.from_user.username)
            all_users = GetUsers()
            await bot.send_message(LOG_CHNL, NEW_USER_TEXT.format(update.from_user.username, update.from_user.mention ,update.from_user.id, len(all_users)))
        try:
            await bot.get_chat_member(force_channel, update.from_user.id)
        except UserNotParticipant:
            return await bot.send_message(update.from_user.id,
            text=USER_NOT.format(update.from_user.mention),
            reply_markup=CHANNEL_LINK,
            disable_web_page_preview=True) 



def get_replied_file_details(message):
    if message.reply_to_message and message.reply_to_message.document:
            # Get the Document object of the replied file
            document = message.reply_to_message.document

            # Retrieve the file details
            file_size = document.file_size
            duration = document.duration
            file_name = document.file_name
            file_id = document.file_id
            caption = message.caption

            # Return the file details
            return file_size, duration, file_name, file_id
        
def replace_invalid_characters(text):
    invalid_characters = ['$','#[',']','/','.','_']
    replacement_characters = [' ', ' ' , ' ', ' ', ' ' ,' ',' ']
    
    for i in range(len(invalid_characters)):
        text = text.replace(invalid_characters[i], replacement_characters[i])
    
    return text



def suggest_similar_word(user_input):
    english_dict = enchant.Dict("en_US")
    if english_dict.check(user_input):
        return 
    suggestions = english_dict.suggest(user_input)
    if suggestions:
        suggestion = suggestions[0]  
        reply = f"Did you mean '`{suggestion}`'?"
    else:
        reply = False
        

    return reply

def searchMname(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                result = True
            else:
                result = False
    return result