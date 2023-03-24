# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Recode now By @thisrama
# t.me/ramsupportt & t.me/userbotch
# Edted by @satyaalfarabiii
# t.me/storesatya & t.me/satya_alfarabi

from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from bot import Bot
from config import OWNER


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"<b>Informasi.\n\n • OWNER REPO : <a href='https://t.me/satyaalfarabiii'>𝐒𝐚𝐭𝐲𝐚 𝐀𝐥𝐟𝐚𝐫𝐚𝐛𝐢</a>\n • CHANNEL : <a href='https://t.me/storesatya'>𝐉𝐎𝐈𝐍</a>\n • SOURCE CODE : <a href='https://t.me/satya_alfarabi'>𝐤𝐥𝐢𝐤 𝐝𝐢𝐬𝐢𝐧𝐢</a>\n\n Support @bgsatbot</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
