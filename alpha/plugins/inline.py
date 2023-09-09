from pyrogram.types import InlineQueryResultCachedDocument, InlineQueryResultArticle, InputTextMessageContent
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from alpha.helpers.db import *
from alpha.helpers.funcs import *

@Client.on_inline_query()
async def answer(client, inline_query):
        B = await  client.get_me() 
        query = inline_query.query.lower()
        q_id = inline_query.id
        results = []

        data = GetMvs()  # Retrieve data from the database

        count = 0  # Counter for limiting the number of results
        for key, val in data.items():
            movie_title = replace_invalid_characters(val.get("Title", ""))
            nm = movie_title.lower()
            if query in nm:
                movie_title = val.get("Title", "")
                kb = int(val.get("Size", ""))
                inkb = kb / 1048576
                movie_size = "{:.2f}".format(inkb)
                movie_caption = val.get("Caption", "")
                file_id = val.get("FileId", "")
                caption = f"Name: `{movie_title}`\nSize: `{movie_size} MB`\nCaption: `{movie_caption}`"
                url=f"https://t.me/{B.username}?start={key}"     
                result = InlineQueryResultCachedDocument(
                    title=movie_title,
                    document_file_id=file_id,
                    description="",
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup([
                        [              
                            InlineKeyboardButton('Inline Here', switch_inline_query_current_chat=""),
                            InlineKeyboardButton('Inline Another Chat', switch_inline_query=""),
                        ],
                        [ 
                            InlineKeyboardButton('Shareable Link 🔗', url=url),        
                            InlineKeyboardButton("Share Link",url=f'https://t.me/share/url?url={url}')            
                        ],
                        [
                            InlineKeyboardButton('🌝 Share Us 🌝', switch_inline_query="bshare"),
                        ],
                        [
                            InlineKeyboardButton("Team ┊𝙰𝙻𝙿𝙷𝙰 么", url="https://t.me/+jrqciS7XvKNhODc1")
                        ]
                    ])
                )

                results.append(result)
                count += 1

                if count == 30:  # Limit the number of results to 10
                    break
        switch_pm_text = 'Newest Updates'
        if count == 0:  # No results found
            suggestion = suggest_similar_word(query)
            switch_pm_text = 'No results found.'
            if suggestion:
                no_results_content = InputTextMessageContent(suggestion)
                no_results_result = InlineQueryResultArticle(
                    title=suggestion,
                    input_message_content=no_results_content
                ) 
            else:    
                no_results_content = InputTextMessageContent("No results found.")
                no_results_result = InlineQueryResultArticle(
                    title="No Results",
                    input_message_content=no_results_content
                )
            results.append(no_results_result)

        await client.answer_inline_query(
            q_id,
            results,
            switch_pm_text=switch_pm_text,
            switch_pm_parameter="inlinest",
            cache_time=0
        )