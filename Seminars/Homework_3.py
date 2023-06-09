# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8


def Fibo(n):
    if n == 1 or n == 2:
        return 1
    return Fibo(n-1) + Fibo(n-2)


def Task1():
    N = int(input("Введите N: "))
    list1 = list()
    for i in range(1, N+1):
        list1.append(Fibo(i))
    print(f"{N} -> {list1}")


    
def Task1b():
    numbers=[1,1]
    N= 10
    for i in range(2,N):
        numbers.append(numbers[i-1]+numbers[i-2])
    print(f"{N} -> {numbers}")
    


# Задача 2. В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

def Task2():
    fruits = ['абрикос', 'авокадо', 'апельсин', 'айва', 'банан',
              'баклажан', 'боярышник', 'ваниль', 'дыня', 'гранат',
              'гуарана', 'земляника', 'калина', 'кокос', 'личи',
              'мускатный орех', 'папайя', 'слива', 'танжерин', 'тыква']

    char = input("Введите букву: ")
    for i in range(len(fruits)):
        if fruits[i][0] == char:
            print(fruits[i], end=' ')
            
    char = input("Введите букву: ")
    for element in fruits:
        if element[0] == char:
            print(element, end=' ')
            


# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут».
# Если фраза ему неизвестна, он выводит соответствующую фразу.

def Task3():
    botName = input("Задайте имя боту: ")

    botPhrases = {"привет": "Привет!", "здравствуйте": "Привет!", "как дела": "Спасибо, все отлично! Как Ваши дела?",
                "как дела?": "Спасибо, что спросили! Все прекрасно! Как Ваши дела?",
                "": "Повторите, пожалуйста!", "как тебя зовут": "Меня зовут " + botName, "как тебя зовут?": "Меня зовут " + botName, "что ты думаешь об ИИ": "Бесконечные возможности" }


    startBot = input("Напишите что-то для старта бота.\n").lower()

    if startBot != "" or startBot != "\n":
        flag = True

    while flag:
        your_message = input("Ваше сообщение: ").lower()
        if your_message.lower() == "стоп":
            flag = False

        elif your_message in botPhrases:
            print(f"{botName}: {botPhrases[your_message]}")
            print()
            if botPhrases.items=="Меня зовут " + botName:
                botPhrases[f'{your_message}'] = input()

        else:
            print(f"{botName}: Извините, на данный момент я не знаю, что ответить на эту фразу.\nНо я являюсь обучаемой моделью. Укажите, что я должен ответить на ваш вопрос: \n")
            botPhrases[f'{your_message}'] = input()
            print()

