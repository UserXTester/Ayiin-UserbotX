# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================ร========================
#            Jangan Hapus Credit Ngentod
# ========================ร========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd.events import register
from .ping import get_readable_time

KONTOL = [175232702, 1192566681, 1282174237]

absen = [
    "**๐๐๐๐๐ง ๐๐ค๐ฃ๐ ๐๐ค๐** ๐",
    "**๐๐๐๐๐ง ๐๐๐ ๐ ๐๐๐ฃ๐ฉ๐๐ฃ๐** ๐",
    "**๐๐ช๐ ๐๐๐๐๐ง ๐พ๐ค๐ฃ๐ฉ๐ค๐ก** ๐",
    "**๐๐ช๐ ๐๐๐๐๐ง ๐๐๐ฃ๐ฉ๐๐ฃ๐** ๐ฅต",
    "**๐๐๐๐๐ง ๐๐๐๐** ๐",
    "**๐๐ช๐ ๐๐๐๐๐ง ๐ผ๐๐๐ฃ๐** ๐ฅบ",
    "**๐๐ ๐พ๐๐ ๐๐ฅ ๐๐๐๐๐ง ๐ฝ๐๐ฃ๐** ๐",
]

ayiincakep = [
    "**iya kakak ganteng banget** ๐",
    "**๐๐๐ฃ๐ฉ๐๐ฃ๐๐ฃ๐ฎ๐ ๐๐๐  ๐ผ๐๐ ๐๐๐ฌ๐๐ฃ** ๐",
    "**Kakak Gantengnya Aku kan** ๐",
    "**Gak ada Saingan Kakak** ๐",
    "**Kakak Jelek tapi bohoong** ๐",
]


@register(incoming=True, from_users=KONTOL, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**โง ๐ฐ๐๐ธ๐ธ๐ฝ-๐๐๐ด๐๐ฑ๐พ๐ โง**\n\nโง **แดษชษดษขแดส :** `%sms`\nโง **แดแดแดษชแดแด :** `{}`\nโง **แดแดกษดแดส :** `{}`\nโง **ษชแด :** `{}`" % (
        duration)
    await ping.reply(message.format(uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK ๐ก
# JANGAN DI HAPUS GOBLOK ๐ก LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA ๐ฅด GUA TANDAIN LU AKUN TELENYA ๐ก

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=KONTOL, pattern=r"^Absen$")
async def ayiinabsen(ganteng):
    await ganteng.reply(choice(absen))


@register(incoming=True, from_users=KONTOL, pattern=r"^Ayiin ganteng kan$")
async def ayiin(ganteng):
    await ganteng.reply(choice(ayiincakep))


# ========================ร========================
#            Jangan Hapus Credit Ngentod
# ========================ร========================


CMD_HELP.update(
    {
        "yinsping": f"**Plugin:** `yinsping`\
        \n\n  ยป  **Perintah : **`Perintah Ini Hanya Untuk Devs Ayiin-Userbot Tod.`\
        \n  ยป  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
