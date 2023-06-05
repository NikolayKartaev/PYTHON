import math
from random import randint


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
    # count=0
    # for i in range (1,len(list1)):
    #     if list1[i]>list1[i-1]:
    #         count+=1
    # print(count)
    
    # вариант 2
    count2 = sum([int(list1[i]>list1[i-1]) for i in range(1,len(list1))])
    print(count2)
            



# СЕМИНАР 4. Аналитик. 29.05.2023

def ZadachaS4_1():
    string=input("Введите слово: ").split()
  
    counter=dict()
           
    for char in string:
        if char in counter:
            print(f'{char}_{counter[char]}', end=' ')
            counter[char] += 1
    else: # ключа i нет внутри словаря result
        print(char, end=' ')
        counter[char] = 1

    #вариант 1
    
# for i in word:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#         result[i] += 1
#     else: # ключа i нет внутри словаря result
#         print(i, end=' ')
#         result[i] = 1

#         #вариант 2
# for i in word:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else: # ключа i нет внутри словаря result
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1



def ZadachaS4_2():
    text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
    print(len(set(((text).lower().split()))))



def ZadachaS4_3():

    n = int(input())
    max_number = n
    while n != 0:
        n = int(input())
        if n > max_number:
            max_number=n
    print(max_number)


# СЕМИНАР 5. 01.06.2023

def ZadachaS5_1():
    def Fibo(a):
        if a in range(0,2): return 0
        elif a == 2: return 1
        else: return Fibo(a-1)+ Fibo(a-2)
    
    n=int(input())
    print([Fibo(i) for i in range(1,n+1)])
    
    
    
def ZadachaS5_2():
    marks = [randint(1,5) for x in range(int(input()))]
    print(marks)
    maxi=max(marks)
    mini = min(marks)
    for i in range(len(marks)):
        if marks[i] == maxi:
            marks[i] = mini
            
    print(marks)
    
    
def ZadachaS5_3():
    N=int(input())
    count=0
    for i in range(2,N//2+1):
        if N%i==0:
            count+=1
    if count>0:
        print(f"Число {N} не является простым")
    else: print(f"Число {N} простое")
    
    
    
def ZadachaS5_4():
    def reverse(n):
        if n==0: return ""
        k = (input())
        return reverse(n-1) + f"{k}"
    
    n = int(input())
    print(reverse(n))
    


# СЕМИНАР 6. 05.06.2023

def ZadachaS6_1():
    list1 = [randint(1,25) for _ in range(int(input("Введите количество элементов первого списка: ")))]  
    list2 = [randint(1,25) for _ in range(int(input("Введите количество элементов второго списка: ")))]
    
    for i in list1:
        if i not in list2:
            print(f"{i}",end=',')
            
    print([i for i in list1 if i not in list2]) ###### ПОВТОРЕНИЕ

# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве выведет количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел. 
# Ввод: 			Ввод:
# 5				5
# 1 2 3 4 5			1 5 1 5 1
# Вывод:			Вывод:
# 0				2

def ZadachaS6_2():
    list1=[randint(1,26) for _ in range(int(input("Введите количество элементов: ")))]
    count=0
    # for i in range(1,len(list1)-1):
    #     if list1[i]>list1[i-1] and list1[i]>list1[i+1]:
    #         count+=1
    
    count = sum([int(list1[i]>list1[i-1] and list1[i]>list1[i+1]) for i in range(1,len(list1)-1)])
    print(list1)
    print(count)
        
        
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод:			Вывод:
# 1 2 3 2 3			2

def ZadachaS6_3():
    list1=[i for i in input("Введите числа через пробел: ").split()]
    dict1=dict()
    
    for i in list1:
        dict1[i] = list1.count(i)
        
    print(dict1)
    
    print(sum([i//2 for i in dict1.values()]))

# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, 
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной 
# в # строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# Ввод:			Вывод:
# 300			220 284


def ZadachaS6_4():
    n = int(input())
    list_1 = list()
    for i in range(n):
        summa = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                summa += j
        list_1.append((i, summa))
    print(list_1)
    for i in range(len(list_1)):
        for j in range(i, len(list_1)):
            if i != j and list_1[i][0] == list_1[j][1] and list_1[i][1] == list_1[j][0]:
                print(*list_1[i])

ZadachaS6_4()
