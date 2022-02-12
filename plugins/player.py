# Aditya Halder // @AdityaHalder

import os
import aiofiles
import aiohttp
import ffmpeg
import requests
from os import path
from asyncio.queues import QueueEmpty
from typing import Callable
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from modules.cache.admins import set
from modules.clientbot import clientbot, queues
from modules.clientbot.clientbot import client as USER
from modules.helpers.admins import get_administrators
from youtube_search import YoutubeSearch
from modules import converter
from modules.downloaders import youtube
from modules.config import DURATION_LIMIT, que, SUDO_USERS
from modules.cache.admins import admins as a
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from modules.helpers.decorators import errors, authorized_users_only
from modules.helpers.errors import DurationLimitError
from modules.helpers.gets import get_url, get_file_name
from PIL import Image, ImageFont, ImageDraw
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputStream
from pytgcalls.types.input_stream import InputAudioStream

# plus
chat_id = None
useer = "NaN"


def transcode(filename):
    ffmpeg.input(filename).output(
        "input.raw", format="s16le", acodec="pcm_s16le", ac=2, ar="48k"
    ).overwrite_output().run()
    os.remove(filename)


# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    return image.resize((newWidth, newHeight))


async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("resource/thumbnail.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resource/font.otf", 32)
    draw.text((190, 550), f"Title: {title[:50]} ...", (255, 255, 255), font=font)
    draw.text((190, 590), f"Duration: {duration}", (255, 255, 255), font=font)
    draw.text((190, 630), f"Views: {views}", (255, 255, 255), font=font)
    draw.text(
        (190, 670),
        f"Powered By: PHOENIX EMPIRE (@PHOENIX_EMPIRE)",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")


@Client.on_message(
    commandpro(["/play", "/yt", "/ytp", "play", "yt", "ytp", "@", "#"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer
    
    lel = await message.reply("**🔎 𝕾𝖊𝖆𝖗𝖈𝖍𝖎𝖓𝖌...**")

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "**💥 💥 𝗙𝗶𝗿𝘀𝘁 𝗺𝗮𝗸𝗲 𝗺𝗲 𝗮𝗱𝗺𝗶𝗻 𝘁𝗼 𝗿𝗼𝗰𝗸 𝗼𝗻 𝘃𝗰  😎🤘🤟 ...**")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "** 😎 𝗜 𝗮𝗺 𝗿𝗲𝗱𝘆 𝘁𝗼 𝗿𝗼𝗰𝗸 𝗼𝗻 𝘃𝗰 🤟🤘❣️💥 ...**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"**𝗣𝗹𝗲𝗮𝘀𝗲 🥺 𝗮𝗱𝗱 @klm_player 𝗺𝗮𝗻𝘂𝘃𝗮𝗹𝘆 𝗼𝗿 𝗰𝗼𝗻𝘁𝗮𝗰𝘁 𝘁𝗼 😎 @kiraxophunter 😎** ")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"**𝗣𝗹𝗲𝗮𝘀𝗲 🥺 𝗮𝗱𝗱 @klm_player 𝗺𝗮𝗻𝘂𝘃𝗮𝗹𝘆 𝗼𝗿 𝗰𝗼𝗻𝘁𝗮𝗰𝘁 𝘁𝗼 😎 @kiraxophunter 😎...*")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"**💥 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗹𝗲𝘀𝘀 𝘁𝗵𝗮𝗻 {DURATION_LIMIT} 𝗺𝗶𝗻. 🥺 ...**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/c9e0ce23c63f595334283.jpg"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="💥 Jøɩɳ Ɦɘɤɘ & Sʋƥƥøɤʈ 💞",
                            url=f"https://t.me/CFC_BOT_SUPPORT")

                ]
            ]
        )

        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

            keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="💥 Jøɩɳ Ɦɘɤɘ & Sʋƥƥøɤʈ 💞",
                            url=f"https://t.me/CFC_BOT_SUPPORT")

                ]
            ]
        )

        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/c9e0ce23c63f595334283.jpg"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="💥 Jøɩɳ Ɦɘɤɘ & Sʋƥƥøɤʈ 💞",
                            url=f"https://t.me/CFC_BOT_SUPPORT")

                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗹𝗲𝘀𝘀 𝘁𝗵𝗮𝗻 {DURATION_LIMIT} 𝗺𝗶𝗻. 🥺...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit(
                "**𝗚𝗶𝘃𝗲 𝘀𝗼𝗻𝗴 𝗻𝗮𝗺𝗲 𝘁𝗼 𝗽𝗹𝗮𝘆 𝘀𝗼𝗻𝗴 𝘁𝗵𝗶𝘀 𝘄𝗮𝘆 /play [song name]...**"
            )
        await lel.edit("**🔄 𝗖𝗼𝗺𝗶𝗻𝗴 𝘁𝗼 𝗿𝗼𝗰𝗸 𝗼𝗻 𝘃𝗰 ...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await lel.edit(
                "**𝗦𝗼𝗻𝗴 𝗻𝗼𝘁 𝗳𝗼𝘂𝗻𝗱 📵𝗽𝗹𝘇 𝘁𝗿𝘆 𝗮𝗴𝗮𝗶𝗻 🥺...**"
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
            [
                [
                        InlineKeyboardButton(
                            text="💥 Jøɩɳ Ɦɘɤɘ & Sʋƥƥøɤʈ 💞",
                            url=f"https://t.me/CFC_BOT_SUPPORT")

                ]
            ]
        )

        if (dur / 60) > DURATION_LIMIT:
            await lel.edit(
                f"**💥 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗹𝗲𝘀𝘀 𝘁𝗵𝗮𝗻 {DURATION_LIMIT} 𝗺𝗶𝗻. 🥺...**"
            )
            return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_photo(
            photo="final.png",
            caption="**💥 𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ 𝗔𝗱𝗱𝗲𝗱 𝗮 𝘀𝗼𝗻𝗴 ❗️\n 𝗮𝘁 𝗽𝗼𝘀𝗶𝘁𝗶𝗼𝗻 » `{}` ❣️...**".format(position),
            reply_markup=keyboard,
        )
    else:
        await clientbot.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_photo(
            photo="final.png",
            reply_markup=keyboard,
            caption="**💥  𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ 𝗥𝗼𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 𝘃𝗰 🤘🤟 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆:- @kirarealdeathgod ...**".format(),
            
           )

    os.remove("final.png")
    return await lel.delete()
    
    
