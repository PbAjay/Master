class script(object):
    START_TXT = """ʜᴇʟᴏ {},
ᴍʏ ɴᴀᴍᴇ ɪꜱ <a href=https://t.me/{}>{}</a>, ɪ ᴄᴀɴ ᴩʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ᴀꜱ ᴀɴ ᴀᴅᴍɪɴ & ᴇɴᴊᴏʏ😍"""
    HELP_TXT = """ʜᴇʏ {}
ʜᴇʀᴇ ɪꜱ ᴍʏ ʜᴇʟᴩ ᴄᴏᴍᴍᴀɴᴅꜱ"""
    ABOUT_TXT = """✯ ᴍʏ ɴᴀᴍᴇ: {}
✯ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/AjayZ_TG>AᴊᴀʏZ TG 💚</a>
✯ ʟɪʙʀᴀʀʏ: ᴩʏʀᴏɢʀᴀᴍ
✯ ʟᴀɴɢᴜᴀɢᴇ: ᴩʏᴛʜᴏɴ 𝟹
✯ ᴅᴀᴛᴀ ʙᴀꜱᴇ: ᴍᴏɴɢᴏ ᴅʙ
✯ ʙᴏᴛ ꜱᴇʀᴠᴇʀ: ᴠᴩꜱ
✯ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜꜱ: v2.6.0"""
    SOURCE_TXT = """<b>ɴᴏᴛᴇ:</b>
ᴍᴀꜱᴛᴇʀ ɪꜱ ᴀ ᴩʀɪᴠᴀᴛᴇ ᴩʀᴏᴊᴇᴄᴛ
<a href=https://github.com/PbAjay/Master>ᴍᴀꜱᴛᴇʀ</a>

<b>ᴅᴇᴠꜱ:</b>
- <a href=https://t.me/AjayZ_TG>AᴊᴀʏZ TG 💚</a>"""
    MANUELFILTER_TXT = """<b>ʜᴇʟᴩ: ꜰɪʟᴛᴇʀꜱ</b>

- ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ғᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ EᴠᴀMᴀʀɪᴀ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ғᴏᴜɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ

ɴᴏᴛᴇ:
𝟷. ᴍᴀꜱᴛᴇʀ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
𝟸. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ғɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
𝟹. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏғ 𝟼𝟺 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:
• /filter - <code>ᴀᴅᴅ ᴀ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ғɪʟᴛᴇʀꜱ ᴏғ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪғɪᴄ ғɪʟᴛᴇʀ ɪɴ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ғɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""
    BUTTON_TXT = """<b>ʜᴇʟᴩ:</b> <b>ʙᴜᴛᴛᴏɴ</b>

- ᴍᴀꜱᴛᴇʀ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴏᴛʜ ᴜʀʟ ᴀɴᴅ ᴀʟᴇʀᴛ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴꜱ.

ɴᴏᴛᴇ:
𝟷. ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴇɴᴅ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, ꜱᴏ ᴄᴏɴᴛᴇɴᴛ ɪꜱ ᴍᴀɴᴅᴀᴛᴏʀʏ.
𝟸. ᴍᴀꜱᴛᴇʀ ꜱᴜᴘᴘᴏʀᴛꜱ ʙᴜᴛᴛᴏɴꜱ ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
𝟹. ʙᴜᴛᴛᴏɴꜱ ꜱʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀꜱᴇᴅ ᴀꜱ ᴍᴀʀᴋᴅᴏᴡɴ ғᴏʀᴍᴀᴛ

