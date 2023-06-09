# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def Task1():
    listN = set(int(input("Введите число списка 1: ")) for _ in range(
        int(input("Введите количество элементов первого набора цифр: "))))
    listM = set(map(lambda x: int(x), input("Введите числа списка 2 через пробел: ").split()))

    newlist=list(listN.intersection(listM))
    newlist.sort()
    print(newlist)
    
import random
# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

def Task2():
    N = random.randint(3,10)
    harvest = [random.randint(1,15) for _ in range (N)]
    
    maximum = -1
    maxharv=list()
    
    for i in range(len(harvest)):
        if i in range (1, len(harvest)-1):
            if harvest[i]+harvest[i-1]+harvest[i+1] > maximum:
                maximum = harvest[i]+harvest[i-1]+harvest[i+1]
        elif i == (len(harvest)-1):
            if harvest[i]+harvest[i-1]+harvest[0] > maximum:
                maximum = harvest[i]+harvest[i-1]+harvest[0]
        else:
            if harvest[i]+harvest[len(harvest)-1]+harvest[i+1] > maximum:
                maximum = harvest[i]+harvest[i-1]+harvest[i+1]
        
    for i in range(len(harvest)):
        if i in range (1, len(harvest)-1):
            maxharv.append(harvest[i]+harvest[i-1]+harvest[i+1])
        elif i == (len(harvest)-1):
            maxharv.append(harvest[i]+harvest[i-1]+harvest[0])
        else:
            maxharv.append(harvest[i]+harvest[len(harvest)-1]+harvest[i+1])
            
        
            
    print(maximum, max(maxharv))
    
    
    
Task2()
