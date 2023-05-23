import telebot
import requests
import time

bot = telebot.TeleBot("", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Как дела?")
        

@bot.message_handler(content_types=['text'])
def greetings(message):
    print(message)
    text = (message.text).lower()
    if 'привет' in text:
        bot.reply_to(message, f'Привет, {message.from_user.first_name}!')
    elif text == 'погода':
        request=requests.get('https://wttr.in/?0T')
        bot.reply_to(message, request.text)
    elif text == 'котик':
        request=requests.get(f"https://cataas.com/cat?{time.time()}")
        bot.send_photo(message.from_user.id, request.content)

bot.polling()