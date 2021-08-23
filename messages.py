def get(msg, **kwargs):
    message = ''

    if msg == 'greeting':
        message = f'🙌 Добро пожаловать, {list(kwargs.items())[0][1]}!\n\nВведи команду /help или нажми соответствующую кнопку, чтобы посмотреть ответы на частозадаваемые вопросы или задать свой вопрос.\nВведи команду /start если бот завис или работает как-то некорректно'
    elif msg == 'help':
        message = '🌸 По любым вопросам писать сюда: @yasin_vegasE'
    elif msg == 'account':
        user_info = kwargs['user_info']
        user_status = kwargs['user_status']
        status = user_info[1]
        if status == 0:
            status = '👤 *Статус:* Пользователь'
        elif status == 1:
            status = '🧑‍⚖️ *Статус:* Арбитр'
        elif status == 2:
            status = '👑 *Статус:* Администратор'

        if user_status == 'self':
            message = f'👁 *Профиль:* {user_info[0]}\n{status}\n💰 *Баланс:* {user_info[2]} руб\.\n❄️ *Замороженный баланс:* {user_info[3]} руб\.\n💬 *Отзывы:* {user_info[4]} шт\.\n\n🤝 *Продаж:* {user_info[5]} шт\.\n🛒 *Покупок:* {user_info[6]} шт\.\n💸 *Сумма продаж:* {user_info[7]} руб\.\n💵 *Сумма покупок:* {user_info[8]} руб\.'
        elif user_status == 'finder':
            message = f'👁 *Профиль:* {user_info[0]}\n{status}\n💬 *Отзывы:* {user_info[4]} шт\.\n\n🤝 *Продаж:* {user_info[5]} шт\.\n🛒 *Покупок:* {user_info[6]} шт\.\n💸 *Сумма продаж:* {user_info[7]} руб\.\n💵 *Сумма покупок:* {user_info[8]} руб\.'

    elif msg == 'you_admin':
        message = f'👑 Вы теперь администратор!'
    elif msg == 'you_arbitr':
        message = '🧑‍⚖️ Вы теперь арбитр!'
    elif msg == 'input_user_id':
        message = '🆔 Введите ID пользователя:'
    elif msg == 'user_not_find':
        message = '☹️ Пользователь не найден, попробуйте ввести ID снова:'
    elif msg == 'main_menu':
        message = '✨ Вы в главном меню!'
    elif msg == 'results_of_search':
        message = '👇 Результаты поиска:'
    elif msg == 'write_condition':
        message = '➡️ Полностью напиши условия сделки:'
    elif msg == 'write_price':
        message = '➡️ Укажите сумму сделки (учтите, бот возьмет комиссию 5%):'
    elif msg == 'write_commission':
        message = '➡️ Укажите, кто возьмет на себя расходы комиссии:'
    elif msg == 'price_is_not_int':
        message = '⚠️ Введенная вами сумма не является числом! Попробуйте снова'
    elif msg == 'deal_is_formed':
        message = '✅ Сделка успешно сформирована и отправлена продавцу на подтверждение!'

    return message
