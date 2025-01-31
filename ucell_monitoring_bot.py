import telebot
from telebot import types

bot = telebot.TeleBot('7918506920:AAFUyc3GoP3TP7MBO3TQS0eFv1yz6tlRPQg')

sai_alerts = {
    'alert1': {'name': 'UserPackagesIntegerOverflow',
               'description': '✨ <b>alertname:</b> = UserPackagesIntegerOverflow \nenvironment = prod \ngroup = business-metrics \ninstance = mon.iti.domain:9399\njob = sql-exporter\nseverity = critical\nAnnotations\nsummary = More than 1 integer overflow in user_packages\n _______________\n<b>Причина: биллинг возвращает NaN в квотах</b>.'},
    'alert2': {'name': 'HostClockNotSynchronising',
               'description': '✨ <b>alertname:</b> = HostClockNotSynchronising\nenvironment = prod \ninstance = app-5.prod:9100\njob = node_exporter\nseverity = warning\nAnnotations\ndescription = Clock not synchronising. Ensure NTP is\nconfigured on this host. VALUE = 0 LABELS =\nmap[environment:prod instance:app-5.prod:9100\njob:node_exporter]\nsummary = Host clock not synchronising (instance app-5.prod:9100)\n_______________________\n<b>Необходимое решение: кластер VMware сделать без оверпровизионинга</b>..'},
    'alert3': {'name': 'HighCountOfErrorsOnEventProcessor',
               'description': '✨ <b>alertname:</b> = HighCountOfErrorsOnEventProcessor\naction = failed_to_find_appmetrica_device_id_in_clickhouse\ngroup = eventer\nseverity = critical\nAnnotations\nsummary = High count of errors (424.8) on event-processor\nmap[action:failed_to_find_appmetrica_device_id_in_clickhouse].'},
    'alert4': {'name': 'UserPackagesIntegerOverflow',
               'description': '✨ <b>alertname:</b> = UserPackagesIntegerOverflow\nenvironment = prod\ngroup = business-metrics\ninstance = mon.iti.domain:9399\njob = sql-exporter\nseverity = critical\nAnnotations\nsummary = More than 1 integer overflow in user_packages.'},
    'alert5': {'name': 'PromtailIsDown',
               'description': '✨ <b>alertname:</b> = PromtailIsDown\nenvironment = prod\ninstance = app-1.prod:9080\njob = promtail\nseverity = moderate\nAnnotations\ndescription = app-1.prod:9080 has been down more than 60s (job promtail).\ntitle = app-1.prod:9080 is down\n_________________\nСетевая/миграция виртуалки Vmware.'},
    'alert6': {'name': 'ApiV1.14SimActivationRegistrationPost400Low',
               'description': '✨ <b>alertname:</b> = ApiV1.14SimActivationRegistrationPost400Low\nenv = gateways\nfilename = /var/log/nginx/api-ma.ucell.uz-access.log\nhostname = gw-1.prod\njob = nginx-access\nmessage = 400 errors are more than 20 per minute on url:\n/api/v1.14/sim/activation/registration\nseverity = low\n.'},
    'alert7': {'name': 'ProcessExporterIsDown',
               'description': '✨ <b>alertname:</b> = ProcessExporterIsDown\nenvironment = prod\ninstance = db-2.prod:9256\njob = process_exporter\nseverity = moderate\nAnnotations\ndescription = db-2.prod:9256 has been down more than 60s (job process_exporter).\ntitle = db-2.prod:9256 is down\n \n.'},
    'alert8': {'name': 'Ошибки входа в SAI',
               'description': '✨ <b>alertname:</b> Описание для алерта 8, связанное с ошибками входа в систему SAI.'},
    'alert9': {'name': 'Проблемы с базой данных SAI',
               'description': '✨ <b>alertname:</b> Описание для алерта 9, связанное с проблемами базы данных в SAI.'},
    'alert10': {'name': 'Завершение работы в SAI',
                'description': '✨ <b>alertname:</b> Описание для алерта 10, связанное с завершением работы важного сервиса в SAI.'},
}

vas_alerts = {
    'alert1': {'name': 'Проблемы с услугами VAS',
               'description': '✨ <b>Алерт 1:</b> Этот алерт сообщает о проблемах с услугами VAS. Описание проблемы и действия, которые нужно предпринять.'},
    'alert2': {'name': 'Сбои в системах VAS',
               'description': '✨ <b>Алерт 2:</b> Этот алерт сообщает о сбоях в системах VAS. Требуется вмешательство для восстановления работы.'},
    'alert3': {'name': 'Потеря данных в VAS',
               'description': '✨ <b>Алерт 3:</b> Этот алерт сообщает о потере данных в сервисах VAS. Необходимо провести анализ и восстановление.'},
    'alert4': {'name': 'Проблемы с подключением VAS',
               'description': '✨ <b>Алерт 4:</b> Описание для алерта 4, связанное с проблемами с подключением к сервисам VAS.'},
    'alert5': {'name': 'Безопасность в VAS',
               'description': '✨ <b>Алерт 5:</b> Описание для алерта 5, связанное с безопасностью в системе VAS.'},
    'alert6': {'name': 'Риски с обновлениями VAS',
               'description': '✨ <b>Алерт 6:</b> Описание для алерта 6, указывающее на риски с обновлениями системы VAS.'},
    'alert7': {'name': 'Ошибки авторизации в VAS',
               'description': '✨ <b>Алерт 7:</b> Описание для алерта 7, связанное с ошибками авторизации в VAS.'},
    'alert8': {'name': 'Технические проблемы VAS',
               'description': '✨ <b>Алерт 8:</b> Описание для алерта 8, связанное с техническими проблемами в VAS.'},
    'alert9': {'name': 'Проблемы с производительностью VAS',
               'description': '✨ <b>Алерт 9:</b> Описание для алерта 9, связанное с производительностью в VAS.'},
    'alert10': {'name': 'Завершение работы в VAS',
                'description': '✨ <b>Алерт 10:</b> Описание для алерта 10, связанное с завершением работы важного сервиса в VAS.'},
}

