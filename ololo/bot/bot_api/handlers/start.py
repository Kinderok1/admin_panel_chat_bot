from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram import types
import os, sys
import django
from attr import filters
from PIL import Image


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
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    # find = Items.objects.all()
    #
    # message_reply = "Привет!\nМеня зовут FindBot!\n%s" % find
    # await message.reply(message_reply, parse_mode=types.ParseMode.MARKDOWN)

    member_name = m.from_user.full_name
    member_id = m.from_user.id

    new_member = Members(name=member_name, id_t=member_id)
    new_member.save()

    user_photo = await bot.get_user_profile_photos(m.from_user.id, offset=0)
    #await bot.send_photo(message.from_user.id, photo=user_photo.photos[0][-1].file_id)
    try:
        file = await bot.download_file_by_id(user_photo.photos[0][-1].file_id)
    except:
        'no photo'

    from io import BytesIO
    from django.core.files.uploadedfile import InMemoryUploadedFile
    from django.core.files.base import ContentFile
    from django.conf import settings

    IMAGE_WIDTH = 100
    IMAGE_HEIGHT = 100

    def resize_image(image_field, width=IMAGE_WIDTH, height=IMAGE_HEIGHT, name=None):
        """
        Resizes an image from a Model.ImageField and returns a new image as a ContentFile
        """
        img = Image.open(file)


        if img.size[0] > width or img.size[1] > height:
            new_img = img.resize((width, height))

        buffer = BytesIO()
        new_img.save(fp=buffer, format='JPEG')
        return ContentFile(buffer.getvalue())

    # assuming your Model instance is called `instance`
    image_field = Members.objects.get(name=member_name)

    img_name = 'my_image.jpg'
    img_path = settings.MEDIA_ROOT + img_name

    pillow_image = resize_image(
        image_field,
        width=IMAGE_WIDTH,
        height=IMAGE_HEIGHT,
        name=img_path)

    image_field.image.save(img_name, InMemoryUploadedFile(
        pillow_image,  # file
        None,  # field_name
        img_name,  # file name
        'image/jpeg',  # content_type
        pillow_image.tell,  # size
        None)  # content_type_extra
                     )
    #
    #
    #
    #
    # product = Members.objects.get(name='Pavel')
    # product.name = m.from_user.full_name
    # product.id_t = m.from_user.id
    # product.save()
    # product = Members.objects.get(name='Pavel')
    #

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
