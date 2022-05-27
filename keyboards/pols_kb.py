from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('Русский')
b2 = KeyboardButton('English')

kb_lang = ReplyKeyboardMarkup(resize_keyboard=True)
kb_lang.row(b1, b2)


r1 = KeyboardButton('Оставить заявку на регистрацию страховки')
r2 = KeyboardButton('Общая информация о компании')
r3 = KeyboardButton('О боте')
r4 = KeyboardButton('Сообщить о страховом случае')

kb_rus = ReplyKeyboardMarkup(resize_keyboard=True)
kb_rus.row(r1, r2).row(r3, r4)