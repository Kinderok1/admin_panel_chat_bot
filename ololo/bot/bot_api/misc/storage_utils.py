import asyncio, os
from ..bot import bot,dp
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
    DATE = None
    FULL_DATE = None

    @classmethod
    async def cancel_task(cls):
        user = await dp.storage.get_data(user=cls.PK)
        task_id = user["task_id"]
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
        Sendler.objects.filter(pk=cls.PK).update(status=cls.STATUS+cls.FULL_DATE)

    @classmethod
    async def send(cls):
        caption = cls.CAPTION
        await bot.send_message(618669689,'caption')
        await cls.change_status()

        #await cls.cancel_task()

    @classmethod
    def time_difference(cls, start, end):
        start_dt = datetime.strptime(start, '%H:%M:%S')
        end_dt = datetime.strptime(end, '%H:%M:%S')
        diff = (end_dt - start_dt)
        result = diff.seconds
        return result

    @classmethod
    async def wait(cls, data:dict,):
        cls.FULL_DATE = data['date']
        cls.DATE = data['date'][11:]
        cls.STATUS = data['status']
        cls.CAPTION = data['caption']
        cls.PK = data['pk']
        logger.info('TRIGGERED')
        time_now = datetime.now()
        time_now = time_now.strftime("%H:%M:%S")
        wait = cls.time_difference(time_now, cls.DATE)
        await asyncio.sleep(wait)

        await cls.send()




