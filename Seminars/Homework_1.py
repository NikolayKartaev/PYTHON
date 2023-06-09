# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

from math import sqrt


def WeekDay():
    day = int(input("Введите день недели: "))
    while day < 1 or day > 7:
        day = int(input("Нет такого дня.\nВведите день недели: "))
    if day == 1:
        print("Понедельник")
    elif day == 2:
        print("Вторник")
    elif day == 3:
        print("Среда")
    elif day == 4:
        print("Четверг")
    elif day == 5:
        print("Пятница")
    elif day == 6:
        print("Суббота")
    else:
        print("Воскресенье")

def WeekDay2():
    weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = int(input("Введите день недели: "))
    while day < 0 or day > 7:
        day = int(input("Нет такого дня.\nВведите день недели: "))
    print(weekdays[day-1])


def WeekDay3():
    weekdays={"1":'Monday', "2":'Tuesday', "3":'Wednesday', "4":'Thursday', "5":'Friday', "6":'Saturday', "7":'Sunday'}
    day = input("Введите день недели: ")
    print(weekdays[day])



# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

def Distance():
    x1 = float(input("Введите координату первой точки по оси абцисс: "))
    y1 = float(input("Введите координату первой точки по оси ординат: "))
    x2 = float(input("Введите координату второй точки по оси абцисс: "))
    y2 = float(input("Введите координату второй точки по оси ординат: "))

    distance = sqrt((y2-y1)**2 + (x2-x1)**2)
    print(f"Расстояние между точками: {distance:.4f}")
    print(f"Расстояние между точками: {round(distance,4)}")

Distance()


# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0

def FindCoordinate():
    quarter = int(input("Введите номер координатной плоскости: "))
    while quarter < 1 or quarter > 4:
        quarter = int(
            input("Вы сделали неверный ввод\nВведите номер координатной плоскости: "))
    if quarter == 1:
        print("x ∈ (0;+∞), y ∈ (0;+∞)")
    elif quarter == 2:
        print("x ∈ (-∞;0), y ∈ (0;+∞)")
    elif quarter == 3:
        print("x ∈ (-∞;0), y ∈ (-∞;0)")
    elif quarter == 4:
        print("x ∈ (0;+∞), y ∈ (-∞;0)")


# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def PrintEven():
    n = int(input("Введите число N: "))
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i,  end=" ")


