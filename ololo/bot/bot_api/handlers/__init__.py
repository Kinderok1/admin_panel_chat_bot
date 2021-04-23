from aiogram import Dispatcher

from .errors import errors_handler
from .start import start_command
from .start import menu
from .start import menu_items
from .start import process_callback_kb1btn1
from  .start import notice

def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(menu,  regexp='Меню')
    dp.register_message_handler(menu_items, regexp='Десерты')
    dp.register_message_handler(notice, commands="notice")
    dp.register_callback_query_handler(process_callback_kb1btn1, lambda c: c.data and c.data.startswith('Десерты'))