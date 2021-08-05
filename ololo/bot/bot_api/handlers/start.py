from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import types
import os, sys
import django
from attr import filters
from PIL import Image


from ..keyboards.keyboards import DefaultConstructor

django.setup()

from aiogram.dispatcher.filters.state import State, StatesGroup
from ...models import Items, Notifications, Members, Messages, Type
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

class CallBackData():
    callback_data = {}
# !!!Need refactoring: callback functions is repeating
async def process_callback_kb1btn2(callback_query: types.CallbackQuery):
    us = Members.objects.filter(id_t=callback_query.from_user.id).update(user_state='В разделе "Символизм"')
    try:
        search_itm = Type.objects.get(name='Символизм')
        search = Items.objects.filter(type=search_itm.pk)  # HARDCODE

        #troubles with send descr.probably reason is probel:)
        for e in search:
            pay_markup = InlineKeyboardMarkup()
            CallBackData.callback_data[e.caption]={'desc': e.description, 'cost': str(e.cost), 'link': e.link}
            callback_data_for_buy_button = 'Купить<' + e.caption
            pay_markup.insert(
                InlineKeyboardButton(
                    "Купить", callback_data=callback_data_for_buy_button
                )
            )
            caption = '<b>%s</b> \n %s' % (e.caption, e.description)
            photo = types.InputFile(e.image.path)
            await bot.send_photo(callback_query.from_user.id, photo, caption, reply_markup=pay_markup)



    except:
        await bot.send_message(callback_query.from_user.id, 'Товаров в этой категории нет')


async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    user_state = Members.objects.filter(id_t=callback_query.from_user.id).update(user_state='В разделе "Поп-арт"')
    try:
        search_itm = Type.objects.get(name='Поп-арт')
        search = Items.objects.filter(type=search_itm.pk)
        search[0].caption
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
    except:
        await bot.send_message(callback_query.from_user.id, 'Товаров в этой категории нет')


async def start_command(m: Message):
    """
    Responds to /start.
    тут будет первичная запись в базу!
    """

    # member_name = m.from_user.full_name
    # member_id = m.from_user.id
    # link_tg = m.from_user.url

    # new_member = Members(name=member_name, id_t=member_id, link_id=link_tg,)
    # new_member.save()
    #
    # user_photo = await bot.get_user_profile_photos(m.from_user.id, offset=0)
    # #await bot.send_photo(message.from_user.id, photo=user_photo.photos[0][-1].file_id)
    # try:
    #     file = await bot.download_file_by_id(user_photo.photos[0][-1].file_id)
    # except:
    #     'no photo'
    #
    # from io import BytesIO
    # from django.core.files.uploadedfile import InMemoryUploadedFile
    # from django.core.files.base import ContentFile
    # from django.conf import settings
    #
    # IMAGE_WIDTH = 100
    # IMAGE_HEIGHT = 100
    #
    # def resize_image(image_field, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, name=None):
    #     """
    #     Resizes an image from a Model.ImageField and returns a new image as a ContentFile
    #     """
    #     img = Image.open(file)
    #
    #
    #     if img.size[0] > width or img.size[1] > height:
    #         new_img = img.resize((width, height))
    #
    #     buffer = BytesIO()
    #     new_img.save(fp=buffer, format='JPEG')
    #     return ContentFile(buffer.getvalue())
    #
    # # assuming your Model instance is called `instance`
    # image_field = Members.objects.get(name=member_name)
    #
    # img_name = 'my_image.jpg'
    # img_path = settings.MEDIA_ROOT + img_name
    #
    # pillow_image = resize_image(
    #     image_field,
    #     width=IMAGE_WIDTH,
    #     height=IMAGE_HEIGHT,
    #     name=img_path)
    #
    # image_field.image.save(img_name, InMemoryUploadedFile(
    #     pillow_image,  # file
    #     None,  # field_name
    #     img_name,  # file name
    #     'image/jpeg',  # content_type
    #     pillow_image.tell,  # size
    #     None)  # content_type_extra
    #                  )

    keyboard = DefaultConstructor.create_main_kb()

    await m.reply("Добро пожаловать в галерею!", reply_markup=keyboard)


async def menu(m: types.Message):
    user_state = Members.objects.filter(id_t=m.from_user.id).update(user_state='В разделе \'Каталог\'')
    keyboard = DefaultConstructor.create_kb()
    await m.reply('Все наши картины разбиты по стилям живописи', reply_markup=keyboard)


async def menu_items(m: types.Message):
    pass
    # меню должно быть колбэкное
    # но для видео я эту логику реализовывать не буду!


async def notice(m: types.Message):
    id_t = m.from_user.id
    user_name = m.from_user.full_name
    notification = Notifications.objects.create(from_user_id=id_t, from_user_name=user_name)
    member = Members.objects.get(id_t=id_t)
    Messages.objects.create(owner=member, from_user_msg=m.text)

# хандлер корзины
# хандлер оплаты
#    user_state = Members.objects.filter(id_t=m.from_user.id).update(user_state='В разделе меню')
#    user_state = Members.objects.filter(id_t=m.from_user.id).update(user_state='В разделе меню')
