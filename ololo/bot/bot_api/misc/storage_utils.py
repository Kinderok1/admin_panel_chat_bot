import asyncio, os
from ..bot import bot
from datetime import datetime
from ...models import Sendler
from loguru import logger
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
from asgiref.sync import sync_to_async
class StorageHandler():
    PK = None
    FLAG = None
    CAPTION = None
    STATUS = None


    @classmethod
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

    @classmethod
    @sync_to_async()
    def change_status(cls):
        Sendler.objects.filter(pk=cls.PK).update(status=cls.STATUS)
        q=1
    @classmethod
    async def send(cls):
        caption = cls.CAPTION
        await bot.send_message(618669689,'caption')
        await cls.change_status()

        #await cls.cancel_task(cls.ID_TASK)

    @classmethod
    def time_difference(cls, start, end):
        start_dt = datetime.strptime(start, '%H:%M:%S')
        end_dt = datetime.strptime(end, '%H:%M:%S')
        diff = (end_dt - start_dt)
        result = diff.seconds
        return result

    @classmethod
    async def wait(cls, data:dict,):

        cls.DATE = data['date']
        cls.STATUS = data['status']
        cls.CAPTION = data['caption']
        cls.PK = data['pk']
        logger.info('TRIGGERED')
        time_now = datetime.now()
        time_now = time_now.strftime("%H:%M:%S")
       # wait = cls.time_difference(time_now, cls.DATE)

        #await asyncio.sleep(wait)

        await cls.send()



