# Списки

# Создание нового пустого списка
def Create():
    list_1 = []  
    list_2 = list()

 # Создание списка со значениями
list_3 = [1, 2, 3, 4, 5] 

# Вывод списка без скобочек и запятых - открытие списка
def PrintList():
    print(*list_3)  


# ФУНКЦИИ СПИСКОВ

# Добавление элемента в конец списка
def Append():
    list_3.append(6)  
    print(*list_3)

# Добавление элемента через цикл
def AppendLoop():
    list_3_1 = list()
    for i in range(10): 
        list_3_1.append(i)
        print(list_3_1)
    
# Удаление элемента с конца (.pop удаляет элемент и возвращает его )
def Pop():
    list_3.append(6)
    print(list_3)
    print(list_3.pop()) # Вывод значения удаленного элемента
    print(list_3)
    a = list_3.pop() # Возвращает значение удаленного элемента в переменную
    print(f"a = {a}")
    print(list_3)
    print(list_3.pop(0)) # Удаление элемента с индексом
    print(list_3)

# Вставляем элемент на указанный индекс (нужную позицию)
def Insert():
    print(list_3)
    list_3.insert(2,10)
    print(list_3)


print(list_3[-2:])
print(list_3[1::3])







# LIST COMPREHENSION - ГЕНЕРАТОР СПИСКА
def Comprehension ():
    N = int(input())
    list_4 = [a for a in range(1, N) if a % 2 == 0]
    list_5 = [(a, a**2) for a in range(1, N) if a % 3 == 0]

    print(list_4)
    print(list_5)




# Множества
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

q = a.union(b).difference(a.intersection(b))
