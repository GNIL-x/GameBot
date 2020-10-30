import telebot
from parcers.steam import *
from .keyboards import *
from .Callback_to_user import *
import time
import random

sl = dict()

bot = telebot.TeleBot("1383488768:AAET5-F8xH4Wvy7nc-yQRd6ic6n_2MJOg44")


@bot.message_handler(commands=['start', 'help', ])
def start_mes(message):
    bot.send_message(message.chat.id, 'Привет, это бот для просмотра цен игр на сайтах...', reply_markup=key1)
    sl[message.chat.id] = [False, False]


@bot.message_handler(commands=['game'])
def game_mes(message):
    bot.send_message(message.chat.id, 'Введи название игры')
    sl[message.chat.id] = [True, False]


@bot.message_handler(content_types=['text'])
def text_mes(message):
    if sl[message.chat.id][0]:
        steam_pr(message.text)


