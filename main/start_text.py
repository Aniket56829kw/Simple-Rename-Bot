from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="This is personal use bot 🙏. Do you want your own bot? 👇 Click the source code to deploy"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🤖 SOURCE CODE", url="https://github.com/MrMKN/Simple-Rename-Bot")
        ],[
        InlineKeyboardButton("🖥️ How To Deploy", url="https://youtu.be/oc847WvOUaI")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"Hᴀɪ  {msg.from_user.mention} I Aᴍ Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ & Cᴀᴘᴛɪᴏɴ Sᴜᴘᴘᴏʀᴛ.
Aɴᴅ Rᴇɴᴀᴍᴇ Wɪᴛʜᴏᴜᴛ Dᴏᴡɴʟᴏᴀᴅ 💯 Fᴜʟʟʏ Wᴏʀᴋ Oɴ Tɢ Dᴄ Sᴏ Rᴇɴᴀᴍɪɴɢ
Sᴘᴇᴇᴅ Is Dᴇᴘᴇɴᴅɪɴɢ Oɴ Yᴏᴜʀ Fɪʟᴇ Dᴄ_Iᴅ 

Pʟᴇᴀsᴇ Sʜᴀʀᴇ Tʜɪs Bᴏᴛ Tᴏ Yᴏᴜʀ Fʀɪᴇɴᴅs 💝.
.\nthis bot is made by <b><a href=https://github.com/MrMKN>MrMKN</a></b>"                                     
    button= [[
        InlineKeyboardButton("🤖 Bot Updates", url="https://t.me/AJ_TVSHOWS")
        ],[
        InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        InlineKeyboardButton("📡 About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "just send a file and /rename <new name> with replayed your file\n\n"
    txt += "send photo to set thumbnail automatic \n"
    txt += "/view to see your thumbnail \n"
    txt += "/del to delete your thumbnail"
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/Mo_Tech_YT>MoTech</a> & <a href=https://t.me/venombotupdates>MhdRzn</a>"  
    Source="<a href=https://github.com/MrMKN/Simple-Rename-Bot>Click Here</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://github.com/MrMKN>MrMKN</a>\nBot Updates: <a href=https://t.me/mkn_bots_updates>Mᴋɴ Bᴏᴛᴢ™</a>\nMy Master's: {Master}\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🚫 Close", callback_data="del"),
        InlineKeyboardButton("⬅️ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


