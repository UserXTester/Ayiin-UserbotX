""" Userbot module for other small commands. """
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.utils import edit_or_reply, ayiin_cmd


@ayiin_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await edit_or_reply(
        event,
        f"**Hai {me.first_name} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `{cmd}help` Atau Bisa Minta Bantuan Ke:\n"
        f"β **Group Support :** [π°ππΈπΈπ½ πππΏπΏπΎππ](t.me/AyiinXdSupport)\n"
        f"β **Channel Ayiin :** [π°ππΈπΈπ½ πππΏπΏπΎππ](t.me/AyiinSupport)\n"
        f"β **Owner Repo :** [ππΈπ½π](t.me/AyiinXd)\n"
        f"β **Repo :** [π°ππΈπΈπ½-πππ΄ππ±πΎπ](https://github.com/AyiinXd/Ayiin-Userbot)\n",
    )


@ayiin_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Ayiin-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variable-Heroku-Untuk-Ayiin-Userbot-02-08)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  Β»  **Perintah :** `{cmd}ihelp`\
        \n  Β»  **Kegunaan : **Bantuan Untuk Ayiin-Userbot.\
        \n\n  Β»  **Perintah :** `{cmd}listvar`\
        \n  Β»  **Kegunaan : **Melihat Daftar Vars.\
        \n\n  Β»  **Perintah :** `{cmd}repo`\
        \n  Β»  **Kegunaan : **Melihat Repository Ayiin-Userbot.\
        \n\n  Β»  **Perintah :** `{cmd}string`\
        \n  Β»  **Kegunaan : **Link untuk mengambil String Ayiin-Userbot.\
    "
    }
)
