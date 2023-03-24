import telebot
from parsing import about_names

token = '6008974194:AAGBg1YyvQ16a-HEn5Jtfyhh_vxNOKUKv5I'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет, о каком имени тебе рассказать?')
    bot.register_next_step_handler(message, text_to_message)



@bot.message_handler(content_types=['text'])
def text_to_message(message):
    bot.send_message(message.chat.id, about_names(message.text))






bot.polling(none_stop=True)