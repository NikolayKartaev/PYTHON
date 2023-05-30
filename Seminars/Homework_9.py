import numpy as np
from random import randint

# Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

def Task1():
    list_N = [randint(0, 15) for _ in range (int(input("Введите размер списка: ")))]
    unique_elements, count = np.unique(list_N, return_counts=True)
  
    print(f"\nИсходный список: {list_N}\n")
    print(f"Уникальные элементы: {unique_elements}")

    print(f"Всего уникальных элементов: {len(unique_elements)}\n")

    for el, counts in zip(unique_elements,count):
        print(f"Элемент {el}: его количество равно {counts}")
    

# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.
def Task2():
    matrix = np.random.randint(1,3,(5,5))
   
    print(f"{matrix}")
    unique_rows, unique_index = np.unique(matrix, axis =0, return_index=True)
    if len(unique_index) < matrix.shape[0]:
        print(f"В массиве есть одинаковые строки")
    else:
        print("В массиве нет одинаковых строк")
    

# Задача 3. Создайте двумерный массив случайного размера.
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

def Task3():
    matrix = np.random.randint(1,100,list(map(lambda x: int(x), input("Введите размеры двумерного массива через пробел: ").split())))
    print(matrix)
    
    max_index=np.argmax(matrix)
    min_index=np.argmin(matrix)

    print("Индекс максимального элемента: {}\nИндекс минимального элемента: {}".format(max_index,min_index))
    
    print(np.diagonal(matrix))
    
Task3()