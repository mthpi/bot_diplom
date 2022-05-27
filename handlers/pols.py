from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards.pols_kb import *
from asyncio import sleep


# @dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
	await bot.send_message(message.from_user.id, 'Здравствуйте. Выберите язык:', reply_markup=kb_lang)

# @dp.message_handler(text='Русский')
async def rus_kb(message : types.Message):
	await bot.send_message(message.from_user.id, 'Выберите:', reply_markup=kb_rus)

# @dp.message_handler(text='Общая информация о компании')
async def info(message : types.Message):
	await bot.send_message(message.from_user.id, 'Здесь надо написать информацию о компании OMIR', reply_markup=types.ReplyKeyboardRemove())
	await sleep(1)
	await bot.send_message(message.from_user.id, 'Выберите:', reply_markup=kb_rus)



def register_handlers_client(dp : Dispatcher):
	dp.register_message_handler(commands_start, commands=['start', 'help'])
	dp.register_message_handler(rus_kb, text='Русский')
	dp.register_message_handler(info, text='Общая информация о компании')