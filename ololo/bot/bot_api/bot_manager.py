import asyncio
from .misc.storage_set import flag
from .misc.storage_utils import StorageHandler
from loguru import logger


async def bot_manager():
    logger.info('Start bot_manager')

    while True:
        print('****************************************************************************')
        print(flag)
        print('****************************************************************************')
        if flag[1]:
            await StorageHandler.wait()
        await asyncio.sleep(10)
        logger.info('Cycling')
