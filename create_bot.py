from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot('5358118207:AAFGQmuhr_NwHOsMyMBTgSXbAz70hNvjQE4')
dp = Dispatcher(bot, storage=storage)