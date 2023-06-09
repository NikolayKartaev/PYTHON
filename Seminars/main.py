import string
import random
from random import randint as R

# Задача 0

# def Power():
#     a = int(input("Введите число a: "))
#     b = a*a
#     print(f"Квадрат {a} = {b}")


def TaskS1_0():
    n = int(input("Введите число n: "))
    print(f"{n} -> {n**2}")


# # Задача 1 Напишите программу, которая на вход принимает два
# числа и проверяет, является ли второе число квадратом
# первого.

def TaskS1_1():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a**2 == b:
        print(f'Число {b} является квадратом {a}')
    else:
        print(f'Число {b} НЕ является квадратом {a}')


# Задача 2 Организуйте последовательный ввод чисел до тех пор, пока не будет введён 0.
# Подсчитайте среди введённых чисел те, которые кратны трём.

def TaskS1_2():
    count = 0
    A = int(input("Введите число a: "))
    while A != 0:
        if A % 3 == 0:
            count += 1
        A = int(input("Введите число a: "))
    print(f'Количество чисел кратных 3: {count}')


# Задача 3. Напишите программу, которая будет на число N и выводить числа от -N до N

def TaskS1_3():
    N = abs(int(input("Введите число N: ")))
    for i in range(-N, N+1):
        print(i, end=' ')


# N = abs(int(input("Введите число N: "))) // модуль числа
# i = -N
# while i <= N:
#     print(f"{i} ", end='')
#     i += 1


# Задача 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

