from aiogram import Dispatcher, types

from .errors import errors_handler
from .start import start_command
from .start import menu
from .start import menu_items
from .start import process_callback_kb1btn1, process_callback_kb1btn2
from .start import notice
from .payments import process_buy_callback
from .payments import process_pre_checkout_query
from .payments import process_successful_payment



def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(menu, regexp='Каталог')
    dp.register_message_handler(notice, content_types=types.ContentType.TEXT, state="*")
    dp.register_callback_query_handler(process_callback_kb1btn2, lambda c: c.data and c.data.startswith('Символизм'))
    dp.register_callback_query_handler(process_callback_kb1btn1, lambda c: c.data and c.data.startswith('Поп-арт'))
    dp.register_callback_query_handler(process_buy_callback, lambda c: c.data and c.data.startswith('Купить'))
    dp.register_pre_checkout_query_handler(process_pre_checkout_query, lambda shipping_query: True)
    dp.register_message_handler(process_successful_payment, content_types=types.ContentType.SUCCESSFUL_PAYMENT)