from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"ᴄᴜʀʀᴇɴᴛʟʏ ᴏɴʟʏ sᴜᴘᴘᴏʀᴛs ʏᴏᴜᴛᴜʙᴇ sɪɴɢʟᴇ ᴠɪᴅᴇᴏs (ᴍᴇᴀɴs ɴᴏᴛ ғᴏʀ ᴘʟᴀʏʟɪsᴛs) sᴏ,ᴊᴜsᴛ sᴇɴᴅ ʏᴏᴜᴛᴜʙʀ ᴜʀʟ [✨](https://telegra.ph/file/7791e85fa2aea71ec31c7.jpg)"
    await message.reply_text(helptxt)
