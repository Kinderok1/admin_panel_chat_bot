import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .misc.helper import parse_config

# Project directory
ROOT_DIRECTORY = Path(__file__).parent

# Config
config = parse_config(ROOT_DIRECTORY / "config.yaml")

# Bot, storage and dispatcher instances
PAYMENTS_TOKEN = config.get("test_payment_token")[0]
bot = Bot(**config.get("bot"))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

