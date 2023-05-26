# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot


def Zadacha1():
    with open("bot.txt", mode='r', encoding='utf-8') as bottoken:
        token = bottoken.readline()
    bot = telebot.TeleBot(token)

    @bot.message_handler(content_types=['text'])
    def technical_support(user_question):
        text = (user_question.text).lower()

        if '?' in text:

            with open("questions.txt", mode='a', encoding='utf-8') as user_questions:
                user_questions.write(
                    f'ID:{user_question.from_user.id}:{text}\n')

    bot.polling()



# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.


def Zadacha2():
    with open('bot.txt', mode='r', encoding='utf-8') as bottoken:
        token = bottoken.readline()
    bot = telebot.TeleBot(token)

    with open("questions.txt", mode='r', encoding='utf-8') as user_questions:

        
        user_questions = list((user_questions.readlines())) # список вопросов от пользователей из файла

        for line in user_questions:
            position = (line[:-1]).split(":") # разбиваем строку на ID и вопрос
            id, question = position[1], position[2]

            print(f"Вопрос от пользователя с ID {id}: {question}")
            bot.send_message(id, input(f"Ответ для пользователя с ID {id}: "))

# Zadacha1()
# Zadacha2()
