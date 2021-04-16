import asyncio
from ..bot import dp,bot
from datetime import datetime
from ...models import Sendler
from .storage_set import flag
from loguru import logger

class StorageHandler():
    PK = None
    FLAG = None
    CAPTION = None
    STATUS = None
    # @classmethod
    # def prepare_message(cls):
    #     caption =
    #     text =
    #     image = ''

    @classmethod
    def change_status(cls):
        obj = Sendler.objects.get(pk=1)
        obj.status = flag[2]
        obj.save(update_fields=['status',])

    @classmethod
    async def send(cls):
        caption = flag[2]
        await bot.send_message(618669689,caption)
        cls.change_status()

    @classmethod
    def time_difference(cls, start, end):
        start_dt = datetime.strptime(start, '%H:%M:%S')
        end_dt = datetime.strptime(end, '%H:%M:%S')
        diff = (end_dt - start_dt)
        result = diff.seconds
        return result

    @classmethod
    async def wait(cls):
        logger.info('TRIGGERED')
        time_now = datetime.now()
        time_now = time_now.strftime("%H:%M:%S")
        wait = cls.time_difference(time_now, flag[1])

        await asyncio.sleep(wait)

        await cls.send()




