# Задача 0
# a = int(input("Введите число a: "))
# b=a*a
# print(f"Квадрат {a} = {b}")

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


numbers = [5,-4,8,9,-9,4,7,0,1,-5]
for i in numbers:
    print(i)
    
    

def CheckEvenOrOdd(value):
    if value % 2 == 0:
        return ("четное")
    else:
        return ("нечетное")


def Task2_1(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            if i % 2 == 0:
                print(f"{i} - четное")
            else:
                print(f"{i} - нечетное")
    print(f"Количество делителей: {count} - by Task2_1")


def Task2_2(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            print(f"{i} - {CheckEvenOrOdd(i)}")
    print(f"Количество делителей: {count} - by Task2_2")

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


print('X Y R')
for x in range(2):
    for y in range(2):
        print(x, end=' ')
        print(y, end=' ')
        print(FindBoolValue(x, y))

# x = int(input("Введите X: "))
# y = int(input("Введите Y: "))
# FindBoolValue(x,y)

print()
for x in range(2):
    for y in range(2):
        print(f"{x} {y} {int(not x or y)}")
