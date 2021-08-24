from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
import database_queries as dq

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

def list_of_offers_of_deals_pending(id_to, current_page):
    offer_deal__cb = CallbackData('deal_offer_pending', 'id_deal')
    pages__cb      = CallbackData('goto', 'page')

    list_of_offers = dq.list_of_offers_of_deals_pending(seller=id_to)
    list_of_offers = [list_of_offers[i:i + 10] for i in range(0, len(list_of_offers), 10)]

    pages = []

    for page in list_of_offers:
        page_of_button = []

        for button in page:
            page_of_button.append([InlineKeyboardButton(text='#'+str(button[0]), callback_data=offer_deal__cb.new(id_deal=button[0]))])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[button for button in page_of_button])

        if list_of_offers.index(page) == 0:
            pages.append(InlineKeyboardMarkup(inline_keyboard=[button for button in page_of_button]).add(InlineKeyboardButton(text='➡️', callback_data=pages__cb.new(page=list_of_offers.index(page)+1))))
        elif list_of_offers.index(page) == len(list_of_offers)-1:
            pages.append(InlineKeyboardMarkup(inline_keyboard=[button for button in page_of_button]).add(InlineKeyboardButton(text='⬅️', callback_data=pages__cb.new(page=list_of_offers.index(page)-1))))
        elif list_of_offers.index(page) != 0:
            pages.append(InlineKeyboardMarkup(inline_keyboard=[button for button in page_of_button]).add(InlineKeyboardButton(text='⬅️', callback_data=pages__cb.new(page=list_of_offers.index(page)-1)), InlineKeyboardButton(text='➡️', callback_data=pages__cb.new(page=list_of_offers.index(page)+1))))

    return pages[current_page]
