import telebot

token = '6106915773:AAEl6DhYn4un_FGZEdzIyPnHjWlO4SUXC0A'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Ритм')
    item2 = telebot.types.KeyboardButton('Степень')
    item3 = telebot.types.KeyboardButton('Арифметика')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, как жизнь?', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == 'отлично':
        bot.send_message(message.chat.id, 'Я рад за тебя')
    elif message.text.lower() == 'плохо':
        bot.send_message(message.chat.id, 'Жизнь - это синусоида...')
    elif message.text.lower() == 'ритм':
        bot.send_message(message.chat.id, 'Введите вашу фразу')
        bot.register_next_step_handler(message, rhythm)
    elif message.text.lower() == 'арифметика':
        bot.send_message(message.chat.id, 'Введите формулу')
        bot.register_next_step_handler(message, formula)
    elif message.text.lower() == 'степень':
        bot.send_message(message.chat.id, 'Введите число и степень через пробел')
        bot.register_next_step_handler(message, power)


    else:
        bot.send_message(message.chat.id, 'Не знаю, чего вы хотите, ткните в другую кнопку)')

@bot.message_handler(content_types=['text'])
def vinny(phrase):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    new_list = []
    count = 0

    for i in range(len(phrase)):
        if phrase[i].lower() != ' ':
            if phrase[i].lower() in vowel_list:
                count += 1
        else:
            new_list.append(count)
            count = 0
    new_list.append(count)

    for el in range(len(new_list) - 1):
        if new_list[el] != new_list[el + 1]:
            return 'Ритм присутствует'
    return 'Ритм отсутствует :)'


@bot.message_handler(content_types=['text'])
def rhythm(message):
    bot.send_message(message.chat.id, vinny(message.text))

@bot.message_handler(content_types=['text'])
def str_to_formula(some_str):
    res = 0
    i = 0
    flag = True
    while flag:
        if some_str[i] == '+':
            res = res + int(some_str[i - 1]) + int(some_str[i + 1])
            flag = False
        elif some_str[i] == '-':
            res = res + int(some_str[i - 1]) - int(some_str[i + 1])
            flag = False
        i += 1
    for i in range(i, len(some_str)):
        if some_str[i] == '+':
            res = res + int(some_str[i + 1])
        elif some_str[i] == '-':
            res = res - int(some_str[i + 1])
    return res

@bot.message_handler(content_types=['text'])
def formula(message):
    bot.send_message(message.chat.id, str_to_formula(message.text))

@bot.message_handler(content_types=['text'])
def to_the_power_of(message):
    some_str = ''
    some_list = []
    for i in range(len(message)):
        if message[i] != ' ':
            some_str += message[i]
        else:
            some_list.append(some_str)
            some_str = ''
    # some_list.append(some_str)
    a = int(some_list[0])
    b = int(some_str)

    res = 1
    if b == 0:
        return 1
    else:
        while b >= 1:
            res = res * a
            b -= 1
    return res

@bot.message_handler(content_types=['text'])
def power(message):
    bot.send_message(message.chat.id, to_the_power_of(message.text))





bot.polling(none_stop=True)