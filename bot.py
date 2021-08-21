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
import config, messages

# Enabled logging
log.add('resources/logfiles/logging.log', format='{time} {message}', rotation='1 week', compression='zip')
log.info('Launching the bot. Importing libraries, connect to DB and creating a log file')

# Init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'], state='*')
async def start(msg: types.Message):
    await bot.send_message(msg.from_user.id, messages.get('greeting', first_name=msg.from_user.first_name))

    start = dq.user_reg(user_id=msg.from_user.id)

    if start == 1:
        log.info(f'User {msg.from_user.id} was registred')

@dp.message_handler(commands=['help'], state='*')
async def help(msg: types.Message):
    await bot.send_message(msg.from_user.id, messages.get('help'))

if __name__ == '__main__':
    executor.start_polling(dp)
