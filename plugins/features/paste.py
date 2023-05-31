import os
import re
import json
import aiohttp
import requests
from pyrogram import Client, filters

#Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

#Pastebins
async def p_paste(message, extension=None):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        return {
            "url": purl,
            "raw": f"https://pasty.lus.pm/{response['id']}/raw",
            "bin": "Pasty",
        }
    return {"error": "ᴜɴᴀʙʟᴇ ᴛᴏ ʀᴇᴀᴄʜ pasty.lus.pm"}



@Client.on_message(filters.command(["tgpaste", "pasty", "paste"]))
async def pasty(client, message):
    pablo = await message.reply_text("`ᴩʟᴇᴀꜱᴇ ᴡᴀɪᴛ...`")
    tex_t = message.text
    if ' ' in message.text:
        message_s = message.text.split(" ", 1)[1]
    elif message.reply_to_message:
        message_s = message.reply_to_message.text
    else:
        await message.reply("ꜱᴏʀʀʏ ɴᴏ ɪɴᴩᴜᴛ.ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴏʀ/paste ᴡɪᴛʜ ᴛᴇxᴛ")
    if not tex_t:
        if not message.reply_to_message:
            await pablo.edit("`ᴏɴʟʏ ᴛᴇxᴛ ᴀɴᴅ ᴅᴏᴄᴜᴍᴇɴᴛ ꜱᴜᴩᴩᴏʀᴛ`")
            return
        if not message.reply_to_message.text:
            file = await message.reply_to_message.download()
            m_list = open(file, "r").read()
            message_s = m_list
            os.remove(file)
        elif message.reply_to_message.text:
            message_s = message.reply_to_message.text

    ext = "py"
    x = await p_paste(message_s, ext)
    p_link = x["url"]
    p_raw = x["raw"]

    pasted = f"**ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴩᴀꜱᴛᴇ ᴛᴏ ᴩᴀꜱᴛʏ**\n\n**ʟɪɴᴋ:** • [ᴄʟɪᴄᴋ ʜᴇʀᴇ]({p_link})\n\n**ʀᴀᴡ ʟɪɴᴋ:** • [ᴄʟɪᴄᴋ ʜᴇʀᴇ]({p_raw})"
    await pablo.edit(pasted, disable_web_page_preview=True)
