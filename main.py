import telebot
from telebot import types


token = '6168455071:AAGdwPfOjEktwm-_4ugZruV5cWDJ_osjLiU'
bot = telebot.TeleBot(token)

def send(idd, text, markup=None):
    try:
        bot.send_message(chat_id=idd, text=text, reply_markup=markup, parse_mode='html')
    except OSError as e:
        print(repr(e) + "    Oshibka seti    (stroka 64)")
        bot.send_message(chat_id=idd, text=text, reply_markup=markup, parse_mode='html')


def send_photo(idd, photo, capt=None, markup=None):
    try:
        bot.send_photo(chat_id=idd, photo=photo, caption=capt, reply_markup=markup, parse_mode='html')
    except OSError as e:
        print(repr(e) + " Oshibka seti ")
        bot.send_photo(chat_id=idd, photo=photo, caption=capt, reply_markup=markup, parse_mode='html')

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


@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    bot.send_photo(-1001685928825, fileID)

bot.polling(none_stop=True)
