from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ 𝗪ᴇʟᴄᴏᴍᴇ ᴛᴏ 𝗧ᴇᴀᴍ 𝗣ᴜʀᴠɪ 𝗥ᴇᴘᴏs ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @Tait3nX ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Aᴅᴅ ᴍᴇ Bᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("Hᴇʟᴘ", url="https://t.me/TaitanXBot"),
          InlineKeyboardButton("Tᴀɪᴛᴀɴ", url="https://t.me/TaitanSupportGroup"),
          ],
               [
                InlineKeyboardButton("Tᴀɪᴛᴀɴ Oғғɪᴄᴇ", url=f"https://t.me/TaitanSupportGroup"),
],
[
InlineKeyboardButton("Uᴘᴅᴀᴛᴇᴅ", url=f"https://t.me/TaitanXBot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/54cd69e8028ecdeda7de7-54f195bcfea39e2a16.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )