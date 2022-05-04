# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os

import heroku3
from telethon.errors import FloodWaitError

from AyiinXd import BLACKLIST_GCAST
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, DEVS, HEROKU_API_KEY, HEROKU_APP_NAME
from AyiinXd.utils import ayiin_cmd, edit_delete, edit_or_reply

GCAST_BLACKLIST = [
    -1001200629564, # [03] Test Deadly X Yukki
    -1001220709531, # [08C] M3$ - DX & MX
    -1001233731565, # [02] GC Test 🤖 [yellow]x
    -1001153220287, # [01] GC Test 🤖 [white]
    -1001769312871, # GROUP CHAOS
    -1001607863864, # [08D] M4 DLX
    -1001596829631, # [08A] M1 - DeadlyXbot
    -1001330015329, # [08B] M2 - Alpha & Beta
    -1001121508405, # TeamX [#log]
    -1001346029874, # [06] PabrikBot X
    -1001293374538, # ADMIN INTI [XTEAM VIP]
    -1001355701394, # Sumatera VIP
    -1001312536930, # Jambi City VIP
    -1001519270474, # TEAM VIP [FEDERASI]
    -1001316159619, # Sulawesi VIP
    -1001466910048, # Jawa VIP
    -1001370565835, # cariteman1 vip
    -1001442678073, # anonymeet vip
    -1001457877280, # podcast vip
    -1001263091728, # kutipan insecure GC
    -1001365683522, # kalimanta vip
    -1001471517253, # pekanbaru
    -1001162379117, # palembang
    -1001401263904, # medan
    -1001409245390, # padang
    -1001382715380, # lampung
    -1001457517148, # aceh
    -1001241283174, # AlphaXGank
    -1001410961692, # TGdev desu <indo day> = fadil
    -1001310420564, # GAS Testing Grup
    -1001419516987, # Veez Support Group 🇮🇩
    -1001209432070, # Geez Support Group
    -1001473548283, # 𝗦𝗵𝗮𝗿𝗶𝗻𝗴 𝗕𝗼𝘁 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 🇮🇩

]

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("BLACKLIST_GCAST") or ""


@ayiin_cmd(pattern="gcast(?: |$)(.*)")
async def gcast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`𝙎𝙖𝙗𝙖𝙧 𝙏𝙤𝙙 𝙇𝙖𝙜𝙞 𝙂𝙪𝙖 𝙆𝙞𝙧𝙞𝙢, 𝙆𝙖𝙡𝙤 𝙇𝙞𝙢𝙞𝙩 𝙅𝙖𝙣𝙜𝙖𝙣 𝙎𝙖𝙡𝙖𝙝𝙞𝙣 𝙂𝙪𝙖 𝘼𝙣𝙟𝙞𝙣𝙜...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** {done} **Grup Tod.**\n**Sorry Tod Gagal Mengirim Pesan Ke** {er} **Grup.**"
    )


@ayiin_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`𝙎𝙖𝙗𝙖𝙧 𝙏𝙤𝙙 𝙇𝙖𝙜𝙞 𝙂𝙪𝙖 𝙆𝙞𝙧𝙞𝙢, 𝙆𝙖𝙡𝙤 𝙇𝙞𝙢𝙞𝙩 𝙅𝙖𝙣𝙜𝙖𝙣 𝙎𝙖𝙡𝙖𝙝𝙞𝙣 𝙂𝙪𝙖 𝘼𝙣𝙟𝙞𝙣𝙜...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** {done} **Chat Tod.**\n**Sorry Tod Gagal Mengirim Pesan Ke** {er} **Chat.**"
    )


@ayiin_cmd(pattern="blchat$")
async def sudo(event):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    blc = blchat
    list = blc.replace(" ", "\n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            event,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n» {list}\n\nKetik `{cmd}addblacklist` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_delete(event, "🔮 **Blacklist GCAST:** `Disabled`")


@ayiin_cmd(pattern="addblacklist(?:\\s|$)([\\s\\S]*)")
async def add(event):
    xxnx = await edit_or_reply(event, "`Processing...`")
    var = "BLACKLIST_GCAST"
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxnx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    blgc = f"{BLACKLIST_GCAST} {gc}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await xxnx.edit(
        f"**Berhasil Menambahkan** `{gc}` **ke daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
    )
    heroku_Config[var] = blacklistgrup


@ayiin_cmd(pattern="delblacklist(?:\\s|$)([\\s\\S]*)")
async def _(event):
    xxx = await edit_or_reply(event, "`Processing...`")
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await xxx.edit(
            f"**Berhasil Menghapus** `{gc}` **dari daftar blacklist gcast.**\n\nSedang MeRestart Heroku untuk Menerapkan Perubahan."
        )
        var = "BLACKLIST_GCAST"
        heroku_Config[var] = blacklistgrup
    else:
        await edit_delete(
            xxx, "**Grup ini tidak ada dalam daftar blacklist gcast.**", 45
        )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  »  **Perintah :** `{cmd}gcast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Grup yang kamu masuk. (Bisa Mengirim Media/Sticker)\
        \n\n  »  **Perintah :** `{cmd}blchat`\
        \n  »  **Kegunaan : **Untuk Mengecek informasi daftar blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}addblacklist`\
        \n  »  **Kegunaan : **Untuk Menambahkan grup tersebut ke blacklist gcast.\
        \n\n  »  **Perintah :** `{cmd}delblacklist`\
        \n  »  **Kegunaan : **Untuk Menghapus grup tersebut dari blacklist gcast.\
        \n  •  **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  »  **Perintah :** `{cmd}gucast` <text/reply media>\
        \n  »  **Kegunaan : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
