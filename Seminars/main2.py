import math
# СЕМИНАР 1. Аналитик. 18.05.2023
def Zadacha1():
    n=700
    m=750
    print(m//n+round(m/n,0))

    # print((m + n - 1) // n) 2 вариант
    
    # print(math.ceil(m / n)) 3 вариант
    
    # ceil - округляет 
    
    
def Zadacha3():
    a=int(input("Введите количество учеников в классе A: "))
    b=int(input("Введите количество учеников в классе B: "))
    c=int(input("Введите количество учеников в классе C: "))
    
    result = math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2)
    
    # result = a//2+a%2 + b//2+b%2 + c//2+c%2         2 вариант
    
    # s1 = (a + 1) // 2                               3 вариант
    # s2 = (b + 1) // 2
    # s3 = (c + 1) // 2
    # print(s1 + s2 + s3)

    print(result)
    
def Zadacha5():
    x=int(input("Введите номер вагона подсчета: "))
    y=int(input("Введите номер указанный в вагоне: "))
    if x==y:
        print("Нужна доп.информация")
    else:
        print(f"В электричке всего {x+y-1} вагонов")
       


def Zadacha7():
    x=int(input("Введите год: "))
    if x%4==0 and x%100!=0 or x%400==0:
        print("YES")
    else:
        print("NO")
        

# СЕМИНАР 2. Аналитик. 22.05.2023

def ZadachaS2_1():
    N=int(input("Введите число N: "))
    while N<0:
        N=int(input("Вы ввели неверное число.\nВведите неотрицательное число: "))
    result=i=1
    while i<=N:
        result= result*i
        i+=1   
    print(f"{N}! = {result}")
        

def ZadachaS2_2():
    A=int(input("Введите число A: "))
    while A<=1:
        A=int(input("Вы ввели неверное число.\nВведите число больше 1: "))
    x0 = 0
    x1 = 1
    x = 0
    i = 2
    while x < A:
        x = x0 + x1
        x0 = x1
        x1 = x
        i += 1
        if x > A:
            i = 0

    if i == 0:
        print(-1)
    else:
        print(i)
               
               
def ZadachaS2_3():   
    N=int(input())
    count=0
    x=int(input())
    while N>100 and N<1:
        N=int(input("Вы ввели неверное число.\nВведите верное: "))
    for i in range(N-1):
        x2=int(input())
        if x2>x:
            count+=1
        x=x2
    print(count)
             
             
def ZadachaS2_4():
    N=int(input("Введите количество арбузов: "))
    weight=int(input("Введите вес арбуза: "))
    max=min=weight
    for _ in range(N-1):
        weight=int(input("Введите вес арбуза: "))
        while weight>1000 and weight<1:
            weight=int(input("Вы ввели неверное число.\nВведите верное: "))
        
        if weight>max:
            max=weight
        if weight<min:
            min=weight
            
    print(max,min)
        
# СЕМИНАР 3. Аналитик. 25.05.2023

# Массивы в Python при помощи import array или import numpy

# ЗАДАЧА 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.

def ZadachaS3_1():
    
    numbers=list()
    for el in range (int(input("Введите размер списка: "))):
        numbers.append(int(input("Введите числа списка: ")))
        
    print(f"Разных чисел в списке: {len(set(numbers))}")
    
    


# ЗАДАЧА 2.
# 
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на |K| элементов вправо, если K – положительное и влево, если отрицательное.

def ZadachaS3_2():
    
    N=int(input("Введите количество "))
    list1=list(int(input()) for x in range(N))
    K=int(input())
    
    if K >0:
        list2= list1[K-1:]+list1[:K-1]
    else:
        list2= list1[-K:]+list1[:K+1]
        
    print(list2)


# data = [int(i) for i in input("Введите числа: ").split()]
# step = int(input("Введите кол-во сдвигов: "))
# step = step % len(data)
# data = [data[i - step] for i in range(len(data))]
# print(data)

#  0  1  2  3  4
# [1, 2, 3, 4, 5]
# -5  -4 -3 -2 -1
# k = 3
# [3, 4, 5, 1, 2]
#  2  3  4  0  1


# 0 - 3 = -3
# 1 - 3 = -2

# data = [int(i) for i in input("Введите числа: ").split()]
# for i in range((-1) * len(data), 0, +1):
#     print(data[i], i)


# ЗАДАЧА 3. 
# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, 
# {"V":"S009"}, {"VIII":"S007"}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

def ZadachaS3_3():

    list1= [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
            {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 
    
    list2=set()
    for el in list1:
        for key in el:
            list2.add(el[key])

    print(*list2)
    
# list1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"},
#            {"VIII":"S007"}]
# list2 = set()
# for el in list1:
#     list2.add(list(el.values())[0])
# print(*list2)
    
    
# ЗАДАЧА 4
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

def ZadachaS3_4():
    # list1=[int(input("Введите число: ")) for x in range(int(input("Введите количество элеметнов: ")))]
    list1=[int(x) for x in input("Введите числа через пробел: ").split()]
    count=0
    for i in range (1,len(list1)):
        if list1[i]>list1[i-1]:
            count+=1
    print(count)
    
    # вариант 2
    # count2 = sum([int(list1[i]>list1[i-1]) for i in range(1,len(list1))])
    # print(count2)
            
      
ZadachaS3_4()