def TaskS1_4():
    n = float(input("Введите число: "))
    print(n)
    print(int(n*10//1)%10)



def TaskS1_4b():

    number = 6
    div = 3
    a=number//div
    b= number%div
    
    print(a*div+b)
    

# # Задача 5. Напишите программу, которая находит наибольшее и наименьшее число из списка значений.

def TaskS1_5():
    number = int(input("Введите число: "))
    min = number
    max = number
    while number!=0:
        number = int(input("Введите число: "))
        if number<min: min=number
        if number>max: max=number
    print(f"Максимум {max}, минимум {min}")

def TaskS1_5b():
    number = [1,2,3]
    print(number)
    min = number[0]
    max = number[0]
    for i in number:
        if i<min: min=i
        if i>max: max=i
    print(f"Максимум {max}, минимум {min}")


# numbers = [5,-4,8,9,-9,4,7,0,1,-5]
# for i in numbers:
#     print(i)


# СЕМИНАР 2

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

def CheckEvenOrOdd(value):
    if value % 2 == 0:
        return ("четное")
    else:
        return ("нечетное")
    
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
# print(FindBoolValue(x, y))


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

def Task2repeat():
    count=0
    phrase = input("Введите фразу: ")
    word = input("Введите слово: ")
    for i in range (0, len(phrase)-len(word)+1):
        if word == phrase[i:i+len(word)]:
            count+=1
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
            
def Task3_1b():
    array=[(-3)**i for i in range(int(input()))]
    print(array)



def Task3_2():
    N = int(input())
    for i in range(N):
        print(f"{(-3)**i}", end=' ')


# Задача 4. Найдите все числа до 10000, у который количество делителей равно 10.

def NumCounters(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    return count


def Task4():
    countnumbers = 0
    for number in range(1, 10001):
        if NumCounters(number) == 10:
            countnumbers += 1
            print(f"{number}\t", end='')
    print()
    print(f"Количество чисел с 10 делителями: {countnumbers}")




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

    length = int(input("Введите количество элементов  списка: "))
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
    s=''
    password = [symbols[random.randint(0, len(symbols))] for _ in range(
        int(input("Введите длину пароля: ")))]
    print(password)
    for i in password:
        s+=i
    print(s)

def PasswordGenerator():
    pass_symbols = string.ascii_letters + string.digits + string.punctuation
    
    print("".join(map(lambda x: str(x), 
                               (pass_symbols[random.randint(0, len(pass_symbols))] 
                                                  for _ in range(int(input()))))))
        



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
    tuple1 = tuple1[:N] + (random.randint(1, 100),) + tuple1[N+1:]
    print(tuple1)




# ЗАДАЧА 1. Создайте кортеж, заполненный случайными числами. Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.


def change_element(numbers, index):
    return numbers[:index] + (random.randint(1, 100), ) + numbers[index+1:]


def TaskS4_2():
    tuple1 = tuple(random.randint(1, 10) for _ in range(5))
    print(tuple1)
    index = 2
    print(change_element(tuple1, index))

def Z(tupleN, N):
    return tupleN[:N]+(random.randint(1,15),)+tupleN[N+1:]

def Zadacha():
    N=int(input())
    tuple1=tuple(random.randint(1,15) for _ in range(10))
    print(tuple1)
    tuple2=tuple1[:N]+(random.randint(1,15),)+tuple1[N+1:]
    print(tuple2)
    tuple3=Z(tuple1,N)
    print(tuple3)    


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

def Calculate(a,b):
    return a+b, a-b, a*b, a/b


# ЗАДАЧА 3
# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов.
# Удалите из списка дубликаты уже имеющихся элементов. Определите, сколько элементов было удалено.

def TaskS4_4():
    list1 = [random.randint(1, 20) for _ in range(10)]
    list2 = list(set(list1))
    print(f"Список на 10 элементов: {list1}")
    print(f"Список без повторяющихся значений:{list2}")
    print(f"Удалено элементов: {len(list1) - len(list2)}")

def T4():
    list1=[random.randint(1,20) for _ in range(10)]
    list2=list(set(list1))
    print("list1 - {}, list2 - {}, удалено: {}".format(list1, list2, (len(list1)-len(list2))))

# Задача 4

def TaskS4_5():
    A = set("Илья Федор Коля Семен Олег Лев Антон Артем Боря Стас Марк Ян".split())
    B = set("Илья Георгий Лев Демьян Антон Коля Владислав Боря Стас Марк Влад".split())
    C = set("Федор Георгий Олег Демьян Артем Коля Елисей Боря Стас Влад".split())

    result = A.intersection(B).intersection(C)  # или A & B & C
    print(*result)
    
    
    
    
    


# СЕМИНАР 5

# Задача 0. С помощью анонимной функции найдите в списке на 15 элементов числа, кратные 5.
# Заполните список случайным образом числами от 1 до 100.

def tasks5_000():
    number_list=[R(1,100) for _ in range(15)]
    print(number_list)
    print(*list(filter(lambda el:el%5==0,number_list)))


def TaskS5_00():
    list1 = [random.randint(1, 100) for _ in range(15)]

    
    list2 = list(filter(lambda x: x % 5 == 0, list1)) # перебирает коллекцию и выполняет условие функции для значения
    
    list2 = list(filter(lambda x: not (x % 5), list1)) # not(x % 5) можно вместо x % 5 == 0
    print(list1)
    print(list2)


def TaskS5_01():
    list1 = [1, 10, 50, 100]
    # перебирает коллекцию и использует для элемента y лямбда-функцию
    list2 = list(map(lambda y: y*5, list1))
    print(list1)
    print(list2)
    



# Задача 1. На вход подаётся четырёхзначное число. Получите список, состоящий из цифр данного числа, увеличенных на 10.
def option1():
    print(list(map(lambda x: int(x)+10, input())))  # создание списка из числа с помощью преобразований типов данных лямбдой-функцией


def option2():
    N=input()
    listN=list()
    for i in N: # создание списка из числа с помощью цикла
        listN.append(int(i))
    x=list(map(lambda x: x+10, listN))
    print(x)
    
def option3():
    print([int(el)+10 for el in input()]) # создание списка из числа с помощью генератора


def TaskS5_1():
    N = input("Enter number: ")
    list1 = []
    for el in N:
        list1.append(int(el))  # создание списка из числа с помощью цикла
    list2 = list(map(lambda x: x+10, list1))
    print(list2)


def TaskS5_1b():
    N = input("Enter number: ")
    list1 = [int(el) for el in N] # создание списка из числа с помощью генератора
    list2 = list(map(lambda x: x + 10, list1))
    print(list2)

def TaskS5_1c():
    N = list(str(input("Enter number: "))) # создание списка из числа с помощью преобразований типов данных
    print(list(map(lambda x: int(x) + 10, N)))




def ToBinary(x):
    result=""
    while x>0:
        result = str(x%2) + result
        x//=2
    return "0"*(6-len(result)) + result 

def decoder(code):
    animal = [code[i:i+6]  for i in range(0, len(code),6)]
    print(animal)       

def TaskS5_2():

    animals = ['010100001100001001010011001011000000',
               '000001011100001011',
               '001011001111010011',
               '010010010011001111010001001111000111',
               '001100000101000010',
               '001011010001001111001100001001001011',
               '001101010100001100',
               '000001000000010001010010010100001011',
               '000011000101010000000000010001000100',
               '010010001111001101',
               '010010001111000001000000001011000000',
               '011000001001000111']

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet = list(alphabet)
    dictionary = {}
    for i in range(len(alphabet)):
        dictionary[ToBinary(i)] = alphabet[i]
    print()
    # print(dictionary)
        
    result = list(map(lambda x: [dictionary[x[i:i+6]]  for i in range(0, len(x),6)], animals))
    result = list(map(lambda x: "".join(x), result))

    print(*result)


    print()
 

# СЕМИНАР 6

def CheckRandom(lst):
    if len(lst)==len(set(lst)):
        print(f"{lst} - Список с уникальными значениями")
    else: print(f"{lst} - Значения не уникальны!")
        
    
# random_list=[int(input("Введите элемент списка:")) for _ in range(int(input("Введите размер списка: ")))]


# Задача 1. Дан список случайных элементов. Проверьте, что все его элементы уникальны.
list1=[random.randint(1,25) for _ in range(10)]

def IsUnique(sourceList):
    print(sourceList)
    if len(sourceList) == len(set(sourceList)):
        print(f"{sourceList} - уникальный")
    else: 
        print(f"{sourceList} - есть повторы")
        
def Task2_0():
    number1=4444156666
    number2=6164646445
    
    n1=[int(el) for el in str(number1)]
    n2=[int(el) for el in str(number2)]
    n1.sort()
    n2.sort()
    if n1== n2:
        print(f"{n1} {n2} yes")
    else: print("no")
    

def Task2():
    number1=4444156666
    number2=6164646445
    dict1=dict()
    dict2=dict()
    
    number1=str(number1)
    number2=str(number2)

    for i in number1:
        dict1[i]=number1.count(i)

    for i in number2:
        dict2[i]=number2.count(i)

    print(dict1)
    print(dict2)

    if dict1 == dict2:
        print("Числа состоят из одних и тех же цифр.")
    else:
        print("Числа состоят из разных цифр.")
        

# Task2()

def Task2b():
    number1=4444411
    number2=4411444
    
    number1=str(number1)
    number2=str(number2)

    dict1=dict([i,number1.count(i)] for i in number1) # в словарь передается список для всех i из строки
    dict2=dict((i,number2.count(i)) for i in number2) # в словарь передается кортеж для всех i из строки

    print(dict1)
    print(dict2)

    if dict1 == dict2:
        print("Числа состоят из одних и тех же цифр.")
    else:
        print("Числа состоят из разных цифр.")
        
# Task2b()
        
def Task2Maths():
    n1=int(input())
    n2=int(input())
    
    digits=[0]*10
    
    while n1>0:
        index=n1%10
        digits[index]+=1
        n1//=10
    while n2>0:
        index=n2%10
        digits[index]-=1
        n2//=10
        
    for el in digits:
        if el!=0:
            print("Состоят из разных чисел")
            return False
        
    print("Состоят из одинаковых чисел")
        
        

# Task2Maths()  
    

# Задача 3. 2+2

def Task3():
    example = input("Введите арифметическое выражение: ")
    if "+" in example:
        for i in range(len(example)-example.count("+")):
            result += int(example.split("+")[i])

    print(result)
    
def Task3b():
    example = input("Введите арифметическое выражение: ")
    if "+" in example:  
        numbers = example.split("+")
        print(int(numbers[0])+int(numbers[1]))
    if "-" in example:  
        numbers = example.split("-")
        print(int(numbers[0])-int(numbers[1]))
    if "*" in example:  
        numbers = example.split("*")
        print(int(numbers[0])*int(numbers[1]))
    if "/" in example:  
        numbers = example.split("/")
        print(int(numbers[0])/int(numbers[1]))
    

# Task3b()

# Задача 4. Имеется 1000 рублей. Бык стоит – 100 рублей, корова – 50 рублей, телёнок – 5 рублей.
# Сколько быков, коров и телят можно купить на все эти деньги, если всего надо купить 100 голов скота?

def Task4():
    budget = 1000
    bull_price = 100
    cow_price = 50
    calf_price = 5

    for bull_count in range (1,101):
        for cow_count in range (1,101):
            for calf_count in range(1,101):
                if bull_count*bull_price + cow_count*cow_price + calf_count*calf_price == budget and bull_count+cow_count+calf_count == 100:
                    print(f"Купленное количество: быков - {bull_count}, коров - {cow_count}, телят - {calf_count}")
                    
# Task4()


#SEMINAR 7. 20.05.2023

def function():
    print("Hello")

a_function = function # функция - это объект. Функция как объект помещена в переменную. Переменная приняла тип "функция". Функцию можно передавать в другие функции.
# a_function()
# print(type(a_function))

#PVP - функции высшего порядка

#ЗАДАЧА 1. Создайте пользовательский аналог метода filter()
def function_filter(function1, list1):
    return[x for x in list1 if function1(x)] # при помощи генератора перебираем элементы x в списке List и если выполняется функция function1, то возвращаем этот элемент

def Zadacha1():
    numbers=[int(input("Введите элементы списка: ")) for _ in range(int(input("Введите количество элементов списка: ")))]
    print(numbers)
    number_above5a=function_filter(lambda x: x>5, numbers)
    number_above5b=list(filter(lambda x: x>5, numbers))
    print(number_above5a)
    print(number_above5b)

    def above5(x):
        return x>5
    number_above5c=list(filter(above5, numbers))
    number_above5d=function_filter(above5, numbers)
    print(number_above5c)
    print(number_above5d)

#ЗАДАЧА 2. Создать метод, позволяющий замерить время работы других методов

def stopwatch(function):
    import time # импорт модуля в функцию
    def decorator():
        start_time=time.time()
        function()
        print(f"Время выполнения функции: {time.time()-start_time}")
    return decorator

@stopwatch # декоратор
def math_str():
    number='132'
    result=int(number)+int(number+number)+int(number+number+number)
    print(result)
    
@stopwatch # декоратор
def math_int():
    number=132
    result=number + number*1000 + number + number*1000000+number*1000+number
    print(result)
    
# stopwatch(math_str)() # второй вариант вызова (либо поместить в переменную и вызвать ее)
# stopwatch(math_int)() # второй вариант вызова (либо поместить в переменную и вызвать ее)

def Zadacha2():
    math_str() # вызывается функция и декоратор
    math_int() # вызывается функция и декоратор

#ЗАДАЧА 3. Создать декоратор для метода нахождения суммы.

def Zadacha3():
    def formatting_1(function):
        def decorator(a,b): # либо args
            print(f"Cумма чисел {a} + {b} = ",end="") # для двух значений
            function(a,b) # либо args
        return decorator


    def formatting_2(function):
        def decorator(*args):       
            print (f"Cумма чисел ", end='')
            for arg in args:
                print (f"{arg} + ", end='') # для нескольких значений
            print("\b\b= ",end='')
            function(*args)         
        return decorator
            
    @formatting_1
    def sum(a,b):
        print (a+b)

    @formatting_2
    def sum4(a,b,c,d):
        print (a+b+c+d)

    sum (50,125)
    sum4(10,20,30,500)


#ЗАДАЧА 4. Создать декоратор с параметрами.

def greetings(hello): # параметр декоратора
    def our_greetings(function):
        def decorator():
            name = function()
            print(f"{hello}, {name}")
        return decorator
    return our_greetings

def greetings2(greetme):
    def func(function):
        def decorator():
            name = function()
            print(f"{greetme}, {name}")
        return decorator    
    return func


@greetings2("Как поживаете") # параметр декоратора изменяемый
def get_name():
    return input("Как тебя зовут? ")




# СЕМИНАР 8. 21.05.2023
def files():
    data = open("text.txt", mode = 'r+', encoding='utf-8') # открытие файла в корневой папке // указываем имя файла, режим и кодировку


    # <_io.TextIOWrapper name='text.txt' mode='r' encoding='cp1251'> - объект "поток"
    # encoding='cp1251' - стандартная кодировка windows. Нам нужна кодировка utf-8

    # mode='r' - режим чтения
    # mode='w' - режим записи
    # mode='r+' - режим чтения плюс запись
    # mode='w+' - режим записи плюс чтение

    # print(data.readlines()) #считывает файл и выводит в строку как список строк
    # print(data.read()) #считывает файл и выводит строки
    # print(data.readline()) #считывает первую строку (или указанную строку)

    # data.write("\nВторая строка")
    readdata = data.readlines() #запись считанных данных из файла в переменную. Можно пользоваться после закрытия файла

    data.close() # после закрытия файла считывать из него данные или записываь в него данные нельзя

    print(f"1:{readdata}")

    with open("text.txt", mode='r', encoding='utf-8') as data: # включает в себя также close() !!!
        readdata = data.readlines()
    print(f"2:{readdata}")

# СЕМИНАР 9 27.05.2023

import numpy as np

def ZadachaS9_1():
    first = [56,37,48,45,46,43,41,45,47,48,57,63]
    second = [66,46,46,54,57,51,52,54,57,54,68,72]
    third = [89,67,65,77,79,68,74,75,77,77,91,96]

    matrix = [first,second,third]
    result = np.corrcoef(matrix)

    print(result)



def ZadachaS9_2():
    size= 10
    numbers = np.random.randint(1,50,size) # создает массив из случайных элементов размера size
    print(numbers)
    # print(type(numbers)) # массив
    # numbers.sort()                       # сортировка массива (от numpy)
    # print(numbers)

    # mean = sum(numbers)/size
    # print(mean)

    # mean = np.median(numbers)            # среднее значение
    # print(mean)

    num = int(input("Введите число: "))

    distance = [np.abs(x - num) for x in numbers] # distance = list(map(lambda x: np.abs(x - num ), numbers))
    print(f"Расстояния {distance}")

    min_distance = np.min(distance)        # минимальное значение
    print(f"Минимальное расстояние {min_distance}")

    index= distance.index(min_distance)
    print(f"Индекс Минимального расстояния {distance.index(min_distance)}")

    print(f"Ответ: {numbers[index]}")




def ZadachaS9_3():

    # size = tuple(int(x) for x in (input("Введите размеры матрицы через пробел: ")).split()) #повторение. Создание списка с помощью генератора
    size = tuple(map(lambda x: int(x),input("Введите размеры матрицы через пробел: ").split())) #повторение. Создание списка с помощью лямбда-функций

    matrix = np.random.randint(1,10, size) # создание матрицы размера size (size - кортеж из 2 чисел)
    print(f"{matrix}\t")

    # list1=list()
    # list2=list()
    # count=dict()

    # ВАРИАНТ 1 - решение через 2 списка, циклы
    # for array in matrix:
    #     for el in array:
    #         list2.append(el)
    #         if el not in list1:
    #             list1.append(el)
    # count=list(map(lambda x: list2.count(x), list1))
    # result = count.index(np.max(count))
   
    # print(list1)
    # print(count)
    # print(result)
    # print(f"Больше всех повторяется число: {list1[result]} - {count[result]} раз")

    # ВАРИАНТ 2 - решение через встроенный функционал

    uniq_list, uniq_counts = np.unique(matrix, return_counts=True)  # возвращает кортеж из уникальных элементов и количество повторений элементов 
    print(f'Уникальные элементы:   {uniq_list}')
    print(f"Количество повторений: {uniq_counts}")
    max_index=np.argmax(uniq_counts)                                # возвращает индекс максимального элемента
    print(f"Элемент {uniq_list[max_index]} встречает {uniq_counts[max_index]} раз.")



def ZadachaS9_4():
   matrix = np.random.randint(0,2, tuple(map(lambda x: int(x),input("Введите размеры матрицы через пробел: ").split())))
   print(matrix)
#    result = np.any(matrix == 5) # проверяет есть ли в массиве элементы равные 5
   result = matrix.any(axis=0) #параметр axis - оси, где 1 - строки, 0 - столбцы
   print(result)
   result = ~result # ~ применяет операцию not ко всем элементам
   print(result)

   if True in result:
       print("В матрице есть столбец(столбцы) из нулей.")
  

## diagmain

