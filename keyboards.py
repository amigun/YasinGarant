from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu__button_1 = KeyboardButton('🔍 Найти пользователя')
main_menu__button_2 = KeyboardButton('👤 Мой профиль')
main_menu__button_3 = KeyboardButton('💬 Помощь')
main_menu__button_4 = KeyboardButton('👑 Панель администратора')
main_menu__button_5 = KeyboardButton('👨‍⚖️ Панель арбитра')

main_menu__kb_user = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu__button_1, main_menu__button_2, main_menu__button_3)
main_menu__kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu__button_1, main_menu__button_2, main_menu__button_3, main_menu__button_4)
main_menu__kb_arbitr = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu__button_1, main_menu__button_2, main_menu__button_3, main_menu__button_5)
