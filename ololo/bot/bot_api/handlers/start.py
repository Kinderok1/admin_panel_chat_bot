from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'ololo.settings'
django.setup()
from ...models import Items

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

    find = Items.objects.all()

    message_reply = "Привет!\nМеня зовут FindBot!\n%s" % find

    await m.reply(message_reply)

    #получить id аватарки
    #async def test(message: types.Message):
    #user_photo = await bot.get_user_profile_photos(message.from_user.id, offset=0)
    #await bot.send_photo(message.from_user.id, photo=user_photo.photos[0][-1].file_id)
    #
    #file = await bot.download_file_by_id(message.photo[-1].file_id)

    #img = Image.open(file)
    #
    #
    #
    #
    #
    #