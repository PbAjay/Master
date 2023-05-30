import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["share_text", "share", "sharetext",]))
async def share_text(client, message):
    reply = message.reply_to_message
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    input_split = message.text.split(None, 1)
    if len(input_split) == 2:
        input_text = input_split[1]
    elif reply and (reply.text or reply.caption):
        input_text = reply.text or reply.caption
    else:
        await message.reply_text(
            text=f"**ɴᴏᴛɪᴄᴇ:**\n\n1. ʀᴇᴩʟʏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇꜱ.\n2. ɴᴏ ᴍᴇᴅɪᴀ ꜱᴜᴩᴩᴏʀᴛ**",                
            reply_to_message_id=reply_id,               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ᴄʀᴇᴀᴛᴏʀ", url=f"https://t.me/AjayZ_TG")]])
            )                                                   
        return
    await message.reply_text(
        text=f"**ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ꜱʜᴀʀᴇɪɴɢ ᴛᴇxᴛ👇**\n\nhttps://t.me/share/url?url=" + quote(input_text),
        reply_to_message_id=reply_id,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("ꜱʜᴀʀᴇ", url=f"https://t.me/share/url?url={quote(input_text)}")]])       
    )
