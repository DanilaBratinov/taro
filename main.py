import telebot

from card import descr
import text

import re
from time import sleep
from telebot import types

token = '7032117391:AAH4HD0J4OusBe9GT_hEg60gyuO8o4GAdOU'
bot = telebot.TeleBot(token)
remove_keyboard = telebot.types.ReplyKeyboardRemove()

# Старт
# Start
@bot.message_handler(commands=['start'])
def start_message(message):
    chatID = message.chat.id
    print("Зашел")

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Принять магию 🪐')

    markup.add(item1)

    bot.send_chat_action(chatID, 'typing')
    bot.send_message(chatID, f"Приветствую тебя, {message.from_user.first_name}!")

    bot.send_chat_action(chatID, 'typing')
    sleep(1)
    bot.send_message(chatID, "Я – бот твоего будущего🔮 стражник мистических знаний и тайн 🧙🏻‍♂️")

    bot.send_chat_action(chatID, 'typing')
    sleep(2)
    bot.send_message(chatID, "Раскладывая карты и читая звезды 💫 я помогу тебе раскрывать тайны своего собственного пути 🎩")

    bot.send_chat_action(chatID, 'typing')
    sleep(2)
    bot.send_message(chatID, "Доверься мне и позволь мне осветить твоё будущее светом магии и мудрости! 🙏")

    bot.send_chat_action(chatID, 'typing')
    sleep(4)
    bot.send_message(chatID, "Чтобы помочь тебе раскрывать загадки своего собственного пути, мне нужно узнать о тебе немного больше 🌙✨", reply_markup=markup)

# Варианты кнопок
@bot.message_handler(content_types=['text'])
def send_message(message):
    chatID = message.chat.id
    match message.text:
        case "Принять магию 🪐":
            bot.send_message(chatID, "Напиши, пожалуйста, своё имя", reply_markup=remove_keyboard)
            bot.register_next_step_handler(message, get_name)
        case "Любовь 💘":
            bot.send_message(chatID, f"_{text.descr}_", parse_mode="Markdown", reply_markup=remove_keyboard)
             
            bot.send_chat_action(chatID, 'typing')
            sleep(2)
            bot.send_message(chatID, "Опиши, пожалуйста, своего спутника")

            bot.send_chat_action(chatID, 'typing')
            sleep(1)
            bot.send_message(chatID, "Как его зовут ?")
            bot.register_next_step_handler(message, get_partner_name)
        case "Магия 🔮":
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(chatID, "Сиди и думай, что написать дальше!")

        case "Дурак":
            photo = open('card/img/fool.jpg', 'rb')
            bot.send_photo(chatID, photo, caption=descr.fool, parse_mode="Markdown")

        case "Маг":
            photo = open('card/img/magician.jpg', 'rb')
            bot.send_photo(chatID, photo, caption=descr.magician, parse_mode="Markdown")

        


# User data
def get_name(message):
    chatID = message.chat.id

    name = message.text

    if name.isalpha() or name.isspace():
        print(name)

        bot.send_message(chatID, "Прекрасное имя, полное волшебства!")
        sleep(1)
        bot.send_message(chatID, "Напиши свою дату рождения")

        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(chatID, "В имени должны быть только буквы")
        bot.register_next_step_handler(message, get_name)


def get_age(message):
    chatID = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('👨')
    item2 = types.KeyboardButton('👧')

    markup.add(item1, item2)

    age = message.text
    if re.match(r'\d{2}\.\d{2}\.\d{4}', age):
        print(age)

        bot.send_message(chatID, "Ваш возраст полон мудрости 🧙🏻‍♂️")

        sleep(2)
        bot.send_message(chatID, "Каков твой пол?", reply_markup=markup)
        bot.register_next_step_handler(message, get_genus)
    else:
        bot.send_message(chatID, "Введи дату в формате *01.01.2001*", parse_mode="Markdown")
        bot.register_next_step_handler(message, get_age)


def get_genus(message):
    chatID = message.chat.id
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Любовь 💘')
    item2 = types.KeyboardButton('Будующее 🔮')
    item3 = types.KeyboardButton('Карта дня ☀️')
    item4 = types.KeyboardButton('Финансовое благополучие 💰')

    markup.add(item1, item2, item3, item4)

    match message.text:
        case '👨':
            print("Парень")
        case '👧':
            print("Девушка")

    bot.send_message(chatID, "Благодарю тебя за ответы, которые мне пригодятся для раскрытия тайны твоего собственного пути", reply_markup=remove_keyboard)
    sleep(2)
    bot.send_message(chatID, "Выбери тему гадания:", reply_markup=markup)

# Pertner data
def get_partner_name(message):
    chatID = message.chat.id

    name = message.text

    if name.isalpha() or name.isspace():
        print(name)

        bot.send_message(chatID, "Когда он родился?")
        bot.register_next_step_handler(message, get_partner_age)
    else:
        bot.send_message(chatID, "В имени должны быть только буквы")
        bot.register_next_step_handler(message, get_partner_name)


def get_partner_age(message):
    chatID = message.chat.id
    age = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Магия 🔮')
    markup.add(item1)

    if re.match(r'\d{2}\.\d{2}\.\d{4}', age):        
        print(age)

        bot.send_message(chatID, "Супер! Спасибо")
        bot.send_message(chatID, "Нажимай на кнопку, чтобы начать", reply_markup=markup)
    else:
        bot.send_message(chatID, "Введи дату в формате *01.01.2001*", parse_mode="Markdown")
        bot.register_next_step_handler(message, get_partner_age)


bot.infinity_polling()