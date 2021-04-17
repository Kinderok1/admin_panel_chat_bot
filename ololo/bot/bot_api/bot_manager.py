import asyncio
import shelve
from .misc.storage_utils import StorageHandler
from loguru import logger
from .bot import bot
data = dict()
FILENAME = r'C:\Users\павел\PycharmProjects\huita\ololo\bot\bot_api\misc\states2.db'

async def cancel_task(task_id: int):
    task_reg = {
        id(task): task for task in asyncio.all_tasks()
    }
    try:
        task_reg[task_id].cancel()
    except KeyError:
        logger.warning(
            f"Trying to cancel the non existing task"
        )
        pass



async def bla_bla():
    await StorageHandler.wait(data)




async def bot_manager():
    logger.info('Start bot_manager')
    #тут создать луп асинка,чтобы программа могла отслеживать несколько задач на рассылку
    loop = asyncio.get_event_loop()
    while True:
        try:
            with shelve.open(FILENAME) as states:
                data['date'] = states['date']
                data['caption'] = states['caption']
                data['status'] = states['status']
                data['pk'] = states['pk']
                states.clear()
            await bot.send_message(618669689, 'badsadasa')

            task = loop.create_task(bla_bla())
        except:
            await asyncio.sleep(3)
            logger.info('Cycling')
