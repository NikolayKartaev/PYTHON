# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

def Zadacha10():
    n = int(input("Введите n: "))
    x = int(input("Введите число монеток, лежащих вверх решкой: "))
    y = n - x
    if x>y:
        print(f"Перевернуть необходимо: {y} монеток")
    else:
        print(f"Перевернуть необходимо: {x} монеток")
        
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

def Zadacha12():
    S=int(input("Введите сумму загаданных чисел: "))
    P=int(input("Введите произведение загаданных чисел: "))
    
    for X in range(1,1001):
        for Y in range(1,1001):
            if X*Y==P and X+Y==S:
                return f"Загаданные числа: {X}, {Y}"

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
def Zadacha14():
    N=int(input("Введите число N: "))
    k=0   
    print(f"Целые степени двойки от 1 до {N}: ", end=" ")
    while 2**k<=N:
        print(2**k, end=" ")
        k+=1
        