# thanks for: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/ramadhani892/RamPyro-Bot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/ramsupportt

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from rams import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from rams.helpers.misc import create_botlog, git, heroku

MSG_ON = """
🔥 **RamPyro-Bot Menyala** 🔥
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
🤖 **Userbot Version -** `{}`
⌨️ **Ketik** `{}rama` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ramsupportt")
            await bot.join_chat("k0kb4c0de")
            await bot.join_chat("userbotch")
            await bot.join_chat("femily_nongki")
            await bot.join_chat("SharingUserbot")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("rams").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("rams").info(f"RamPyro-Bot v{BOT_VER} [🔥 UDAH AKTIF NGENTOT! 🔥]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("rams").info("Starting RamPyro-Bot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
