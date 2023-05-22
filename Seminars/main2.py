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
        
    