<b>ᴜʀʟ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](buttonurl:https://t.me/MasterV3Bot)</code>

<b>ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ:</b>
<code>[ʙᴜᴛᴛᴏɴ ᴛᴇxᴛ](buttonalert:ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀʟᴇʀᴛ ᴍᴇꜱꜱᴀɢᴇ)</code>"""
    AUTOFILTER_TXT = """<b>ʜᴇʟᴩ: ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ</b>

<b>ɴᴏᴛᴇ:</b>
𝟷. ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪғ ɪᴛ'ꜱ ᴘʀɪᴠᴀᴛᴇ
𝟸. ᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇꜱ ɴᴏᴛ ᴄᴏɴᴛᴀɪɴꜱ ᴄᴀᴍʀɪᴘꜱ, ᴘᴏʀɴ ᴀɴᴅ ғᴀᴋᴇ ғɪʟᴇꜱ
𝟹. ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇꜱ
ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ғɪʟᴇꜱ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ"""
    CONNECTION_TXT = """<b>ʜᴇʟᴩ: ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</b>

- ᴜꜱᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʙᴏᴛ ᴛᴏ ᴩᴍ ғᴏʀ ᴍᴀɴᴀɢɪɴɢ ғɪʟᴛᴇʀꜱ 
- ɪᴛ ʜᴇʟᴘꜱ ᴛᴏ ᴀᴠᴏɪᴅ ꜱᴘᴀᴍᴍɪɴɢ ɪɴ ɢʀᴏᴜᴘꜱ.

ɴᴏᴛᴇ:
𝟷. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ᴀ ᴄᴏɴɴᴇᴄᴛɪᴏɴ.
𝟸. ꜱᴇɴᴅ /connect ғᴏʀ ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴍᴇ ᴛᴏ ᴜʀ ᴩᴍ

ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ
• /connect - <code>ᴄᴏɴɴᴇᴄᴛ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ ᴛᴏ ʏᴏᴜʀ ᴩᴍ</code>
• /disconnect - <code>ᴅɪꜱᴄᴏɴɴᴇᴄᴛ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /connections - <code>ʟɪꜱᴛ ᴀʟʟ ʏᴏᴜʀ ᴄᴏɴɴᴇᴄᴛɪᴏɴꜱ</code>"""
    EXTRAMOD_TXT = """<b>ʜᴇʟᴩ: ᴇxᴛʀᴀ ᴍᴏᴅꜱ</b>

<b>ɴᴏᴛᴇ:</b>
ᴛʜᴇꜱᴇ ᴀʀᴇ ᴛʜᴇ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇꜱ ᴏғ ᴍᴀꜱᴛᴇʀ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /id - <code>ɢᴇᴛ ɪᴅ ᴏғ ᴀ ꜱᴘᴇᴄɪғɪᴇᴅ ᴜꜱᴇʀ</code>
• /info - <code>ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴜꜱᴇʀ</code>
• /imdb  - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ɪᴍᴅʙ ꜱᴏᴜʀᴄᴇ</code>
• /search  - <code>ɢᴇᴛ ᴛʜᴇ ғɪʟᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ғʀᴏᴍ ᴠᴀʀɪᴏᴜꜱ ꜱᴏᴜʀᴄᴇꜱ</code>"""
    ADMIN_TXT = """<b>ʜᴇʟᴩ: ᴀᴅᴍɪɴ</b>

<b>ɴᴏᴛᴇ:</b>
ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴏɴʟʏ ᴡᴏʀᴋꜱ ғᴏʀ ᴍʏ ᴀᴅᴍɪɴꜱ

ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:
• /logs - <code>ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇꜱᴄᴇɴᴛ ᴇʀʀᴏʀꜱ</code>
• /stats - <code>ᴛᴏ ɢᴇᴛ ꜱᴛᴀᴛᴜꜱ ᴏғ ғɪʟᴇꜱ ɪɴ ᴅʙ</code>
• /delete - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪғɪᴄ ғɪʟᴇ ғʀᴏᴍ ᴅʙ</code>
• /users - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏғ ᴍʏ ᴜꜱᴇʀꜱ ᴀɴᴅ ɪᴅꜱ</code>
• /chats - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏғ ᴛʜᴇ ᴍʏ ᴄʜᴀᴛꜱ ᴀɴᴅ ɪᴅꜱ </code>
• /leave  - <code>ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ</code>
• /disable  -  <code>ᴅᴏ ᴅɪꜱᴀʙʟᴇ ᴀ ᴄʜᴀᴛ</code>
• /ban  - <code>ᴛᴏ ʙᴀɴ ᴀ ᴜꜱᴇʀ</code>
• /unban  - <code>ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ</code>
• /channel - <code>ᴛᴏ ɢᴇᴛ ʟɪꜱᴛ ᴏғ ᴛᴏᴛᴀʟ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴄʜᴀɴɴᴇʟꜱ</code>
• /broadcast - <code>ᴛᴏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀꜱ</code>"""
    STATUS_TXT = """★ ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
★ ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
★ ᴅʙ𝟷 ᴜꜱᴇᴅ: <code>{}</code>
★ ᴅʙ𝟷 ꜰʀᴇᴇ: <code>{}</code>
★ ᴅʙ𝟸 ᴜꜱᴇᴅ: <code>{}</code>
★ ᴅʙ𝟸 ꜰʀᴇᴇ: <code>{}</code>"""
    LOG_TEXT_G = """#ɴᴇᴡɢʀᴏᴜᴩ
ɢʀᴏᴜᴩ = {}(<code>{}</code>)
ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀꜱ = <code>{}</code>
ᴀᴅᴅᴇᴅ ʙʏ - {}
"""
    LOG_TEXT_P = """#ɴᴇᴡᴜꜱᴇʀ
ɪᴅ - <code>{}</code>
ɴᴀᴍᴇ - {}
"""

    AI_TXT = """<b>ʜᴇʟᴩ: ᴏᴩᴇɴ ᴀɪ</b>
    
ᴏᴩᴇɴ ᴀɪ ᴄᴀɴ ᴀɴꜱᴡᴇʀ ᴍᴏꜱᴛ ᴏꜰ ʏᴏᴜʀ ǫᴜᴇʀʏ
    
<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇꜱ:</b>
• /openai - <code>[ʏᴏᴜʀ ǫᴜᴇʀʏ]</code>
    """
    
    TELE_TXT = """<b>ʜᴇʟᴩ: ᴛᴇʟᴇɢʀᴀᴩʜ</b>
     
ᴅᴏ ᴀꜱ ʏᴏᴜ ᴡɪꜱʜ ᴡɪᴛʜ graph.org ᴍᴏᴅᴜʟᴇ

</b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b> 
• /telegraph - ꜱᴇɴᴅ ᴍᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴩʟʏ ᴡɪᴛʜ ᴀ ᴩɪᴄᴛᴜʀᴇ  ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 𝟻ᴍʙ"""
    
    FONT_TXT = """<b>ʜᴇʟᴩ: ꜰᴏɴᴛ</b>
ꜰᴏɴᴛ ɪꜱ ᴀ ᴍᴏᴅᴜʟᴇ ꜰᴏʀ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴛᴇxᴛ ꜱᴛʏʟɪꜱʜ
ꜰᴏʀ ᴜꜱᴇ ᴛʜᴀᴛ ꜰᴇᴀᴛᴜʀᴇ ᴛʏᴩᴇ /font <your text> ᴛʜᴇɴ ʏᴏᴜʀ ᴛᴇxᴛ ʀᴇᴀᴅʏ"""
    
    GITHUB_TXT = """<b>ʜᴇʟᴩ: ɢɪᴛʜᴜʙ</b>
ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ʜᴇʟᴩꜱ ʏᴏᴜ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /github username - <code>ᴛʏᴩᴇ ʟɪᴋᴇ ᴛʜɪꜱ ᴛᴏ ɪɴᴅᴇɴᴛʏꜰʏ ᴛʜᴇ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ</code>"""
    
    SONG_TXT = """<b>ʜᴇʟᴩ: ꜱᴏɴɢ</b>

ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ, ꜰᴏʀ ᴛʜᴏꜱᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜꜱɪᴄ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ꜱᴏɴɢ ʙʏ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ

<b>ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b> 
• /song ꜱᴏɴɢ ɴᴀᴍᴇ - <code>ᴛʏᴩᴇ ʟɪᴋᴇ ᴛʜɪꜱ ᴀɴᴅ ꜱᴇɴᴅ ᴛᴏ ɢᴇᴛ ꜱᴏɴɢ</code>"""
    
    REPO_TXT = """<b>ʜᴇʟᴩ: ʀᴇᴩᴏ</b>
ʙʏ ᴜꜱɪɴɢ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ᴡᴏʀᴋɪɴɢ ɢɪᴛʜᴜʙ ʙᴏᴛ ʀᴇᴩᴏꜱ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /repo reponame - <code>ᴛʏᴩᴇ ʟɪᴋᴇ ᴛʜɪꜱ ᴀɴᴅ ꜱᴇɴᴅ ᴛᴏ ɢᴇᴛ ʀᴇᴩᴏ</code>"""
    
    URL_TXT = """<b>ʜᴇʟᴩ: ᴜʀʟ ꜱʜᴏʀᴛ</b>
ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴꜱ ʜᴇʟᴩꜱ ʏᴏᴜ ᴛᴏ ꜱʜᴏʀᴛ ᴀ ᴜʀʟ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>:
• /short - <code>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀᴍᴅ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ ꜱʜᴏʀᴛᴇᴅ ʟɪɴᴋ</code>"""
    
    PING_TXT = """<b>ʜᴇʟᴩ: ᴩɪɴɢ</b>
ɪᴛ ʜᴇʟᴩꜱ ʏᴏᴜ ᴛᴏ ᴋɴᴏᴡ ʙᴏᴛ ꜱᴩᴇᴇᴅ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b> 
• /ping - <code>ᴛᴏ ɢᴇᴛ ᴩɪɴɢ</code>"""
    
    RESTART_TXT = """
<b>ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...!
📅 ᴅᴀᴛᴇ : <code>{}</code>
⏰ ᴛɪᴍᴇ : <code>{}</code>
🌐 ᴛɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>
🛠️ ʙᴜɪʟᴅ ꜱᴛᴀᴛᴜs: <code>[ꜱɪɢᴍᴀ]</code>"""
    
    CREATOR_REQUIRED = """<b>ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ʙᴇ ᴛʜᴇ ɢʀᴏᴜᴩ ᴄʀᴇᴀᴛᴏʀ ᴛᴏ ᴅᴏ ᴛʜᴀᴛ</b>"""
    
    INPUT_REQUIRED = " **ᴀʀɢᴜᴍᴇɴᴛꜱ ʀᴇǫᴜɪʀᴇᴅ**"
      
    KICKED = """ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴋɪᴄᴋᴇᴅ {} ᴍᴇᴍʙᴇʀꜱ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴛʜᴇ ᴀʀɢᴜᴍᴇɴᴛꜱ ᴩʀᴏᴠɪᴅᴇᴅ"""
      
    START_KICK = """ʀᴇᴍᴏᴠᴇ ɪɴᴀᴄᴛɪᴠᴇ ᴍᴇᴍʙᴇʀꜱ ᴛʜɪꜱ ᴍᴀʏ ᴛᴀᴋᴇ ᴀ ᴡʜɪʟᴇ..."""
      
    ADMIN_REQUIRED = """<b>എന്നെ ᴀᴅᴍɪɴ ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ ʙʏᴇᴇ..ᴀᴅᴅ ᴍᴇ ᴀɢᴀɪɴ ᴡɪᴛʜ ᴀʟʟ ʀɪɢʜᴛꜱ</b>"""
      
    DKICK = """ᴋɪᴄᴋᴇᴅ {} ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛꜱ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ"""
      
    FETCHING_INFO = """<b>ᴩʟᴇᴀꜱᴇ ᴡᴀɪᴛ...</b>"""

    MULTIFEATURE_TXT = """
    
<b>#ᴄᴀʀʙᴏɴ</b>
ᴄᴀʀʙᴏɴ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇ ɪᴍᴀɢᴇ ᴀꜱ ꜱʜᴏᴡɴ ɪɴ ᴛʜᴇ ᴛᴏᴩ ᴡɪᴛʜ ʏᴏᴜʀ ᴛᴇxᴛꜱ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /carbon - <code>ꜰᴏʀ ᴜꜱɪɴɢ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴩʟʏ ᴀ ᴛᴇxᴛ ᴡɪᴛʜ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ</code>
    
    #ꜱʜᴀʀᴇ ᴛᴇxᴛ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /share - <code>ʀᴇᴩʟʏ ᴡɪᴛʜ ᴀɴʏ ᴛᴇxᴛ ᴛᴏ ꜱᴇɴᴅ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ</code>
    
    #ꜰɪʟᴇꜱᴛᴏʀᴇ

<b>ʙʏ ᴜꜱɪɴɢ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴛᴏʀᴇ ꜰɪʟᴇꜱ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴀ ᴩᴇʀᴍᴀɴᴀɴᴛ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ꜱᴀᴠᴇᴅ ꜰɪʟᴇꜱ.ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴀ ᴩᴜʙʟɪᴄ ᴄʜᴀɴɴᴇʟ ꜱᴇɴᴅ ᴛʜᴇ ꜰɪʟᴍ ʟɪɴᴋ ᴏɴʟʏ ᴏʀ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ꜰʀᴏᴍ ᴀ ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ʏᴏᴜ ᴍᴜꜱᴛ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴏɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.</b>

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /plink - <code>ʀᴇᴩʟʏ ᴛᴏ ᴀɴʏ  ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ ʟɪɴᴋ</code>
• /pbatch - <code>ᴜꜱᴇ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ʟɪɴᴋ ᴡʜɪᴛʜ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ</code>
• /batch - <code>ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ꜰᴏʀ ᴍᴜʟᴛɪᴩʟᴇ ꜰɪʟᴇꜱ</code>
    
    <b>#ʟʏʀɪᴄꜱ</b>
ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ʜᴇʟᴩꜱ ʏᴏᴜ ᴛᴏ ꜰɪɴᴅ ꜱᴏɴɢꜱ ʟʏʀɪᴄꜱ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /lyrics - <code>ʀᴇᴩʟʏ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀɴʏ ꜱᴏɴɢ ɴᴀᴍᴇ</code>

    <b>#ᴊꜱᴏɴ</b>
ʙᴏᴛ ʀᴇᴛᴜʀɴs ɪsᴏɴ ғᴏʀ ᴀʟʟ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇs ᴡɪᴛʜ /json

<b>ꜰᴇᴀᴛᴜʀᴇꜱ:</b>

ᴍᴇssᴀɢᴇ ᴇᴅɪᴛᴛɪɴɢ ᴊꜱᴏɴ
ᴩᴍ ꜱᴜᴘᴘᴏʀᴛ
ɢʀᴏᴜᴘ ꜱᴜᴘᴘᴏʀᴛ

<b>ɴᴏᴛᴇ:</b>

ᴇᴠᴇʀʏᴏɴᴇ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ , ɪғ sᴘᴀᴍɪɴɢ ʜᴀᴘᴘᴇɴs ʙᴏᴛ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʙᴀɴ ʏᴏᴜ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ """

      MU2_TXT = """

<b>#ꜱᴛɪᴄᴋᴇʀ ɪᴅ</b>
ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴍᴏᴅᴜʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ ꜱᴛɪᴄᴋᴇʀꜱ ɪᴅ 

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ: </b>  
• ʀᴇᴩʟʏ ᴛᴏ ᴀɴʏ ꜱᴛɪᴄᴋᴇʀ /stickerid

<b>#ᴡʀɪᴛᴇ</b>
ʙʏ ᴜꜱɪɴɢ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʏᴏᴜ ᴄᴀɴ ᴡʀɪᴛᴇ ʏᴏᴜʀ ᴀꜱꜱᴀɪɢɴᴍᴇɴᴛ ᴡɪᴛʜᴏᴜᴛᴛ ᴡʀɪᴛᴇɪɴɢ ɪᴛ ᴏɴ ɴᴏᴛᴇ ʙᴏᴏᴋ 

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /write - <code>ᴛᴏ ᴡʀɪᴛᴇ ᴀꜱꜱᴀɪɢɴᴍᴇɴᴛ</code>

    <b>#ᴏᴩᴇɴ ᴀɪ</b>
ᴏᴩᴇɴ ᴀɪ ᴄᴀɴ ᴀɴꜱᴡᴇʀ ᴍᴏꜱᴛ ᴏꜰ ʏᴏᴜʀ ǫᴜᴇʀʏ
    
<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇꜱ:</b>
• /openai - <code>[ʏᴏᴜʀ ǫᴜᴇʀʏ]</code>
    
    <b>#ᴛᴇʟᴇɢʀᴀᴩʜ</b>
ᴅᴏ ᴀꜱ ʏᴏᴜ ᴡɪꜱʜ ᴡɪᴛʜ graph.org ᴍᴏᴅᴜʟᴇ

</b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b> 
• /telegraph - ꜱᴇɴᴅ ᴍᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ʀᴇᴩʟʏ ᴡɪᴛʜ ᴀ ᴩɪᴄᴛᴜʀᴇ  ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ 𝟻ᴍʙ
    
    <b>#ꜰᴏɴᴛ</b>
ꜰᴏɴᴛ ɪꜱ ᴀ ᴍᴏᴅᴜʟᴇ ꜰᴏʀ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴛᴇxᴛ ꜱᴛʏʟɪꜱʜ
ꜰᴏʀ ᴜꜱᴇ ᴛʜᴀᴛ ꜰᴇᴀᴛᴜʀᴇ ᴛʏᴩᴇ /font <your text> ᴛʜᴇɴ ʏᴏᴜʀ ᴛᴇxᴛ ʀᴇᴀᴅʏ"""

    MU3_TXT = """
    
    <b>#ɢɪᴛʜᴜʙ</b>
ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ʜᴇʟᴩꜱ ʏᴏᴜ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /github username - <code>ᴛʏᴩᴇ ʟɪᴋᴇ ᴛʜɪꜱ ᴛᴏ ɪɴᴅᴇɴᴛʏꜰʏ ᴛʜᴇ ɢɪᴛʜᴜʙ ᴀᴄᴄᴏᴜɴᴛ</code>
    
    <b>#ꜱᴏɴɢ</b>
ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴍᴏᴅᴜʟᴇ, ꜰᴏʀ ᴛʜᴏꜱᴇ ᴡʜᴏ ʟᴏᴠᴇ ᴍᴜꜱɪᴄ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ꜱᴏɴɢ ʙʏ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ

<b>ᴄᴏᴍᴍᴀɴᴅ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b> 
• /song ꜱᴏɴɢ ɴᴀᴍᴇ - <code>ᴛʏᴩᴇ ʟɪᴋᴇ ᴛʜɪꜱ ᴀɴᴅ ꜱᴇɴᴅ ᴛᴏ ɢᴇᴛ ꜱᴏɴɢ</code>
    
    <b>#ʀᴇᴩᴏ</b>
ʙʏ ᴜꜱɪɴɢ ᴛʜɪꜱ ꜰᴇᴀᴛᴜʀᴇ ʏᴏᴜ ᴄᴀɴ ꜰɪɴᴅ ᴡᴏʀᴋɪɴɢ ɢɪᴛʜᴜʙ ʙᴏᴛ ʀᴇᴩᴏꜱ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /repo reponame - <code>ᴛʏᴩᴇ ʟɪᴋᴇ ᴛʜɪꜱ ᴀɴᴅ ꜱᴇɴᴅ ᴛᴏ ɢᴇᴛ ʀᴇᴩᴏ</code>
    
    <b>#ᴜʀʟ ꜱʜᴏʀᴛ</b>
ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴꜱ ʜᴇʟᴩꜱ ʏᴏᴜ ᴛᴏ ꜱʜᴏʀᴛ ᴀ ᴜʀʟ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>:
• /short - <code>ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀᴍᴅ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ɢᴇᴛ ꜱʜᴏʀᴛᴇᴅ ʟɪɴᴋ</code>
    
    <b>#ᴩɪɴɢ</b>
ɪᴛ ʜᴇʟᴩꜱ ʏᴏᴜ ᴛᴏ ᴋɴᴏᴡ ʙᴏᴛ ꜱᴩᴇᴇᴅ

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b> 
• /ping - <code>ᴛᴏ ɢᴇᴛ ᴩɪɴɢ</code>"""
