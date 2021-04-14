import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'ololo.settings'
django.setup()
from bot.models import Items

import logging

from aiogram import Bot, Dispatcher, executor, types

import asyncio
from aiogram.types.message import ContentType
from messages import MESSAGES


PAYMENTS_PROVIDER_TOKEN = '381764678:TEST:24071'

TIME_MACHINE_IMAGE_URL = 'http://erkelzaar.tsudao.com/models/perrotta/TIME_MACHINE.jpg'


API_TOKEN = '1043923109:AAG26SjtlMZLd5mmPt78D8Fch7vYnlTCPoM'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

PRICE = types.LabeledPrice(label='Настоящая Машина Времени', amount=4200000)

async def process_terms_command(message: types.Message):
    await message.reply(MESSAGES['terms'], reply=False)

async def finder(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    find = Items.objects.all()

    message_reply = "Привет!\nМеня зовут FindBot!\n%s" % find
    await message.reply(message_reply, parse_mode=types.ParseMode.MARKDOWN)

#set callback to this handler!
async def process_buy_command(message: types.Message):
    if PAYMENTS_PROVIDER_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, MESSAGES['pre_buy_demo_alert'])

    await bot.send_invoice(message.chat.id,
                           title=MESSAGES['tm_title'],
                           description=MESSAGES['tm_description'],
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='rub',
                           photo_url=TIME_MACHINE_IMAGE_URL,
                           photo_height=512,  # !=0/None, иначе изображение не покажется
                           photo_width=512,
                           photo_size=512,
                           is_flexible=False,  # True если конечная цена зависит от способа доставки
                           prices=[PRICE],
                           start_parameter='time-machine-example',
                           payload='some-invoice-payload-for-our-internal-use'
                           )
@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')

    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency
        )
    )




dp.register_message_handler(
    process_terms_command,
    commands=["terms"],
)

dp.register_message_handler(
    process_buy_command,
    commands=["buy"],
)

# dp.register_message_handler(
#     process_buy_command,
#     lambda query: True
# )

dp.register_message_handler(
    finder,
    content_types=types.ContentType.TEXT,
    state="*"
)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)