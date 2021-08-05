from ..bot import bot, PAYMENTS_TOKEN
from aiogram import types
from ..handlers.start import CallBackData
import emoji

async def process_buy_callback(callback_query: types.CallbackQuery):
    """create invoice pay"""
    IMAGE_URL = 'https://i.ibb.co/phhygV7/Screenshot-323.png'
    payments_data = callback_query.data.split('<')
    data = CallBackData.callback_data[payments_data[1]]

    # if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
    #     await bot.send_message(callback_query.from_user.id, 'Платеж является тестовым')

    PRICE = types.LabeledPrice(label=payments_data[1], amount=int(data['cost']+'00'))
    await bot.send_invoice(callback_query.from_user.id,
                           title=payments_data[1],
                           description=data['desc'],
                           provider_token=PAYMENTS_TOKEN,
                           currency='rub',
                           photo_url=IMAGE_URL,
                           photo_height=142,  # !=0/None, иначе изображение не покажется
                           photo_width=212,
                           prices=[PRICE],
                           start_parameter='deeplink-argument',
                           payload=data['link']
                           )
    q=1
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def process_successful_payment(message: types.Message):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')

    await bot.send_message(
        message.from_user.id,
        '{emoji2}Оплата прошла успешно.\n'
        'Сумма {total_amount}{currency} оплачена.\n'
        '{emoji1}Поздравляем,картина теперь ваша!\n'
        'Ссылка на картину:\n'
        '{item}'.format(
            total_amount=message.successful_payment.total_amount // 100,
            currency=message.successful_payment.currency,
            item=message.successful_payment.invoice_payload,
            emoji1= emoji.emojize(':tada:', use_aliases=True),
            emoji2=emoji.emojize(':white_check_mark:', use_aliases=True),

        )
    )
