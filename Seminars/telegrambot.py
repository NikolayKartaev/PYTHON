import telebot
import requests
import time
from random import randint as RAND

bot = telebot.TeleBot("5986374571:AAHH-gRgrsbSNig3ZL0GJuzaSloNwF-ol5c", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Как дела?")
        
is_game=False
@bot.message_handler(content_types=['text'])
def greetings(message):
    print(message)
    text = (message.text).lower()
    if 'привет' in text:
        bot.reply_to(message, f'Привет, {message.from_user.first_name}!')

@bot.message_handler(content_types=['text'])
def game(message):

    if message =="ИГРА":
        is_game=True
    while is_game:
        number=RAND(1,1000)
        bot.reply_to(message, f'Я загадал число, угадай его, {message.from_user.first_name}!')

        bot.register_next_step_handler(msg, process_name_step)
        
    # elif text == 'погода':
    #     request=requests.get('https://wttr.in/?0T')
    #     bot.reply_to(message, request.text)
    # elif text == 'котик':
    #     request=requests.get(f"https://cataas.com/cat?{time.time()}")
    #     bot.send_photo(message.from_user.id, request.content)


bot.polling()