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
            text=f"<b>Informasi.\n\n • OWNER REPO : @satyaalfarabiii\n • CHANNEL : <a href='https://t.me/storesatya'>JOIN</a>\n • SOURCE CODE : <a href='https://t.me/satya_alfarabi'>JOIN</a>\n\n Support @bgsatbot</b>\n",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• 𝗧𝗨𝗧𝗨𝗣 •", callback_data="close")]]
            ),
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass
