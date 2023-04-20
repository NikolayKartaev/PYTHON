import string
import random

# Задача 0


def Power():
    a = int(input("Введите число a: "))
    b = a*a
    print(f"Квадрат {a} = {b}")

# Задача 1
# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# if b==a*a:
#     print(f'Число {b} является квадратом {a}')
# else:
#     print(f'Число {b} НЕ является квадратом {a}')

# Задача 2 Организуйте последовательный ввод чисел до тех пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.
# i=0
# a = int(input("Введите число a: "))
# while a!=0:
#     if a%3==0:
#         print(f'Число {a} кратно 3')
#         i+=1
#     a = int(input("Введите число a: "))
# print(f'Количество чисел кратных 3: {i}')

# Задача 3. Напишите программу, которая будет на число N и выводить числа от N до N

# N = int(input("Введите число N: "))
# if N > 0:
#     for i in range(-N, N+1):
#         print(f"{i} ", end='')
# if N < 0:
#     for i in range(N, -N+1):
#         print(f"{i} ", end='')

# N = abs(int(input("Введите число N: "))) // модуль числа
# i = -N
# while i <= N:
#     print(f"{i} ", end='')
#     i += 1


# Задача 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# number = float(input("Введите число: "))
# print(int((number*10) % 10))
# print(int((number % 1 - number % 0.1) * 10))


# # Задача 5. Напишите программу, которая находит наибольшее и наименьшее число из списка значений.

# number = int(input("Введите число: "))
# min = number
# max = number
# while number!=0:
#     number = int(input("Введите число: "))
#     if number<min: min=number
#     if number>max: max=number
# print(f"Максимум {max}, минимум {min}")


# numbers = [5,-4,8,9,-9,4,7,0,1,-5]
# for i in numbers:
#     print(i)


def CheckEvenOrOdd(value):
    if value % 2 == 0:
        return ("четное")
    else:
        return ("нечетное")


def Task0_1(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            if i % 2 == 0:
                print(f"{i} - четное")
            else:
                print(f"{i} - нечетное")
    print(f"Количество делителей: {count} - by Task0_1")


def Task0_2(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            print(f"{i} - {CheckEvenOrOdd(i)}")
    print(f"Количество делителей: {count} - by Task0_2")

# number = int(input("Введите число: "))
# print()
# Task2_1(number)
# print()
# Task2_2(number)


def FindBoolValue(a, b):
    result = not a or b
    if result == True:
        return 1
    else:
        return 0


# Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.
def Task1():
    print('X Y R')
    for x in range(2):
        for y in range(2):
            print(x, end=' ')
            print(y, end=' ')
            print(FindBoolValue(x, y))

# x = int(input("Введите X: "))
# y = int(input("Введите Y: "))
# FindBoolValue(x,y)


def Task1_1():
    print()
    print('X | Y | ¬ X ∨ Y')
    for x in range(2):
        for y in range(2):
            print(f"{x} | {y} |    {int(not x or y)}")


# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.
def Task2(a, b):
    count = 0
    for i in range(len(b)-len(a)+1):
        if a == b[i:i+len(a)]:
            count += 1
    print(count)

# str1= input("Введите строку 1: ")
# str2= input("Введите строку 2: ")
# Task2(str1, str2)


def Task2_1():
    string = input("Введите строку: ")
    phrase = input("Введите фразу: ")
    count = 0
    for i in range(len(phrase)-len(string)+1):
        if string == phrase[i:i+len(string)]:
            count += 1
    print(count)


# Вывод по элементам
# phrase = input("Введите фразу: ")
# for el in phrase:
#     print(el, end='')

# print()
# #Вывод элементов с индексами
# for i in range(len(phrase)):
#     print(phrase[i], end='')


# Вывод дробного числа с указанием количества знаков после запятой без округления
def float():
    fl = 2.715415864
    print(f"{fl:.6f}")


# Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...
def Task3_1():
    N = int(input())
    array = []
    for i in range(N):
        array.append((-3)**i)
        if i == N-1:
            print(array)


def Task3_2():
    N = int(input())
    for i in range(N):
        print(f"{(-3)**i}", end=' ')


# Задача 4. Найдите все числа до 10000, у который количество делителей равно 10.

def Task0_3(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    return count


def Task4():
    countnumbers = 0
    for number in range(1, 10001):
        if Task0_3(number) == 10:
            countnumbers += 1
            print(f"{number}\t", end='')
    print()
    print(f"Количество чисел с делителем 10 равно: {countnumbers}")


def Task4_1():
    countnumbers = 0
    for numbers in range(1, 10001):
        countdivs = 0
        for i in range(1, numbers+1):
            if numbers % i == 0:
                countdivs += 1
        if countdivs == 10:
            countnumbers += 1
            print(f"{numbers}\t", end='')
    print()
    print(countnumbers)


def shift(list, steps):  # Сделать смещение списка ну указанное количество элементов
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            print(list)
            list.append(list.pop(0))

    else:
        for i in range(steps):
            print(list)
            list.insert(0, list.pop())


# SEMINAR_3

def TaskS3_1():
    length = 7
    # numbers = [0]*length
    # for i in range(length):
    #     numbers[i] = random.randint(0,10)          создание списка через цикл
    # print(numbers)

    length = int(input("Введите количество элементов списка: "))
    numbers = [int(input("Введите элемент списка: "))
               for _ in range(length)]  # создание списка через генератор списков
    print(numbers)
    print(sum(numbers))
    if sum(numbers) % 2 == 0:
        print("Сумма всех элементов четная")
    else:
        print("Сумма всех элементов нечетная")

    # укоротил код!!!
    numbers = [int(input("Введите элемент списка: "))for _ in range(
        int(input("Введите количество элементов списка: ")))]
    print(numbers)
    print("Сумма всех элементов четная" if sum(numbers) %
          2 == 0 else "Сумма всех элементов нечетная")
    # укоротил код!!!

    # numbers = (random.randint(0,10)for i in range(length)) # создание генератора
    # numbers=list(numbers)                         # создание списка из генератора
    # print(numbers)
    # print(type(numbers))


# Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня. Определите в какой период выпало больше осадков:
# в первой или второй половине июня.

def TaskS3_2():
    sumFirsthalf = sumSecondhalf = 0
    sumFirsthalf, sumSecondhalf = 0, 0

    list = [random.randint(0, 25)for _ in range(30)]

    # for i in range(len(list)/2):
    #     sumFirsthalf+=list[i]            - подсчет сразу двух переменных в одном цикле
    #     sumSecondhalf+=list[i+15]

    # print(list)
    # if sumFirsthalf > sumSecondhalf:
    #     print(f"В первой половине июня выпало больше осадков")
    # else:
    #     print(f"В второй половине июня выпало больше осадков")

    sumFirsthalf = sum(list[:len(list)//2])
    sumSecondhalf = sum(list[len(list)//2:])
    print(list)
    print(sumFirsthalf)
    print(sumSecondhalf)
    print("В первой половине июня выпало больше осадков" if sumFirsthalf >
          sumSecondhalf else "Во второй половине июня выпало больше осадков")


# Задача 2.
# заполнить анкету, последовательно вводя в программу:
# - имя;
# - возраст;
# - хобби;
# - любимое животное.
# После окончания ввода, выводится заполненная анкета.
def TaskS3_3():
    anketa = dict(Имя=input('Ваше имя: '),
                  Возраст=input('Ваш возраст: '),
                  Хобби=input('Ваше хобби: '),
                  Животное=input('Ваше любимое животное: '))
    print()

    for key, value in anketa.items():
        print("{0}: {1}".format(key, value))
    print(anketa)


def Dictionary3():
    dictionary = {}
    dictionary['name'] = input("Введите свое имя: ")
    dictionary['age'] = input("Введите свой возраст: ")
    dictionary['hobby'] = input("Введите свое хобби: ")
    dictionary['favorite_animal'] = input("Введите свое любимое животное: ")

    for (k, v) in dictionary.items():
        print(k+":", v)


# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.

def TaskS3_4():

    symbols = string.ascii_letters + string.digits + string.punctuation

    password = [symbols[random.randint(0, len(symbols))] for _ in range(
        int(input("Введите длину пароля: ")))]
    print(*password, end='')


# Задача 4. Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
# Кассир последовательно вводит в программу
# позиции из чека «ручка», «карандаш», «ластик».
# Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.

def TaskS3_5():
    # или prices = dict(ручка = 5, карандаш = 3, ластик = 4)
    prices = {"ручка": 5, "карандаш": 3, "ластик": 4}
    check = 0
    flag = True
    while flag:
        goods = input("Введите наименование товара:\n").lower()
        if goods == "стоп":
            flag = False
        elif goods in prices:
            # Ищет в словаре prices по ключу введенного в переменную goods
            check += prices[goods]
        else:
            print("Такого товара нет. Введите корректное название")
    print(f"Сумма чека: {check}")


# СЕМИНАР 4

# ЗАДАЧА 0. Создайте кортеж. Запишите в него 10 случайных чисел
def TaskS4_1():
    tuple1 = tuple(random.randint(1, 100) for _ in range(10))
    N = int(input("Введите индекс элемента, которые хотите заменить: "))
    print(tuple1)
    tuple1 = tuple1[:N-1] + (random.randint(1, 100),) + tuple1[N:] 
    print(tuple1)

# ЗАДАЧА 1. Создайте кортеж, заполненный случайными числами. Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.
def change_element(numbers, index):
    return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]

def TaskS4_2():
    tuple1 = tuple(random.randint(1, 10) for _ in range(5))
    index = 2
    print(*tuple1)

# ЗАДАЧА 2 На вход подаются два числа. Напишите метод, который вернёт сумму, разность, произведение и частное этих чисел.

# def TaskS4_3(x,y):
#     return (x+y, x-y, x*y, x/y)

# x=int(input())
# y=int(input())
# tuple2 = TaskS4_3(x,y)
# print(*tuple2)
# print(tuple2)


# x = int(input())
# y = int(input())
# print(" {}, {}, {}, {}".format(x+y,x-y,x*y,x/y))

# ЗАДАЧА 3
# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов. Определите, сколько элементов было удалено.

def TaskS4_4():
    list1 = [random.randint(1, 20) for _ in range(10)]
    list2 = list(set(list1))
    print(f"Список на 10 элементов: {list1}")
    print(f"Список без повторяющихся значений:{list2}")
    print(f"Удалено элементов: {len(list1) - len(list2)}")



def TaskS4_5():
    A = set("Илья Федор Коля Семен Олег Лев Антон Артем Боря Стас Марк Ян".split())
    B = set("Илья Георгий Лев Демьян Антон Коля Владислав Боря Стас Марк Влад".split())
    C = set("Федор Георгий Олег Демьян Артем Коля Елисей Боря Стас Влад".split())

    result = A.intersection(B).intersection(C) # или A & B & C
    print(*result)

col=[]
values = dict(Ручка = 5, Карандаш = 3, Ластик = 4)
while i != "стоп":
    col[i] = int(input)
    check = values["Ручка"]*col[i]