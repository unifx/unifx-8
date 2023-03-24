# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/userbotch & t.me/ramsupportt
# Add Code FROM 3-BUTTONS <https://github.com/ramadhani892/3-BUTTONS
# Edted by @satyaalfarabiii
# t.me/storesatya & t.me/satya_alfarabi

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_GROUP2, FORCE_SUB3, FORCE_SUB4, FORCE_SUB5, FORCE_SUB6, FORCE_SUB7
from pyrogram.types import InlineKeyboardButton

# klik start tanpa paksa join
def start_button(client):
    # kondisi -> fsub gadipake
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 1 button
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 2 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 3 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and not FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 4 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 5 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 6 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 7 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and FORCE_SUB5 and FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink7),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons
    # kondisi -> fsub 8 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and FORCE_SUB5 and FORCE_SUB6 and FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink7),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink8),
            ],
            [
                InlineKeyboardButton(text="• 𝗧𝗲𝗻𝘁𝗮𝗻𝗴 𝗦𝗮𝘆𝗮 •", callback_data="about"),
                InlineKeyboardButton(text="• 𝗧𝘂𝘁𝘂𝗽 •", callback_data="close"),
            ],
        ]
        return buttons

# klik start paksa join
def fsub_button(client, message):
    #fsub 1 button
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons
    #fsub 2 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and not FORCE_SUB_GROUP2 and not FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons
    #fsub 3 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and not FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons
    #fsub 4 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and not FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons
    #fsub 5 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and not FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons
    #fsub 6 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and FORCE_SUB5 and not FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink6),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons
    #fsub 7 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and FORCE_SUB5 and FORCE_SUB6 and not FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink7),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons
    #fsub 8 button
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP and FORCE_SUB_GROUP2 and FORCE_SUB3 and FORCE_SUB4 and FORCE_SUB5 and FORCE_SUB6 and FORCE_SUB7:
        buttons = [
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink3),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink4),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink5),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink6),
            ],
            [
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink7),
                InlineKeyboardButton(text="• 𝗝𝗼𝗶𝗻 𝗦𝗲𝗸𝗮𝗿𝗮𝗻𝗴 •", url=client.invitelink8),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                            text="• 𝗖𝗼𝗯𝗮 𝗟𝗮𝗴𝗶 •",
                            url=f"https://t.me/{client.username}?start={message.command[1]}",
                        )
                ]
            )
        except IndexError:
            pass
        return buttons

