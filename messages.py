def get(msg, **kwargs):
    if msg == "greeting":
        message = f'🙌 Добро пожаловать, {list(kwargs.items())[0][1]}!\n\nВведи команду /help или нажми соответствующую кнопку, чтобы посмотреть ответы на частозадаваемые вопросы или задать свой вопрос.\nВведи команду /start если бот завис или работает как-то некорректно'
        return message
    elif msg == 'help':
        message = '🌸 По любым вопросам писать сюда: @yasin_vegasE'
        return message
