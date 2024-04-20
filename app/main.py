import asyncio

from pyrogram import idle

from core.bot import bot
from core.db import setup_db


async def main():
    await setup_db()
    await bot.start()
    await idle()
    await bot.stop()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
