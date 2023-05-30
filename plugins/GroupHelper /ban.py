from pyrogram import Client, filters
from plugins.helper.admin_check import admin_check
from plugins.helper.extract import extract_time, extract_user                               


@Client.on_message(filters.command("ban"))
async def ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return 
    user_id, user_first_name = extract_user(message)
    try:
        await message.chat.ban_member(user_id=user_id)
    except Exception as error:
        await message.reply_text(str(error))                    
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(f"ꜱᴏᴍᴇᴏɴᴇ ᴇʟꜱᴇ ɪꜱ ᴅᴜꜱᴛɪɢ ᴏꜰꜰ..! \n{user_first_name} \nɪꜱ ꜰᴏʀʙɪᴅᴅᴇɴ.")                              
        else:
            await message.reply_text(f"ꜱᴏᴍᴇᴏɴᴇ ᴇʟꜱᴇ ɪꜱ ᴅᴜꜱᴛɪɢ ᴏꜰꜰ..! \n<a href='tg://user?id={user_id}'>{user_first_name}</a> Is forbidden")                      
            

@Client.on_message(filters.command("tban"))
async def temp_ban_user(_, message):
    is_admin = await admin_check(message)
    if not is_admin:
        return
    if not len(message.command) > 1:
        return
    user_id, user_first_name = extract_user(message)
    until_date_val = extract_time(message.command[1])
    if until_date_val is None:
        return await message.reply_text(text=f"ɪɴᴠᴀʟɪᴅ ᴛɪᴍᴇ ᴛʏᴩᴇ ꜱᴩᴇᴄɪꜰɪᴇᴅ. \nᴇxᴩᴇᴛᴇᴅ m, h, ᴏʀ d, ɢᴏᴛ ɪᴛ: {message.command[1][-1]}")   
    try:
        await message.chat.ban_member(user_id=user_id, until_date=until_date_val)            
    except Exception as error:
        await message.reply_text(str(error))
    else:
        if str(user_id).lower().startswith("@"):
            await message.reply_text(f"ꜱᴏᴍᴇᴏɴᴇ ᴇʟꜱᴇ ɪꜱ ᴅᴜꜱᴛɪɢ ᴏꜰꜰ..!\n{user_first_name}\nʙᴀɴɴᴇᴅ ꜰᴏʀ {message.command[1]}!")
        else:
            await message.reply_text(f"ꜱᴏᴍᴇᴏɴᴇ ᴇʟꜱᴇ ɪꜱ ᴅᴜꜱᴛɪɢ ᴏꜰꜰ..!\n<a href='tg://user?id={user_id}'>ʟᴀᴠᴀɴᴇ</a>\n ʙᴀɴɴᴇᴅ ꜰᴏʀ{message.command[1]}!")
                
