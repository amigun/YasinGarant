def get(msg, **kwargs):
    if msg == 'greeting':
        message = f'🙌 Добро пожаловать, {list(kwargs.items())[0][1]}!\n\nВведи команду /help или нажми соответствующую кнопку, чтобы посмотреть ответы на частозадаваемые вопросы или задать свой вопрос.\nВведи команду /start если бот завис или работает как-то некорректно'
        return message
    elif msg == 'help':
        message = '🌸 По любым вопросам писать сюда: @yasin_vegasE'
        return message
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

        return message
    elif msg == 'you_admin':
        message = f'👑 Вы теперь администратор!'
        return message
    elif msg == 'you_arbitr':
        message = '🧑‍⚖️ Вы теперь арбитр!'
        return message
    elif msg == 'input_user_id':
        message = '🆔 Введите ID пользователя:'
        return message
    elif msg == 'user_not_find':
        message = '☹️ Пользователь не найден, попробуйте ввести ID снова:'
        return message
    elif msg == 'main_menu':
        message = '✨ Вы в главном меню!'
        return message
