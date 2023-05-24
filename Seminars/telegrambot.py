import telebot
import requests
import time
from random import randint as RAND

bot = telebot.TeleBot(
    "5986374571:AAHH-gRgrsbSNig3ZL0GJuzaSloNwF-ol5c", parse_mode=None)

def randomnumber():
    number = int(RAND(1, 1000))
    return number

@bot.message_handler(commands=['start', 'help'])
def send_welcome(our_message):
	bot.reply_to(our_message, "Howdy, how are you doing?")

@bot.message_handler(content_types=['text'])
def greetings(our_message):
    text = (our_message.text).lower()
    
    data = open("logs.txt", mode='a', encoding='utf-8')
    text_logs=f'{our_message.from_user.first_name} {our_message.from_user.last_name}: {our_message.text}\n'
    data.write(text_logs)
    data.close()
    
    if text == "регистрация":
        data = open("registred_users.txt", mode='a', encoding='utf-8')
        data.write(f"{our_message.from_user.last_name}\n")
        data.close()
        bot.reply
        
        
    # print(f"{our_message}\n")
    # переводим наше сообщение в текст и помещаем в переменную
    
    
    if 'привет' in text:
        bot.reply_to(
            our_message, f'Привет, {our_message.from_user.first_name}!')

    elif text == 'котик':
        request = requests.get(f"https://cataas.com/cat?{time.time()}")
        bot.send_photo(our_message.from_user.id, request.content)

    elif text == 'погода':
        request = requests.get('https://wttr.in/?0T')
        bot.reply_to(our_message, request.text)

    elif text == "игра":

        bot.reply_to(
            our_message, f'{our_message.from_user.first_name}, давай поиграем в игру!\nЯ загадал число, угадай его!\n\nВЫ ГОТОВЫ???🤠')
    answer = (our_message.text).lower()
    if answer == "да":
        bot.reply_to(
            our_message, f'✅Отлично! {our_message.from_user.first_name}, введите ваше число🔢👇 ')
        bot.register_next_step_handler(our_message, game)



def counter(function1):
    def wrap(*args, **kwargs):
        wrap.count_function += 1
        return function1(*args, **kwargs)
    wrap.count_function = 0
    return wrap


number=randomnumber()
@counter
@bot.message_handler(content_types=['text'])
def game(mess):
    
    print(f"Загаданное число: {number}")  # видим в консоли загаданное число
    is_game = True
    while is_game:
        
        text1 = mess.text
        text1 = int(text1)
        
        print(text1)  # видим число указанное пользователем
        
        if text1 > number:

            bot.reply_to(
                mess, f'🔻 Укажите число меньше, {mess.from_user.first_name}!')
            bot.register_next_step_handler(mess, game)
            is_game = False

        if text1 < number:

            bot.reply_to(
                mess, f'🔺 Укажите число больше, {mess.from_user.first_name}!')
            bot.register_next_step_handler(mess, game)
            is_game = False
        if int(text1) == number:
            
            msg = bot.reply_to(
                mess, f'🎉🎉🎉ВЫ ВЫИГРАЛИ, {(mess.from_user.first_name).upper()}!!! ПОЗДРАВЛЯЮ!!!🎉🎉🎉\nВы угадали за {game.count_function} раз!')
            bot.register_next_step_handler(mess, greetings)
            is_game = False



bot.polling()
