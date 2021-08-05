import os
import emoji
from typing import Dict, List, Union

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

from ...models import Type
from loguru import logger
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
from asgiref.sync import sync_to_async






class DefaultConstructor:
    aliases = {
        'Абстракционизм':  ':black_large_square:',
        'Символизм': ':imp:',
        'Сюрреализм':  ':clock7:',
        'Романтизм': ':heartpulse:',
        'Модернизм': ':surfer:',
        'Поп-арт':   ':lollipop:',
    }
    available_properities = ['text', 'request_contact', 'request_location', 'request_poll']
    properties_amount = 2

    #Need refactoring!
    @classmethod
    def create_kb(cls):
        inline_kb_full = InlineKeyboardMarkup(row_width=2)
        types = Type.objects.values('name')
        for t in types:
            name = '%s %s' % (emoji.emojize(cls.aliases[t['name']],use_aliases=True),t['name'])
            if t['name'] == 'Поп-арт':
                inline_kb_full.insert(InlineKeyboardButton(name, callback_data='Поп-арт'))
            elif t['name'] == 'Символизм':
                inline_kb_full.insert(InlineKeyboardButton(name, callback_data='Символизм'))
            else:
                inline_kb_full.insert(InlineKeyboardButton(name,callback_data='_'))

        return inline_kb_full

    @classmethod
    def create_main_kb(cls):
        inline_kb_full = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        button1 = KeyboardButton('%s Каталог' % emoji.emojize(':art:',use_aliases=True))
        button2 = KeyboardButton('%s Корзина' % emoji.emojize(':package:', use_aliases=True))
        button3 = KeyboardButton('%s Настройки' % emoji.emojize(':wrench:',use_aliases=True))

        #inline_kb_full.add(button1).add(button2).add(button3)
        inline_kb_full.row(button1,button2,)
        inline_kb_full.row(button3)

        return inline_kb_full
