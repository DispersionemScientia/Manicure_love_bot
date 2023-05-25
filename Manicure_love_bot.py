import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile

from keyboard_bot import kb, ikb

API_TOKEN = "5975881093:AAFdTKi8rdjSw4Pl5xP0leyR4KE2CjAL_oA"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


HELP_COMMAND = """
<b>/start</b> - <em>команда позволяет начать работу с ботом</em>
<b>/records</b> - <em>команда выводит все доступные записи на ближайшее время</em>
"""

START_COMMAND ="""
<em>Здравствуйте, я бот, который поможет вам записаться на маникюр!\n
Для этого вам помогут кнопочки снизу. Если ничего не понятно,то сходите к врач... тыкните кнопку 'Помощь❓'</em>
"""

PHOTO_WORK = ["./static/work1.jpg",
              "./static/work2.jpg",
              "./static/work3.jpg",
              "./static/work5.jpg",
              "./static/work6.jpg",
              "./static/work7.jpg",
              "./static/work8.jpg",
              "./static/work9.jpg"]

@dp.message_handler(Text(equals="Помощь❓"))
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode="HTML", reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=START_COMMAND,
                         parse_mode="HTML",
                         reply_markup=kb)
    await bot.send_photo(chat_id=message.chat.id,
                         photo="https://1.bp.blogspot.com/-oQ6R93ygb-Y/WJ36LeoBv0I/AAAAAAAAC7I/p7YCT5aK2mk-LG6z17Y2Ko2UvkX5dI1EwCLcB/s1600/42235076_l.jpg")
    # await bot.send_sticker(chat_id=message.chat.id,
    #                        sticker="CAACAgIAAxkBAAEIvzVkSi-6P9QwhSzexnl7Hv9zRBPdMAACCAADwDZPE29sJgveGptpLwQ")
    await message.delete()

@dp.message_handler(Text(equals="Записи✍️"))
async def records_command(message: types.Message):
    response = requests.get(url='http://127.0.0.1:8000/api/v1/recordlist/').json()
    for record in response:
        await message.answer(f"Дата: {record['date']}\nВремя: {record['time']}",
                             parse_mode="HTML",
                             reply_markup=ikb)
    await message.delete()

@dp.message_handler(Text(equals="Прайс💅"))
async def price_command(message: types.Message):
    photo = open("./static/price.jpg", "rb")
    await bot.send_photo(chat_id=message.chat.id,
                         photo=photo)
    await message.delete()

@dp.message_handler(Text(equals="Мои работы❤️"))
async def price_command(message: types.Message):
    for photo in PHOTO_WORK:
        photo_open = open(photo, "rb")
        await bot.send_photo(chat_id=message.chat.id,
                         photo=photo_open)
    await message.delete()

# @dp.message_handler(Text(equals='Веб версия'))
# async def web_version(message: types.Message):
#     await message.answer('Также вы можете перейти на сайт в браузере по следующему адресу: http://127.0.0.1:8000/',
#                          reply_markup=kb)


if __name__ == '__main__':
    executor.start_polling(dp)
