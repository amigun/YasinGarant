from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

remove__kb = ReplyKeyboardRemove()
back__kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('⬅️ Назад'))

main_menu__button_1 = KeyboardButton('🔍 Найти пользователя')
main_menu__button_2 = KeyboardButton('👤 Мой профиль')
main_menu__button_3 = KeyboardButton('💬 Помощь')
main_menu__button_4 = KeyboardButton('👑 Панель администратора')
main_menu__button_5 = KeyboardButton('👨‍⚖️ Панель арбитра')

main_menu__kb_user   = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu__button_1, main_menu__button_2, main_menu__button_3)
main_menu__kb_admin  = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu__button_1, main_menu__button_2, main_menu__button_3, main_menu__button_4)
main_menu__kb_arbitr = ReplyKeyboardMarkup(resize_keyboard=True).add(main_menu__button_1, main_menu__button_2, main_menu__button_3, main_menu__button_5)

who_pays_commission__button_1 = KeyboardButton('🎅 Продавец')
who_pays_commission__button_2 = KeyboardButton('🧑 Покупатель (я)')
who_pays_commission__button_3 = KeyboardButton('👨‍❤️‍👨 Пополам')

who_pays_commission__kb = ReplyKeyboardMarkup(resize_keyboard=True).add(who_pays_commission__button_1, who_pays_commission__button_2, who_pays_commission__button_3)

def user_interaction(id_to):
    offer_deal__cb = CallbackData('offer_deal', 'id_to')

    user_interaction__buttons = [
            InlineKeyboardButton(text='🤝 Предложить сделку', callback_data=offer_deal__cb.new(id_to=id_to))
        ]

    user_interaction__kb = InlineKeyboardMarkup().add(*user_interaction__buttons)

    return user_interaction__kb
