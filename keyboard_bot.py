from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton('Помощь❓')
b2 = KeyboardButton('Записи✍️')
b3 = KeyboardButton('Прайс💅')
b4 = KeyboardButton('Мои работы❤️')
# b5 = KeyboardButton('Веб версия', web_app=WebAppInfo(url='http://127.0.0.1:8000/')) # веб версия в телеграме
kb.add(b1, b2).add(b3, b4)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='Записаться',
                           url='http://127.0.0.1:8000/records/')
ikb.add(ib1)

