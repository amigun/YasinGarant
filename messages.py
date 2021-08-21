def get(msg, **kwargs):
    if msg == 'greeting':
        message = f'🙌 Добро пожаловать, {list(kwargs.items())[0][1]}!\n\nВведи команду /help или нажми соответствующую кнопку, чтобы посмотреть ответы на частозадаваемые вопросы или задать свой вопрос.\nВведи команду /start если бот завис или работает как-то некорректно'
        return message
    elif msg == 'help':
        message = '🌸 По любым вопросам писать сюда: @yasin_vegasE'
        return message
    elif msg == 'account':
        user_info = kwargs['user_info']
        status = user_info[1]
        if status == 0:
            status = '👤 *Статус:* Пользователь'
        elif status == 1:
            status = '🧑‍⚖️ *Статус:* Арбитр'
        elif status == 2:
            status = '👑 *Статус:* Администратор'
        message = f'👁 *Профиль:* {user_info[0]}\n{status}\n💰 *Баланс:* {user_info[2]} руб\.\n❄️ *Замороженный баланс:* {user_info[3]} руб\.\n💬 *Отзывы:* {user_info[4]} шт\.\n\n🤝 *Продаж:* {user_info[5]} шт\.\n🛒 *Покупок:* {user_info[6]} шт\.\n💸 *Сумма продаж:* {user_info[7]} руб\.\n💵 *Сумма покупок:* {user_info[8]} руб\.'
        return message