@Client.on_message(commandpro(["/pause", "pause"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    await clientbot.pytgcalls.pause_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg", 
                             caption="**💥  𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗿𝗼𝗰𝗸 𝗼𝗻 𝘃𝗰 ▶️🤟🤘...**"
    )


@Client.on_message(commandpro(["/resume", "resume"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    await clientbot.pytgcalls.resume_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/6fd7dffc9a4b7901c92a4.jpg", 
                             caption="**💥 𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ 𝘄𝗶𝗹𝗹 𝗿𝗼𝗰𝗸 𝗮𝗴𝗮𝗶𝗻 𝗼𝗻 𝘃𝗰🤘🤟⏸️...**"
    )



@Client.on_message(commandpro(["/skip", "/next", "skip", "next"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in clientbot.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) not in ACTV_CALLS:
        await message.reply_text("**💥 𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ 𝘄𝗶𝗹𝗹 𝗽𝗹𝗮𝘆 𝗻𝗲𝘅𝘁 𝗼𝗽 𝘀𝗼𝗻𝗴 🤟🤘⏩...**")
    else:
        queues.task_done(chat_id)
        
        if queues.is_empty(chat_id):
            await clientbot.pytgcalls.leave_group_call(chat_id)
        else:
            await clientbot.pytgcalls.change_stream(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        clientbot.queues.get(chat_id)["file"],
                    ),
                ),
            )


    await message.reply_photo(
                             photo="https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg", 
                             caption=f'**💥 𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ 𝘄𝗶𝗹𝗹 𝗽𝗹𝗮𝘆 𝗻𝗲𝘅𝘁 𝗼𝗽 𝘀𝗼𝗻𝗴 🤟🤘⏩ ...**'
   ) 


@Client.on_message(commandpro(["/end", "end", "/stop", "stop", "x"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        clientbot.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    await clientbot.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg", 
                             caption="**💥 𝘬𝓲𝘳ꪖ ᥊ ꪑꪊ𝘴𝓲ᥴ 𝗥𝗼𝗰𝗸𝗲𝗱 𝗼𝗻 𝘃𝗰 🤟🤘🚫 𝗽𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆:- @kirarealdeathgod ...**"
    )


@Client.on_message(commandpro(["reload", "refresh"]))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ),
    )

    await message.reply_photo(
                              photo="https://telegra.ph/file/e741ceb6e75683b9f0f81.jpg",
                              caption="**💥 💥 𝘬𝓲𝘳ꪖ ᥊  ꪑꪊ𝘴𝓲ᥴ 𝙬𝙞𝙡𝙡 𝙧𝙚𝙨𝙩𝙖𝙧𝙩 𝙞𝙣 1 𝙩𝙤 2 𝙢𝙞𝙣...**"
    )
