import telebot
from telebot import types
import requests
import time
from random import randint as RAND

with open("bot.txt", mode='r', encoding='utf-8') as bottoken:
    token = bottoken.readline()
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(row_width=2)  # создаем клавиатуру

button_reg = types.KeyboardButton('регистрация')  # создаем кнопки
button_alrm = types.KeyboardButton('оповещение')
markup.add(button_reg, button_alrm)


@bot.message_handler(commands=['start'])
def send_welcome(our_message):
    bot.send_message(our_message.from_user.id,
                     "Приветствую! Я бот. Нажмите /help ", reply_markup=markup)


@bot.message_handler(commands=['help'])
def list_commands(our_message):
    bot.send_message(our_message.from_user.id,
                     "Список команд еще формируется. Нажми /start ")


def randomnumber():
    number = int(RAND(1, 1000))
    return number


@bot.message_handler(content_types=['text'])
def greetings(our_message):

    text = (our_message.text).lower()

    data = open("logs.txt", mode='a', encoding='utf-8')
    text_logs = f'{our_message.from_user.first_name} {our_message.from_user.last_name} {our_message.from_user.id}: {our_message.text}\n'
    data.write(text_logs)  # записываем логи чата
    data.close()

    if text == "регистрация":
        try:
            data = open("registred_users.txt", mode='r', encoding='utf-8')
            id_list = data.readlines()
            data.close()
            id_list = list(id[:-1]
                           for id in id_list)  # убираем символ \n срезом
            if str(our_message.from_user.id) in id_list:
                bot.reply_to(our_message, "Вы уже зарегистрированы!")
        except:
            data = open("registred_users.txt", mode='a', encoding='utf-8')
            data.write(f"{our_message.from_user.id}\n")
            data.close()
            bot.reply_to(our_message, "Регистрация прошла успешно!")

    elif text == "оповещение":
        data = open("registred_users.txt", mode='r', encoding='utf-8')
        id_list = data.readlines()
        data.close()
        for id in id_list:
            bot.send_message(id, "Совещание начнется через 30 минут!")

    elif 'привет' in text:
        bot.reply_to(
            our_message, f'Привет, {our_message.from_user.first_name}!')

    elif text == 'котик':
        request = requests.get(f"https://cataas.com/cat?{time.time()}")
        bot.send_photo(our_message.from_user.id, request.content)

    elif text == 'погода':
        request = requests.get('https://wttr.in/?0T')
        bot.reply_to(our_message, request.text)

    elif text == "игра":
        global number
        bot.reply_to(
            our_message, f'✅ {our_message.from_user.first_name}, давай поиграем в игру!\nЯ загадал число, угадай его!\n\nВведите ваше число👇')

        bot.register_next_step_handler(our_message, game)
        number = randomnumber()


def counter(function1):
    def wrap(*args, **kwargs):
        wrap.count_function += 1
        return function1(*args, **kwargs)
    wrap.count_function = 0
    return wrap


@counter
@bot.message_handler(content_types=['text'])
def game(mess):

    print(f"Загаданное число: {number}")  # видим в консоли загаданное число

    text1 = mess.text
    text1 = int(text1)

    print(text1)  # видим число указанное пользователем

    if text1 > number:

        bot.reply_to(
            mess, f'🔻 Укажите число меньше, {mess.from_user.first_name}!')
        bot.register_next_step_handler(mess, game)

    if text1 < number:

        bot.reply_to(
            mess, f'🔺 Укажите число больше, {mess.from_user.first_name}!')
        bot.register_next_step_handler(mess, game)

    if int(text1) == number:
        msg = bot.reply_to(
            mess, f'🎉🎉🎉ВЫ ВЫИГРАЛИ, {(mess.from_user.first_name).upper()}!!! ПОЗДРАВЛЯЮ!!!🎉🎉🎉\nВы угадали с {game.count_function} попытки!')
        bot.register_next_step_handler(mess, greetings)
        game.count_function = 0


bot.polling()
