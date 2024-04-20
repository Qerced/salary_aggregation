import json

from core.config import settings
from core.db import get_aggregated_salary
from core.validators import check_data
from pyrogram import Client, filters

bot = Client(
    settings.bot_name, settings.api_id,
    settings.api_hash, bot_token=settings.bot_token,
    # in_memory=True
)


@bot.on_message(filters.text)
async def handle_text_message(client, message):
    try:
        data, operation = await check_data(json.loads(message.text))
    except Exception as error:
        await message.reply_text(error)
    else:
        await message.reply_text(
            json.dumps(await get_aggregated_salary(data, operation))
        )
