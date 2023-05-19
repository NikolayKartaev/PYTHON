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



def Zadacha1a():
    list1=[1,2,3,5,8,15,23,38]
    list2=[]
    for el in list1:
        if not(el%2!=0):
            list2.append((el,el**2))
    print(list2)

def Zadacha1b():
    list1=["1","2","3","5","8","15","23","38"]

    def select(function, list): #   --- какая-то функция, какой-то список
        return [function(x) for x in list] #   --- принцип работы функции map (ко всем x списка list применяем функцию function)
    
    def where(function, list): #   --- какая-то функция, какой-то список
        return [x for x in list if function(x)] #   --- принцип работы функции filter (возвращает те x, которые удовлетворяют условию function(x))
    
    list2=select(int,list1) #   --- ко всем элементам list1 применяется функция int - элементы переводятся в int
    print(list2)
    list2=where(lambda x:x%2==0,list2) #   --- ко всем элементам list2 применяется лямбда-функция, которая возвращает те элементы, которые удовлетворяют условию x%2==0
    print(list2)
    list2=select(lambda x:(x,x**2),list2) #   --- ко всем элементам list2 применяется лямбда-функция, которая переводит каждый элемент в кортеж из элемента и его квадрата
    print(list2)

def Zadacha1c():
    list1=[1,2,3,5,8,15,23,38]
    # list2=list(filter(lambda x:  x%2==0,list1))
    # list2=[(x,x**2) for x in list2]
    list2=[(x,x**2) for x in list(filter(lambda x:  x%2==0,list1))]  
    print(list2)




def Zadacha2():
    # list1=input().split()
    # list1=list(map(lambda x: int(x), list1))
    
    list1=list(map(int, input().split()))   #   --- преобразование каждого введенного элемента списка строк в int
    list1=[int(x) for x in input().split()] #   --- создание списка из преобразованных в int элементов

    print(list1)
    

def ZIP():
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    list3=input().split()

    result=list(zip(list1,list2,list3))
    print(result)


