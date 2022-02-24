import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/86ce564ca1226ae15a232.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴀᴅɪᴛʏᴀ ʜᴀʟᴅᴇʀ](https://t.me/adityahalder)
┣★ ᴜᴘᴅᴀᴛᴇs : [ᴀᴅɪᴛʏᴀ sᴇʀᴠᴇʀ](https://t.me/adityaserver)
┣★ sᴜᴘᴘᴏʀᴛ : [ᴀᴅɪᴛʏᴀ ᴅɪsᴄᴜs](https://t.me/adityadiscus)
┣★ sᴏᴜʀᴄᴇ › : [ɢᴇᴛ ʀᴇᴘᴏ ʜᴇʀᴇ](https://github.com/mradityaxd/adityaplayer)
┗━━━━━━━━━━━━━━━━━┛

🤔🙄𝗜𝗳 𝘂 𝗵𝗮𝘃𝗲 𝗮𝗻𝘆 𝗾𝘂𝗲𝘀𝘁𝗶𝗼𝗻 𝘁𝗵𝗲𝗻
𝗰𝗼𝗻𝘁𝗮𝗰𝘁 𝘁𝗼 [𝗰𝗳𝗰 𝗯𝗼𝘁 𝘀𝘂𝗽𝗽𝗼𝗿𝘁](https://t.me/cfc_bot_support) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴊᴏɪɴ ʜᴇʀᴇ ғᴏʀ ᴜᴘᴅᴀᴛᴇs ❱ ➕", url=f"https://t.me/cfc_bots")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 𝗝𝗼𝗶𝗻 𝗼𝘂𝗿 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗴𝗿𝗽❣️", url=f"https://t.me/cfc_bot_support")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥𝗰𝗹𝗶𝗰𝗸 𝗵𝗲𝗿𝗲 𝘁𝗼 𝗴𝗲𝘁 𝗼𝗽 𝗿𝗲𝗽𝗼", url=f"https://github.com/Kiraxophunter/kiraxmuisc")
                ]
            ]
        ),
    )
