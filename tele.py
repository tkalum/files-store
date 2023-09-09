from telethon import TelegramClient, events, Button
from alpha.helpers.db import *

API_ID = 19611094
API_HASH = "c5198b0dab5cdd8e0eaaf3e0c742fbd3"
BOT_TOKEN = '5568470888:AAHXD5aNcriio13kZf7IUap5XlnlLqZ1vNg'

app = TelegramClient("SimpleBot", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@app.on(events.NewMessage(pattern="/new"))
async def start(event):
    s = await event.get_sender()
    async with app.conversation(event.chat_id) as x:
        e = await event.get_chat()
        s = await event.get_sender()
        await x.send_message("Please Enter name\nIf you want cancel this operation use /cancel command")
        name = await x.get_response() 
        if not name.message=="/cancel":
            await x.send_message("Enter Post")
            post = await x.get_response()
            postid = await app.send_message(-1001602351892, post)
            Addfiles(name.message, postid.id)
            me = await app.get_me()
            Btn = Button.url('Download', f'http://t.me/{me.username}?start={name.message}')
            await x.send_message(post, buttons=[Btn])
        else:
            await x.send_message("canceled")

@app.on(events.NewMessage(pattern="/add"))
async def start(event):
    if not event.reply_to:
        async with app.conversation(event.chat_id) as x:
            await x.send_message("Please enter the name you want to use")
            name = await x.get_response()
            if not name.message == "/cancel":
                name_message = name.message

                await x.send_message("Okay, now enter the file you want to add")
                file = await x.get_response()

                if file.media:
                    postid = await app.forward_messages(-1001602351892, file, silent=True)

                    # Fetch the existing dictionary associated with the name
                    data1 = Getfiles().get(name_message, {})

                    # Remove unwanted keys (if present)
                    data1.pop("Id", None)
                    data1.pop("Title", None)

                    # Update the existing dictionary with the new data
                    data1[postid.id] = {"id": postid.id}

                    # Update the Files database with the updated data
                    Files.child(name_message).set(data1)

                    await x.send_message(f'Added file to "{name_message}" with ID {postid.id}')
                else:
                    await x.send_message("Please add files")
            else:
                await x.send_message("Canceled")



    





print("Bot is now running. Press Ctrl+C to stop.")
app.run_until_disconnected()
