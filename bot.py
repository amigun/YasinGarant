# Import libs
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData
from loguru import logger as log
import database_queries as dq
import config, messages, keyboards

# Enabled logging
log.add('resources/logfiles/logging.log', format='{time} {message}', rotation='1 week', compression='zip')
log.info('Launching the bot. Importing libraries, connect to DB and creating a log file')

# Init bot
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Init states
class States(StatesGroup):
    main_menu = State()

@dp.message_handler(commands=['start'], state='*')
async def start(msg: types.Message):
    start = dq.user_reg(user_id=msg.from_user.id)

    if start == 1:
        log.info(f'User {msg.from_user.id} was registred')

    user_status = dq.user_status(user_id=msg.from_user.id)

    if user_status == 0:
        await bot.send_message(msg.from_user.id, messages.get('greeting', first_name=msg.from_user.first_name), reply_markup=keyboards.main_menu__kb_user)
    if user_status == 1:
        await bot.send_message(msg.from_user.id, messages.get('greeting', first_name=msg.from_user.first_name), reply_markup=keyboards.main_menu__kb_arbitr)
    if user_status == 2:
        await bot.send_message(msg.from_user.id, messages.get('greeting', first_name=msg.from_user.first_name), reply_markup=keyboards.main_menu__kb_admin)
    await States.main_menu.set()

@dp.message_handler(commands=['help'], state='*')
async def help(msg: types.Message):
    await bot.send_message(msg.from_user.id, messages.get('help'))
    log.info(f'User {msg.from_user.id} send /help command')

@dp.message_handler(state=States.main_menu)
async def main_menu(msg: types.Message):
    if msg.text == "💬 Помощь":
        await bot.send_message(msg.from_user.id, messages.get('help'))
        log.info(f'User {msg.from_user.id} click on "Help" button')
    if msg.text == "👤 Мой профиль":
        user_info = dq.user_info(user_id=msg.from_user.id)

        await bot.send_message(msg.from_user.id, messages.get('account', user_info=user_info), parse_mode="MarkdownV2")
        log.info(f'User {msg.from_user.id} click on "My profile" button')

if __name__ == '__main__':
    executor.start_polling(dp)
