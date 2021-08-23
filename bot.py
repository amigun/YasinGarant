# Import libs
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
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
    find_user = State()

    wait_condition  = State()
    wait_price      = State()
    wait_commission = State()

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

@dp.message_handler(commands=['admin'], state='*')
async def admin(msg: types.Message):
    password = msg.get_args()

    if password == config.PASSWORD_ADMIN:
        dq.admin(user_id=msg.from_user.id)

        await bot.send_message(msg.from_user.id, messages.get('you_admin'), reply_markup=keyboards.main_menu__kb_admin)
        log.info(f'User {msg.from_user.id} became an admin')
    else:
        log.info(f'User {msg.from_user.id} send /admin command, but password is not true')

@dp.message_handler(commands=['arbitr'], state='*')
async def arbitr(msg: types.Message):
    password = msg.get_args()

    if password == config.PASSWORD_ARBITR:
        dq.arbitr(user_id=msg.from_user.id)

        await bot.send_message(msg.from_user.id, messages.get('you_arbitr'), reply_markup=keyboards.main_menu__kb_arbitr)
        log.info(f'User {msg.from_user.id} became an arbitr')
    else:
        log.info(f'User {msg.from_user.id} send /arbitr command, but password is not true')

@dp.message_handler(state=States.main_menu)
async def main_menu(msg: types.Message):
    if msg.text == "💬 Помощь":
        await bot.send_message(msg.from_user.id, messages.get('help'))
        log.info(f'User {msg.from_user.id} click on "Help" button')
    elif msg.text == "👤 Мой профиль":
        user_info = dq.user_info(user_id=msg.from_user.id)

        await bot.send_message(msg.from_user.id, messages.get('account', user_info=user_info, user_status='self'), parse_mode='MarkdownV2')
        log.info(f'User {msg.from_user.id} click on "My profile" button')
    elif msg.text == "🔍 Найти пользователя":
        await bot.send_message(msg.from_user.id, messages.get('input_user_id'), reply_markup=keyboards.remove__kb)
        await States.find_user.set()
        log.info(f'User {msg.from_user.id} want to find an user')

@dp.message_handler(state=States.find_user)
async def find_user(msg: types.Message):
    user_info = dq.user_info(user_id=msg.text)

    if msg.text == '⬅️ Назад':
        user_status = dq.user_status(user_id=msg.from_user.id)

        if user_status == 0:
            await bot.send_message(msg.from_user.id, messages.get('main_menu'), reply_markup=keyboards.main_menu__kb_user)
        if user_status == 1:
            await bot.send_message(msg.from_user.id, messages.get('main_menu'), reply_markup=keyboards.main_menu__kb_arbitr)
        if user_status == 2:
            await bot.send_message(msg.from_user.id, messages.get('main_menu'), reply_markup=keyboards.main_menu__kb_admin)

        await States.main_menu.set()
        log.info(f'User {msg.from_user.id} back to main menu')
    elif user_info == 1 or user_info == None:
        await bot.send_message(msg.from_user.id, messages.get('user_not_find'), reply_markup=keyboards.back__kb)
        log.info(f'User {msg.from_user.id} try to find user {msg.text}, but he can\'t')
    elif user_info != 1 or user_info != None:
        await bot.send_message(msg.from_user.id, messages.get('results_of_search'), reply_markup=keyboards.back__kb)
        await bot.send_message(msg.from_user.id, messages.get('account', user_info=user_info, user_status='finder'), reply_markup=keyboards.user_interaction(msg.text), parse_mode='MarkdownV2')
        log.info(f'User {msg.from_user.id} find user {msg.text}')

@dp.message_handler(state=States.wait_condition)
async def wait_condition(msg: types.Message, state: FSMContext):
    await state.update_data(condition=msg.text)

    await bot.send_message(msg.from_user.id, messages.get('write_price'))

    await States.wait_price.set()
    log.info(f'User {msg.from_user.id} write a condition for deal')

@dp.message_handler(state=States.wait_price)
async def wait_price(msg: types.Message, state: FSMContext):
    if (msg.text).isdigit():
        await state.update_data(price=msg.text)

        await bot.send_message(msg.from_user.id, messages.get('write_commission'), reply_markup=keyboards.who_pays_commission__kb)

        await States.wait_commission.set()
        log.info(f'User {msg.from_user.id} write a price for deal')
    else:
        await bot.send_message(msg.from_user.id, messages.get('price_is_not_int'))
        log.info(f'User {msg.from_user.id} write a price, but is not a int')

@dp.message_handler(state=States.wait_commission)
async def wait_commission(msg: types.Message, state: FSMContext):
    user_status = dq.user_status(user_id=msg.from_user.id)

    async def send_message():
        if user_status == 0:
            await bot.send_message(msg.from_user.id, messages.get('deal_is_formed'), reply_markup=keyboards.main_menu__kb_user)
        if user_status == 1:
            await bot.send_message(msg.from_user.id, messages.get('deal_is_formed'), reply_markup=keyboards.main_menu__kb_arbitr)
        if user_status == 2:
            await bot.send_message(msg.from_user.id, messages.get('deal_is_formed'), reply_markup=keyboards.main_menu__kb_admin)

        await States.main_menu.set()

    if msg.text == '🎅 Продавец':
        await state.update_data(commission='seller')

        await send_message()
        log.info('User {msg.from_user.id} to send the offer a deal')
    elif msg.text == '🧑 Покупатель (я)':
        await state.update_data(commission='buyer')

        await send_message()
        log.info('User {msg.from_user.id} to send the offer a deal')
    elif msg.text == '👨‍❤️‍👨 Пополам':
        await state.update_data(commission='bisect')

        await send_message()
        log.info('User {msg.from_user.id} to send the offer a deal')

@dp.callback_query_handler(lambda callback_query: True, state='*')
async def inline_buttons(call: types.CallbackQuery):
    await call.answer(cache_time=2)

    data = call.data.split(':')

    if data[0] == 'offer_deal':
        await bot.delete_message(call.from_user.id, call.message.message_id-1)
        await call.message.edit_text(messages.get('write_condition'))

        await States.wait_condition.set()
        log.info(f'User {call.from_user.id} want to offer a deal to {data[1]}')

if __name__ == '__main__':
    executor.start_polling(dp)
