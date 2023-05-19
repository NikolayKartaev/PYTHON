# Пример лямбда-функции
def Zadacha1():
    def math(function, a, b):
        print(f"RESULT = {function(a,b)}")
        
        
    # def calculator1(x,y):  --- стандартная функция
    #     return (x*x) + y
    # math(calculator1, 10, 25) 

    # calculator1 = lambda x,y: x*x + y   --- лямбда-функция присвоенная переменной
    # math(calculator1, 10, 25) 

    # def calculator2(x,y):  --- стандартная функция
    #     return (x+x) * y
    # math(calculator2, 10, 25) 

    # calculator2 = lambda x,y: (x+x) * y   --- лямбда-функция присвоенная переменной
    # math(calculator2, 10, 25) 

    math(lambda x,y: x*x + y, 10, 25) #   --- лямбда-функция вызывается в качестве аргумента функции        
    math(lambda x,y: (x+x) * y, 10, 25) #   --- лямбда-функция вызывается в качестве аргумента функции      

def Zadacha1():
    list1=[1,2,3,5,8,15,23,38]
    # list2=list(filter(lambda x:  x%2==0,list1))
    # list2=[(x,x**2) for x in list2]
    
    list2=[(x,x**2) for x in list(filter(lambda x:  x%2==0,list1))]

    
    print(list2)



def Zadacha2():
    # list1=input().split()
    # list1=list(map(lambda x: int(x), list1))
    list1=input()
    list1=list(map(int, list1.split()))
    
    print(list1)
    
Zadacha1()