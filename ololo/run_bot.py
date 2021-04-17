import asyncio, os
from django.core.management.base import BaseCommand
from aiogram import Dispatcher, executor
from loguru import logger
import django
# from ...bot_api import handlers
# from ...bot_api.bot import config, dp
# from ...bot_api.bot_manager import bot_manager
# from ...bot_api.misc.helper import set_commands
os.environ['DJANGO_SETTINGS_MODULE'] = 'ololo.settings'
django.setup()

from bot.bot_api import handlers
from bot.bot_api.bot import config, dp
from bot.bot_api.bot_manager import bot_manager
from bot.bot_api.misc.helper import set_commands




async def startup(dispatcher: Dispatcher):
    """Triggers on startup."""

    # Setup handlers
    logger.info("Configuring handlers...")
    handlers.setup(dispatcher)

    # Set command hints
    await set_commands(dispatcher, config.get("commands"))

    logger.info("Start polling")

    loop = asyncio.get_event_loop()
    loop.create_task(bot_manager())

executor.start_polling(dp, on_startup=startup, **config.get("executor"))
