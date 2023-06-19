from pyrogram import Client, filters
import openai



@Client.on_message(filters.command('openai'))
async def openai_ask(client, message):
    if len(message.command) == 1:
       return await message.reply_text("ɢɪᴠᴇ ᴀɴ ɪɴᴩᴜᴛ")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)
    
async def ai(query):
    openai.api_key = ""
    response = openai.Completion.create(engine="text-davinci-003", prompt=query, max_tokens=100, n=1, stop=None, temperature=0.9, timeout=5)
    return response.choices[0].text.strip()
     
async def ask_ai(client, m, message):
    try:
        question = message.text.split(" ", 1)[1]
        # Generate response using OpenAI API
        response = await ai(question)
        # Send response back to user
        await m.edit(f"ʀᴇᴩʟʏ ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ \n\n<code>{response}</code>")
    except Exception as e:
        # Handle other errors
        error_message = f"ᴀɴ ᴇʀʀᴏʀ ᴏᴄᴄᴜʀᴇᴅ: {e}"
        await m.edit(error_message)
