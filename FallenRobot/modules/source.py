from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


GANDU_BSDK = "https://telegra.ph/file/152a82a8719fda9ef7d32.jpg"


@client.on_message(filters.command(["repo", "source", "gand"]))
async def repo(client, message):
    await message.reply_animation(
        animation=GANDU_BSDK,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴍᴀʜᴀᴋᴀʟ ʀᴏʙᴏᴛ-🇮🇳](t.me/MahakalRobot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝐒𝐓𝐃](t.me/STD_KING)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴮᵉᵗᵘメ ˹ʟɪꜰᴇʟɪɴᴇ˼➳『🇮🇳』 sᴏᴜʀᴄᴇ ɪs ᴘʀɪᴠᴀᴛᴇ 🥺 sᴏ ᴜsᴇ ᴮᵉᵗᵘメ ˹ʟɪꜰᴇʟɪɴᴇ˼➳『🇮🇳』 ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘs.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="t.me/STD_KING"),
                    InlineKeyboardButton(
                        "• sᴜᴘᴘᴏʀᴛ •",
                        url="https://t.me/Devilshavelimf",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
