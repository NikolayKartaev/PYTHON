# ФУНКЦИИ

import function as f  # импорт модуля и переименовывание его
from function import *  # импорт всех функций из модуля
from function import max1  # импорт указанной функции из модуля
import function  # импорт модуля


def sumNumbers(n, m="Hello"):
    print(m)
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

# print(sumNumbers(5))
# print(sumNumbers(5, 'Hi'))


def sumStr(*args):  # передача неизвестного числа аргументов
    result = ''
    for element in args:
        result += element
    return result

sumStr()

# print(sumStr("1,2","ff","555", "eee")) # Конкатенация строк (concatenate)


# МОДУЛЬНОСТЬ - создание нескольких файлов, в каждом из которых находятся функции работающие с определенной коллекции данных

# A
import function  # импорт модуля
print(function.max1(10, 15)) # вызов функции из модуля через точечную аннотацию

# B
from function import *  # импорт всех функций из модуля

# C
import function as f  # импорт модуля и переименовывание его
print(f.max1(10, 15)) # вызов функции из переименованного модуля через точечную аннотацию

# D
from function import max1  # импорт указанной функции из модуля
print(max1(10, 15))  # вызов импортированной функции


# РЕКУРСИИ - обязательно указывать базис - то место, когда рекурсия останавливается (выход)

def Fibonacci(N):
    if N in [1, 2]:
        return 1
    return Fibonacci(N-1) + Fibonacci(N-2)

def UseFibo():
    list = []
    for i in range(1, 11):
        list.append(Fibonacci(i))
    print(list)


# БЫСТРАЯ СОРТИРОВКА

def QuickSort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
    left = [i for i in list[1:] if i <= pivot]
    right = [i for i in list[1:] if i > pivot]
    return QuickSort(left) + [pivot] + QuickSort(right)

print(QuickSort([15,10,5]))
