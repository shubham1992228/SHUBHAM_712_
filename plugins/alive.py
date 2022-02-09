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


━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [

                 [

                    InlineKeyboardButton(text="Assistant", url="https://t.me/klm_plauer"),

                    InlineKeyboardButton(text="Network", url="https://t.me/PHOENIX_EMPIRE"),

                 ],

                 [

                    InlineKeyboardButton(text="Support", url="https://t.me/CFC_BOT_SUPPORT"),

                    InlineKeyboardButton(text="Updates", url="https://t.me/CFC_BOTS"),

                 ],
                [

        InlineKeyboardButton(

            text="➗ Add Siesta To Your Group ➗", url="t.me/kiraxmuiscbot?startgroup=new"),

    ],
                ),
    
    
@Client.on_message(commandpro(["/start", "/alive", "aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💞", url=f"https://t.me/cfc_bot_support")
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
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://github.com/mradityaxd/adityaplayer")
                ]
            ]
        ),
    )
