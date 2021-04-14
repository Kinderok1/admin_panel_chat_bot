import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .misc import parse_config

# Project directory
ROOT_DIRECTORY = Path(__file__).parent

# Config
config = parse_config(ROOT_DIRECTORY / "config.yaml")

# Bot, storage and dispatcher instances
bot = Bot(**config.get("bot"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def bot_manager():
    while True:
        pass