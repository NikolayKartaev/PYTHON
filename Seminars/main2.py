import math

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
        

