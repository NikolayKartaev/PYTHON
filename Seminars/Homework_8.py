# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot

with open("bot.txt", mode='r', encoding='utf-8') as bottoken:
    token = bottoken.readline()
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def technical_support(user_question):
    text = (user_question.text).lower()

    with open("questions.txt", mode='a', encoding='utf-8') as user_questions:
        user_questions.write(f'ID {user_question.from_user.id} : {text}\n')


bot.polling()


    
