import telebot
from telebot import types

token = '5991662158:AAHyhK9W5XWEKz_hbDnWuHLn9KQuGGfVgmE'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'admin'])
def cmd(message):
    pass


@bot.message_handler(content_types=['text'])
def text(message):
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    pass


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.reply_to(message, text='Добро пожаловать 😈 в наш чат!')


@bot.message_handler(content_types=['left_chat_member'])
def greeting(message):
    bot.reply_to(message, text='Всего доброго👋🏻')


bot.polling(none_stop=True)
