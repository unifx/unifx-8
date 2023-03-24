
import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_CHANNEL,
    FORCE_SUB_GROUP,
    FORCE_SUB_GROUP2,
    FORCE_SUB3,
    FORCE_SUB4,
    FORCE_SUB5,
    FORCE_SUB6,
    FORCE_SUB7,
    LOGGER,
    OWNER,
    TG_BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        try:
            await super().start()
            usr_bot_me = await self.get_me()
            self.username = usr_bot_me.username
            self.namebot = usr_bot_me.first_name
        except Exception as a:
            self.LOGGER(__name__).warning(a)
            self.LOGGER(__name__).info(
                "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
            )
            sys.exit()

        # button 1
        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_CHANNEL!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB_CHANNEL}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # button 2
        if FORCE_SUB_GROUP:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP)
                    link = (await self.get_chat(FORCE_SUB_GROUP)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_GROUP!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Group Tersebut, Chat ID F-Subs Group Saat Ini: {FORCE_SUB_GROUP}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # button 3
        if FORCE_SUB_GROUP2:
            try:
                link = (await self.get_chat(FORCE_SUB_GROUP2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_GROUP2)
                    link = (await self.get_chat(FORCE_SUB_GROUP2)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB_GROUP2!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB_GROUP2}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # button 4
        if FORCE_SUB3:
            try:
                link = (await self.get_chat(FORCE_SUB3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB3)
                    link = (await self.get_chat(FORCE_SUB3)).invite_link
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB3!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB3}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # button 5
        if FORCE_SUB4:
            try:
                link = (await self.get_chat(FORCE_SUB4)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB4)
                    link = (await self.get_chat(FORCE_SUB3)).invite_link
                self.invitelink5 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB4!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB4}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # button 6
        if FORCE_SUB5:
            try:
                link = (await self.get_chat(FORCE_SUB5)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB5)
                    link = (await self.get_chat(FORCE_SUB5)).invite_link
                self.invitelink6 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB5!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB5}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # button 7
        if FORCE_SUB6:
            try:
                link = (await self.get_chat(FORCE_SUB6)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB6)
                    link = (await self.get_chat(FORCE_SUB6)).invite_link
                self.invitelink7 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB6!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB6}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # button 8
        if FORCE_SUB7:
            try:
                link = (await self.get_chat(FORCE_SUB7)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB7)
                    link = (await self.get_chat(FORCE_SUB7)).invite_link
                self.invitelink8 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link invite dari FORCE_SUB7!"
                )
                self.LOGGER(__name__).warning(
                    f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCE_SUB7}"
                )
                self.LOGGER(__name__).info(
                    "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
                )
                sys.exit()

        # database
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="🔥 BOT BERHASIL DIAKTIFKAN! 🔥")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan @{self.username} adalah admin di Channel DataBase anda, CHANNEL_ID Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "Bot Berhenti. Hubungi https://t.me/bgsatbot untuk Bantuan"
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥]\n\nBOT Dibuat oleh @{OWNER}\nJika @{OWNER} Membutuhkan Bantuan, Silahkan Hubungi https://t.me/bgsatbot"
        )

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
