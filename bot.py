import telebot

import requests

import config

import random

from telebot import types

print(config)
bot = telebot.TeleBot(config.access_token)

def my_site_commercial(message):
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="2be - консалтинговая группа", url="2be.team")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Нажми на кнопку, чтобы подробнее познакомиться с нашими услугами", reply_markup=keyboard)
        

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
        bot.send_message(message.chat.id, "Я - бот-консалтер! Если нужна моя помощь, выберите одну из следующих команд:")
        for i in range(config.command_length):
            bot.send_message(message.chat.id, config.command_list[i] + config.command_description[i])


@bot.message_handler(commands=['site'])
def reply(message):
        my_site_commercial(message)

@bot.message_handler(commands = ['consult'])
def reply(message):
        bot.send_message(message.chat.id, "{} {}, вы вошли в режим консультации! Выберите нужные вам параметры, для того, чтобы сделать вместе со мной макет ресторана!".format(message.chat.first_name, message.chat.last_name))  
            
@bot.message_handler(content_types=['text'])
def echo(message):
    if config.count == 0:
        bot.send_message(message.chat.id, random.choice(config.greetings))
        config.greetings.append(message.text)
    if message.text != "/test":
        bot.send_message(message.chat.id, message.text + ". Be cool, visit 2be.team")
        print(config.greetings)
        print(message)
        


if __name__ == '__main__':
     
    bot.polling(none_stop = True)
    
    


