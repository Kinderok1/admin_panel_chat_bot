from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import types
import os, sys
import django
from attr import filters

from ..keyboards.keyboards import DefaultConstructor

django.setup()

from aiogram.dispatcher.filters.state import State, StatesGroup
from ...models import Items, Notifications, Members
from ..bot import bot, dp


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


# !!!Need refactoring: callback functions is repeating
async def process_callback_kb1btn2(callback_query: types.CallbackQuery):
    us = Members.objects.filter(id_t=callback_query.from_user.id).update(user_state='В разделе "Роллы"')
    try:
        search = Items.objects.filter(type=2)  # HARDCODE

        pay_markup = InlineKeyboardMarkup()
        pay_markup.insert(
            InlineKeyboardButton(
                "Купить", url="https://github.com/comictomcat/aiogram-template"
            )
        )

        for e in search:
            caption = '<b>%s</b> \n %s' % (e.caption, e.description)
            photo = types.InputFile(e.image.path)
            await bot.send_photo(callback_query.from_user.id, photo, caption, reply_markup=pay_markup)

        #

    except:
        await bot.send_message(callback_query.from_user.id, 'Товаров в этой категории нет')


async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    user_state = Members.objects.filter(id_t=callback_query.from_user.id).update(user_state='В разделе "Десерты"')
    try:
        search = Items.objects.filter(type='Десерты')
        q = 1
    except:
        await bot.send_message(callback_query.from_user.id, 'Товаров в этой категории нет')


async def start_command(m: Message):
    """
    Responds to /start.
    тут будет первичная запись в базу!
    """

    # Отлично подойдет для кнопки в чате!!!
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
    link = '<a href="https://telegra.ph/Eshe-04-24">link text</a>'
    await bot.send_message(m.from_user.id, link)
    await m.reply("Welcome", reply_markup=keyboard)


async def menu(m: types.Message):
    user_state = Members.objects.filter(id_t=m.from_user.id).update(user_state='В разделе меню')
    keyboard = DefaultConstructor.create_kb()
    await m.reply('Меню', reply_markup=keyboard)


async def menu_items(m: types.Message):
    pass
    # меню должно быть колбэкное
    # но для видео я эту логику реализовывать не буду!


async def notice(m: types.Message):
    id_t = m.from_user.id
    user_name = m.from_user.full_name
    notification = Notifications.objects.create(from_user_id=id_t, from_user_name=user_name)

# хандлер корзины
# хандлер оплаты
#    user_state = Members.objects.filter(id_t=m.from_user.id).update(user_state='В разделе меню')
#    user_state = Members.objects.filter(id_t=m.from_user.id).update(user_state='В разделе меню')
