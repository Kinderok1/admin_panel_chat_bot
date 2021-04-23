from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import types
import os, sys
import django
from attr import filters

from ..keyboards.keyboards import DefaultConstructor
django.setup()

from aiogram.dispatcher.filters.state import State, StatesGroup
from ...models import Items,Notifications,Members
from ..bot import bot,dp

# States
class Form(StatesGroup):
    ep1 = State()  # Will be represented in storage as 'Form:ep1'
    ep2 = State()  # Will be represented in storage as 'Form:ep2'
    ep3 = State()  # Will be represented in storage as 'Form:ep3'
    ep4 = State()  # Will be represented in storage as 'Form:ep4'
    mes = State()
    ep5 = State()  # Will be represented in storage as 'Form:ep5'
    ep6 = State()  # Will be represented in storage as 'Form:ep6'
    goodBye = State()

async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    try:
        search = Items.objects.filter(type='Десерты')
        q = 1
    except:
        await bot.send_message(callback_query.from_user.id, 'Товаров в этой категории нет')

async def start_command(m: Message):
    """
    Responds to /start.
    """
    #Отлично подойдет для кнопки в чате!!!
    # # Create an inline keyboard
    # welcome_markup = InlineKeyboardMarkup()
    #
    # # Insert a button with a url
    # welcome_markup.insert(
    #     InlineKeyboardButton(
    #         "My Sources", url="https://github.com/comictomcat/aiogram-template"
    #     )
    # )
    #
    # await m.answer(
    #     f"Hello there, <b>{m.from_user.first_name}</b>!", reply_markup=welcome_markup
    # )
    keyboard = DefaultConstructor.create_main_kb()
    await m.reply("Welcome", reply_markup=keyboard)

async def menu(m: types.Message):
    keyboard = DefaultConstructor.create_kb()
    await m.reply('Меню', reply_markup=keyboard)
    #найти в базе по айдишнику
    #апдэйтнуть статус

async def menu_items(m: types.Message):
    pass
    #меню должно быть колбэкное
    #но для видео я эту логику реализовывать не буду!
async def notice(m: types.Message):
    id_t = m.from_user.id
    user_name = m.from_user.full_name
    notification = Notifications.objects.create(from_user_id=id_t, from_user_name=user_name)