import random
import asyncio
from pyrogram import filters
from FallenRobot import pbot as FallenRobot




WISH_STRINGS = [
                "मेरी वफा की कदर ना की अपनी पसन्द पे एतबार किया होता,सुना है वो उनकी भी ना हुई मुझे छोड़ दिया था तो उसे अपना लिया होता!",
                "मुद्दतों बाद भी नहीं मिलते हम जैसे नायाब लोग तेरे हाथ क्या लग गए तुमने तो हमे आम समझ लिया!",
                "अभी तक मौजूद है इस दिल पर तेरे कदमों के निशां..हमने तेरे बाद किसी को इस राह से गुजरने नहीं दिया!",
                "बेहद करीब है वो शख़्स आज भी मेरे इस दिल के, जिसने खामोशियों का सहारा लेकर दुरियों को अंजाम दिया.",
                "हो सके तो फिर मिलेंगे, शायद अनजान बनकर कोई नई जिंदगी जी कर, कोई नई पहचान बनकर.",
                "ᴋʏᴀ ғᴀʀᴋ ᴘᴀᴅᴛᴀ ʜᴀɪ ᴍᴇʀᴇ ʜᴀsɴᴇ sᴇ ...ᴍᴇʀᴇ ʀᴏɴᴇ sᴇ ᴍᴇʀᴇ ʜᴏɴᴇ sᴇ ...ʏᴀ ᴍᴇʀᴇ ɴᴀ ʜᴏɴᴇ sᴇ... 🥺!",
                "ʏᴇ ʀᴀᴀᴛ ʜᴜᴍꜱᴇ ʙᴏʜᴏᴛ ᴘʏᴀᴀʀ ᴋᴀʀᴛɪ ʜᴀɪɴ,ꜱᴀʙᴋᴏ ꜱᴜʟᴀᴋᴀʀ ʜᴜᴍꜱᴇ ᴀᴋᴇʟᴇ ᴍᴀɪɴ ʙᴀᴀᴛ ᴋᴀʀᴛɪ ʜᴀɪ...!!🥺💔🥺!",
                "May god bless my angelic sister with loads of happiness, health and success. Happy Raksha Bandhan.",
                "I wait for the day throughout the year to see you tie a Rakhi so religiously on my wrist and pray to God for my well-being. Sweetest Sis, I wish our bond grows stronger day by day...",
                "To have an affectionate relationship with a sister is not just to have a friend or a confidant -- it is to have a companion for life."
               ]


@FallenRobot.on_message(filters.command(["rakshabandhan", "rakhi"]))
async def lel(bot, message):
    ran = random.choice(WISH_STRINGS)
    await bot.send_chat_action(message.chat.id, "Typing")
    await asyncio.sleep(1)
    return await message.reply_text(text=ran)

__mod_name__ = "ʀᴀᴋʜɪ"

__help__ = """

*ᴍᴀᴋᴇs ᴀ ʀᴀᴋsʜᴀʙᴀɴᴅʜᴀɴ ǫᴜᴏᴛᴇ ғᴏʀ ᴜʀ sɪsᴛᴇʀ & ʙʀᴏᴛʜᴇʀ* \n*ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛʜᴇᴍ.*

❍ /rakhi *:* *ᴡʀɪᴛᴇ ᴀ ǫᴜᴏᴛᴇ ғᴏʀ ʏᴏᴜʀ sɪsᴛᴇʀ.* \n\n ❍ /rakshabandhan *:* *ᴡʀɪᴛᴇ ǫᴜᴏᴛᴇ ғᴏʀ ʏᴏᴜʀ ʙʀᴏᴛʜᴇʀ!!.* \n\n [🥀Support Chat🥀](t.me./Team_STD_Network)

 """
