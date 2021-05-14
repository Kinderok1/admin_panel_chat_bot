from aiogram import Dispatcher, types

from .errors import errors_handler
from .start import start_command
from .start import menu
from .start import menu_items
from .start import  process_callback_kb1btn1, process_callback_kb1btn2
from  .start import notice

def setup(dp: Dispatcher):
    dp.register_errors_handler(errors_handler)
    dp.register_message_handler(start_command, commands="start")
    dp.register_message_handler(menu,  regexp='Меню')
    dp.register_message_handler(menu_items, regexp='Десерты')
    dp.register_message_handler(notice, content_types=types.ContentType.TEXT, state="*")
    dp.register_callback_query_handler(process_callback_kb1btn2, lambda c: c.data and c.data.startswith('Роллы'))

    dp.register_callback_query_handler(process_callback_kb1btn1, lambda c: c.data and c.data.startswith('Десерты'))
