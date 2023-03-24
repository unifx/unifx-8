# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de
# Edted by @satyaalfarabiii
# t.me/storesatya & t.me/satya_alfarabi
#

import asyncio
import base64
import re

from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

from config import ADMINS, FORCE_SUB_CHANNEL, FORCE_SUB_GROUP, FORCE_SUB_GROUP2, FORCE_SUB3, FORCE_SUB4, FORCE_SUB5, FORCE_SUB6, FORCE_SUB7

#fsub 1
async def subschannel(filter, client, update):
    if not FORCE_SUB_CHANNEL:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#fsub 2
async def subsgroup(filter, client, update):
    if not FORCE_SUB_GROUP:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB_GROUP, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#fsub 3
async def subsgroup2(filter, client, update):
    if not FORCE_SUB_GROUP2:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB_GROUP2, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#fsub 4
async def subsfsub3(filter, client, update):
    if not FORCE_SUB3:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB3, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#fsub 5
async def subsfsub4(filter, client, update):
    if not FORCE_SUB4:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB4, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#fsub 6
async def subsfsub5(filter, client, update):
    if not FORCE_SUB5:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB5, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#fsub 7
async def subsfsub6(filter, client, update):
    if not FORCE_SUB6:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB6, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#fsub 8
async def subsfsub7(filter, client, update):
    if not FORCE_SUB7:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB7, user_id=user_id)
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]

#cek join
async def is_subscribed(filter, client, update):
    if not FORCE_SUB_CHANNEL:
        return True
    if not FORCE_SUB_GROUP:
        return True
    if not FORCE_SUB_GROUP2:
        return True
    if not FORCE_SUB3:
        return True
    if not FORCE_SUB4:
        return True
    if not FORCE_SUB5:
        return True
    if not FORCE_SUB6:
        return True
    if not FORCE_SUB7:
        return True
    user_id = update.from_user.id
    if user_id in ADMINS:
        return True
    #cek join 1
    try:
        member = await client.get_chat_member(chat_id=FORCE_SUB_GROUP, user_id=user_id)
    except UserNotParticipant:
        return False
    #cek join 2
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_CHANNEL, user_id=user_id
        )
    except UserNotParticipant:
        return False
    #cek join 3
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB_GROUP2, user_id=user_id
        )
    except UserNotParticipant:
        return False
    #cek join 4
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB3, user_id=user_id
        )
    except UserNotParticipant:
        return False
    #cek join 5
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB4, user_id=user_id
        )
    except UserNotParticipant:
        return False
    #cek join 6
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB5, user_id=user_id
        )
    except UserNotParticipant:
        return False
    #cek join 7
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB6, user_id=user_id
        )
    except UserNotParticipant:
        return False
    #cek join 8
    try:
        member = await client.get_chat_member(
            chat_id=FORCE_SUB7, user_id=user_id
        )
    except UserNotParticipant:
        return False

    return member.status in ["creator", "administrator", "member"]


async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).strip("=")
    return base64_string

async def decode(base64_string):
    base64_string = base64_string.strip("=") # links generated before this commit will be having = sign, hence striping them to handle padding errors.
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes) 
    string = string_bytes.decode("ascii")
    return string


async def get_messages(client, message_ids):
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temb_ids = message_ids[total_messages : total_messages + 200]
        try:
            msgs = await client.get_messages(
                chat_id=client.db_channel.id, message_ids=temb_ids
            )
        except FloodWait as e:
            await asyncio.sleep(e.x)
            msgs = await client.get_messages(
                chat_id=client.db_channel.id, message_ids=temb_ids
            )
        except BaseException:
            pass
        total_messages += len(temb_ids)
        messages.extend(msgs)
    return messages


async def get_message_id(client, message):
    if (
        message.forward_from_chat
        and message.forward_from_chat.id == client.db_channel.id
    ):
        return message.forward_from_message_id
    elif message.forward_from_chat or message.forward_sender_name or not message.text:
        return 0
    else:
        pattern = "https://t.me/(?:c/)?(.*)/(\\d+)"
        matches = re.match(pattern, message.text)
        if not matches:
            return 0
        channel_id = matches.group(1)
        msg_id = int(matches.group(2))
        if channel_id.isdigit():
            if f"-100{channel_id}" == str(client.db_channel.id):
                return msg_id
        elif channel_id == client.db_channel.username:
            return msg_id


subsch = filters.create(subschannel)
subsgc = filters.create(subsgroup)
substai = filters.create(subsgroup2)
subsfs3 = filters.create(subsfsub3)
subsfs4 = filters.create(subsfsub4)
subsfs5 = filters.create(subsfsub5)
subsfs6 = filters.create(subsfsub6)
subsfs7 = filters.create(subsfsub7)
subsall = filters.create(is_subscribed)
