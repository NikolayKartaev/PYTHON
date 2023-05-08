# СПИСКИ
# Создание нового пустого списка
def CreateList():
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
    print(list_3.pop())  # Вывод значения удаленного элемента
    print(list_3)
    a = list_3.pop()  # Возвращает значение удаленного элемента в переменную
    print(f"a = {a}")
    print(list_3)
    print(list_3.pop(0))  # Удаление элемента с индексом
    print(list_3)

# Вставляем элемент на указанный индекс (нужную позицию)
def Insert():
    print(list_3)
    list_3.insert(2, 10)
    print(list_3)

# Сделать смещение списка ну указанное количество элементов
def shift(list, steps): 
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            print(list)
            list.append(list.pop(0))
             
    else:
        for i in range(steps):
            print(list)
            list.insert(0, list.pop())


# Срезы списков
def PrintList_2():
    print(list_3[-2:])
    print(list_3[::3])


# КОРТЕЖ - неизменяемый список (занимает мало памяти, работает быстрее)

# Создание нового кортежа
t = ()         # пустой кортеж
t1 = (1,)     # кортеж со значениями


def ListTuple():
    v = [1, 2, 3]
    print(v)
    print(type(v))

    v = tuple(v)
    print(v)
    print(type(v))


# Множественное присваивание
a, b = 1, 2
a = b = 1


def Prisv():
    v = [5, 10, 15]
    v = tuple(v)
    a, b, c = v
    print(a, b, c)  # Печать трех переменных, равных элементам кортежа
    print(*v)  # Вывод кортежа без скобочек и запятых - распаковка кортежа

    for i in v:  # Вывод элементов списка/кортежа
        print(i, end=" ")

    print()

    for i in range(len(v)):  # Вывод значений с индексами списка/кортежа
        print(v[i], end=" ")
    print()


# СЛОВАРИ - неупорядоченные коллекции произвольных объемов с доступом по ключу (строка, число)

# Создание нового словаря
d = dict()
d = {}
d = {"ключ": "value"}


def Dictionary():
    d['key1'] = 'data1'  # Добавление значения в словарь по ключу (строка)
    print(d)
    d['key2'] = 'data2'  # Добавление значения в словарь по ключу (строка)
    print(d)

    # print(d['key1'])  # Печать значения по ключу
    # print(d['key2'])  # Печать значения по ключу

    # d['key2'] = 'data3'  # Перезаписать значения по ключу
    # d[123] = 100500  # Добавление значения в словарь по ключу (число)

    # del d['key1']  # Удаление значения по ключу
    # print(d)

    for i in d:
        print(i)

    for i in d:
        print(f"{i}: {d[i]}")
        print("{}: {}".format(i, d[i]))

    print(d.items())
    
Dictionary()

def Dictionary2():
    anketa = dict(Имя = input('Ваше имя: '),
                  Возраст = input('Ваш возраст: '),
                  Хобби = input('Ваше хобби: '),
                  Животное = input('Ваше любимое животное: '))
    print()
    for key, value in anketa.items():
                print("{}: {}".format(key,value))


def Dictionary3():
    dictionary = {}
    dictionary['name'] = input("Введите свое имя: ")
    dictionary['age'] = input("Введите свой возраст: ")
    dictionary['hobby'] = input("Введите свое хобби: ")
    dictionary['favorite_animal'] = input("Введите свое любимое животное: ")

    for k, v in dictionary.items():
        print(f"{k}: {v}")


# МНОЖЕСТВА - уникальные неупорядоченные значения


q = set()  # Создание множества
colors = {'red', 'green', 'blue'}  # Создание множества со значениями
f = frozenset(colors)  # Заморожденное множество

colors.add('red')  # Добавление значения (не уникаольное, не добавит)
colors.add('grey')  # Добавление значения (уникальное, добавит)

colors.remove('blue')  # Удаление значения
# Удаление значения (если не может удалить, то пропускает)
colors.discard('blue')
colors.clear()  # Удаление всех значений множества

# Операции со множествами
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}

c = a.copy()  # Копирование значений множества
u = a.union(b)  # Объединение множеств
i = a.intersection(b)  # Пересечение множеств
d1 = a.difference(b)  # Разность множеств a и b
d2 = b.difference(a)  # Разность множеств b и a
q = a.union(b).difference(a.intersection(b))


# LIST COMPREHENSION - ГЕНЕРАТОР СПИСКА

def Comprehension():
    N = int(input())
    list_4 = ["abc" for i in range(5)]
    list_5 = [i for i in range(1, 101) if i % 2 == 0]
    list_6 = [a for a in range(1, N) if a % 2 == 0]
    list_7 = [(a, a) for a in range(1, N)]
    list_8 = [(a, a**2) for a in range(1, N) if a % 3 == 0]
    list_9 = [i*2 for i in range(10)]
    list_10 = [i*2 for i in range(10)if i % 2 == 0]

    print(list_9)
    print(list_10)


# Indented block - блок с отступом
# IndentationErroe (Ошибка отступов)