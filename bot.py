# Import libs
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from loguru import logger as log
import database_queries as dq
import sqlite3
import config, messages

# Enabled logging
log.add('resources/logfiles/logging.log', format='{time} {message}', rotation='1 week', compression='zip')
log.info('Launching the bot. Importing libraries and creating a log file')

# Init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state='*')
async def start(msg: types.Message):
    print(f'\nText: {messages.get("greeting", first_name=msg.from_user.first_name)}')
    await bot.send_message(msg.from_user.id, messages.get('greeting', first_name=msg.from_user.first_name))

    dq.user_reg(user_id=msg.from_user.id)

if __name__ == '__main__':
    executor.start_polling(dp)
