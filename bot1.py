import telebot
from telebot import types

id_chat = -866251372

token = '6168455071:AAGdwPfOjEktwm-_4ugZruV5cWDJ_osjLiU'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'admin'])
def cmd(message):
    chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
    print(chat_member)









@bot.message_handler(content_types=['text'])
def text(message):
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    pass


@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    bot.send_photo(-1001760730931, fileID)


bot.polling(none_stop=True)
