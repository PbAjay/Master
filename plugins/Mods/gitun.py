import aiohttp
from pyrogram import Client, filters


mod_name = "Github"


@Client.on_message(filters.private & filters.command("github"))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("ᴡʀᴏɴɢ ꜱᴀɴᴛᴇx 🚫\nᴇxᴀᴍᴩʟᴇ:\n/github Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                company = result["company"]
                bio = result["bio"]
                created_at = result["created_at"]
                avatar_url = result["avatar_url"]
                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                caption = f"""<b>Info Of {name}</b>
<b>👨‍💼 ᴜsᴇʀɴᴀᴍᴇ:</b> <code>{username}</code>
<b>✍️ ʙɪᴏ:</b> <code>{bio}</code>
<b>🔗 ᴘʀᴏғɪʟᴇ ʟɪɴᴋ:</b> <code>[Here]({url})</code>
<b>🏢 ᴄᴏᴍᴘᴀɴʏ:</b> <code>{company}</code>
<b>📒 ᴄʀᴇᴀᴛᴇᴅ ᴏɴ:</b> <code>{created_at}</code>
<b>⛵️ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs:</b> <code>{repositories}</code>
<b>🧖 ʙʟᴏɢ:</b> <code>{blog}</code>
<b>📍 ʟᴏᴄᴀᴛɪᴏɴ:</b> <code>{location}</code>
<b>➡️ ғᴏʟʟᴏᴡᴇʀs:</b> <code>{followers}</code>
<b>⬅️ ғᴏʟʟᴏᴡɪɴɢ:</b> <code>{following}</code>

<b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ: @MasterV3Bot</b>"""
            except Exception as e:
                print(str(e))
    await message.reply_photo(photo=avatar_url, caption=caption)
