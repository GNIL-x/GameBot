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


@bot.message_handler(commands=['error'])
def err(message):
    bot.send_message(message.chat.id, 'Опишите вашу проблему богу?')
    sl[message.chat.id] = [False, True]


@bot.message_handler(content_types=['text'])
def text_mes(message):
    if sl[message.chat.id][0]:
        z = steam_pr(message.text)
        if len(z) == 2:
            bot.send_message(message.chat.id, f'Цена в steam без скидки: {z[0]}\n'
                                              f'Цена в steam со скидкой: {z[1]}')
        else:
            if z == 'Free to Play':
                bot.send_message(message.chat.id, 'В steam игра бесплатна!')
            elif z == 'Такой игры не существует😭😭😭😭':
                bot.send_message(message.chat.id, z)
            else:
                bot.send_message(message.chat.id, f'Цена в steam (скидки нет): {z}')
    elif sl[message.chat.id][1]:
        send_analytic(message, 'shopgamerbot')
        bot.send_message(message.chat.id, 'Ваше сообщение доставлено.', reply_markup=key1)
        sl[message.chat.id][1] = False
