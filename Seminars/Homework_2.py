# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Factorial():
    factorial = 1
    factorials = []
    N = int(input("Введите число N: "))
    for i in range(1, N+1):
        factorial = factorial*i
        factorials.append(factorial)
    print(factorials)


# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def Task2():
    print('| X | Y | Z | ¬(X ∧ Y) ∨ Z')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                print(f"| {x} | {y} | {z} |       {int(not(x and y) or z)} ")


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def Task3():

    firstString = input("Введите первую строку: ")
    secondString = input("Введите вторую строку: ")
    count = 0
    for char in firstString:
        for i in secondString:
            if i==char:
                count+=1
        print(count)


Task3()

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]


def Task4():
    N = int(input("Введите N: "))
    array = []
    for i in range(-N, N+1):
        array.append(i)
    print(array)
    for j in range(round(N/2)):
        temp = array[j+2]
        array[j+2] = array[j]
        array[j] = temp