def create_alert_buttons(alerts, callback_prefix):
    markup = types.InlineKeyboardMarkup()
    for alert_key, alert_value in alerts.items():
        alert_button = types.InlineKeyboardButton(alert_value['name'], callback_data=f'{callback_prefix}_{alert_key}')
        markup.add(alert_button)
    back_button = types.InlineKeyboardButton('⬅️ Назад', callback_data='main_menu')
    markup.add(back_button)
    return markup


@bot.callback_query_handler(func=lambda call: call.data == 'search_alerts')
def search_alerts(call):
    msg = bot.send_message(call.message.chat.id, "Введите запрос для поиска по алертам:")
    bot.register_next_step_handler(msg, handle_search_query)

def handle_search_query(message):
    query = message.text.lower()
    results = []

    for alert_key, alert_value in sai_alerts.items():
        if query in alert_value['name'].lower() or query in alert_value['description'].lower():
            results.append(f"sai_alert_{alert_key}")

    for alert_key, alert_value in vas_alerts.items():
        if query in alert_value['name'].lower() or query in alert_value['description'].lower():
            results.append(f"vas_alert_{alert_key}")

    if results:
        markup = types.InlineKeyboardMarkup()
        for result in results:
            alert_button = types.InlineKeyboardButton(result, callback_data=result)
            markup.add(alert_button)

        bot.send_message(
            message.chat.id,
            "Вот результаты поиска:",
            reply_markup=markup
        )
    else:
        bot.send_message(
            message.chat.id,
            "Ничего не найдено. Попробуйте ввести другой запрос."
        )

@bot.message_handler(commands=['start', 'main'])
def main_menu(message):
    markup = types.InlineKeyboardMarkup()

    sai_alerts_button = types.InlineKeyboardButton('Алерты отдела SAI', callback_data='sai_alerts')
    vas_alerts_button = types.InlineKeyboardButton('Алерты отдела VAS', callback_data='vas_alerts')
    search_alerts_button = types.InlineKeyboardButton('🔍 Поиск по алертам', callback_data='search_alerts')

    system_info_button = types.InlineKeyboardButton('🖥 Информация о системе', callback_data='system_info')
    tech_support_button = types.InlineKeyboardButton('📞 Техническая поддержка', callback_data='tech_support')
    stats_button = types.InlineKeyboardButton('📊 Статистика по алертам', callback_data='alert_stats')

    markup.add(sai_alerts_button, vas_alerts_button, search_alerts_button)
    markup.add(system_info_button, tech_support_button, stats_button)

    bot.send_message(
        message.chat.id,
        f'👋 <b>Привет {message.from_user.first_name} {message.from_user.last_name}, тебя приветствует бот с базой всех алертов компании Ucell!</b>\n\n'
        'Выберите один из разделов ниже:',
        parse_mode='HTML',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'sai_alerts')
def show_sai_alerts(call):
    markup = create_alert_buttons(sai_alerts, 'sai_alert')

    bot.edit_message_text(
        'Выберите алерт для отдела SAI:',
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode='HTML',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('sai_alert_'))
def show_sai_alert_details(call):
    alert_key = call.data.split('_')[2]
    alert_details = sai_alerts[alert_key]
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('⬅️ Назад', callback_data='sai_alerts')
    markup.add(back_button)

    bot.edit_message_text(
        alert_details['description'],
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode='HTML',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'vas_alerts')
def show_vas_alerts(call):
    markup = create_alert_buttons(vas_alerts, 'vas_alert')

    bot.edit_message_text(
        'Выберите алерт для отдела VAS:',
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode='HTML',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith('vas_alert_'))
def show_vas_alert_details(call):
    alert_key = call.data.split('_')[2]
    alert_details = vas_alerts[alert_key]
    markup = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton('⬅️ Назад', callback_data='vas_alerts')
    markup.add(back_button)

    bot.edit_message_text(
        alert_details['description'],
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode='HTML',
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'main_menu')
def back_to_main_menu(call):
    markup = types.InlineKeyboardMarkup()

    sai_alerts_button = types.InlineKeyboardButton('Алерты отдела SAI', callback_data='sai_alerts')
    vas_alerts_button = types.InlineKeyboardButton('Алерты отдела VAS', callback_data='vas_alerts')
    search_alerts_button = types.InlineKeyboardButton('🔍 Поиск по алертам', callback_data='search_alerts')

    system_info_button = types.InlineKeyboardButton('🖥 Информация о системе', callback_data='system_info')
    tech_support_button = types.InlineKeyboardButton('📞 Техническая поддержка', callback_data='tech_support')
    stats_button = types.InlineKeyboardButton('📊 Статистика по алертам', callback_data='alert_stats')

    markup.add(sai_alerts_button, vas_alerts_button, search_alerts_button)
    markup.add(system_info_button, tech_support_button, stats_button)

    bot.edit_message_text(
        f'👋 <b>Привет {call.from_user.first_name} {call.from_user.last_name}, тебя приветствует бот с базой всех алертов компании Ucell!</b>\n\n'
        'Выберите один из разделов ниже:',
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        parse_mode='HTML',
        reply_markup=markup
    )

bot.polling(none_stop=True)