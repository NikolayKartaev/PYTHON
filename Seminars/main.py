# Задача 0
def Power():
    a = int(input("Введите число a: "))
    b=a*a
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


#Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.
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


#Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.
def Task2(a, b):
    count = 0
    for i in range(len(b)-len(a)+1):
        if a == b[i:i+len(a)]:
            count+= 1
    print (count)

# str1= input("Введите строку 1: ")
# str2= input("Введите строку 2: ")
#Task2(str1, str2)

def Task2_1():
    string = input("Введите строку: ")
    phrase = input("Введите фразу: ")
    count = 0
    for i in range(len(phrase)-len(string)+1):
        if string == phrase[i:i+len(string)]:
            count += 1
    print(count)


#Вывод по элементам
# phrase = input("Введите фразу: ")
# for el in phrase:
#     print(el, end='')

# print()
# #Вывод элементов с индексами
# for i in range(len(phrase)):
#     print(phrase[i], end='')


#Вывод дробного числа с указанием количества знаков после запятой без округления
def float():
    fl = 2.715415864
    print(f"{fl:.6f}")


#Задача 3. Дано число N. Заполните список длиной N элементами 1, -3, 9, -27, 81, -243...
def Task3_1():
    N = int(input())
    array=[]
    for i in range(N):
        array.append((-3)**i)
        if i==N-1:
            print (array)
        
def Task3_2():
    N = int(input())
    for i in range(N):
            print(f"{(-3)**i}", end=' ')



#Задача 4. Найдите все числа до 10000, у который количество делителей равно 10.

def Task0_3(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    return count

def Task4():
    countnumbers=0
    for number in range(1,10001):
        if Task0_3(number)==10:
            countnumbers+=1
            print(f"{number}\t", end='')
    print()
    print(f"Количество чисел с делителем 10 равно: {countnumbers}")


def Task4_1():
    countnumbers=0
    for numbers in range(1,10001):
        countdivs=0
        for i in range (1, numbers+1):
            if numbers%i==0:
                countdivs+=1        
        if countdivs==10:
            countnumbers+=1
            print(f"{numbers}\t", end='')
    print()
    print(countnumbers)


