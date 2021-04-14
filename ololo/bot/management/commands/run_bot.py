import asyncio
from django.core.management.base import BaseCommand
from aiogram import Dispatcher, executor
from loguru import logger

from ...bot_api import handlers
from ...bot_api.bot import config, dp, bot_manager
from ...bot_api.misc import set_commands

class Command(BaseCommand):
    help = 'Запуск телеграм-бота'
    def handle(self, *args, **options):
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
