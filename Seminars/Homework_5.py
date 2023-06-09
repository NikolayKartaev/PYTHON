from random import randint

# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

def Task1():
    random_list=[randint(1, 10) for _ in range(10)]
    print(f"\nИсходный список случайных чисел: {random_list}\nЭлементы больше 5 -> {list(filter(lambda x: x > 5, random_list))}\n")


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.


def Task2():
    numbers=[randint(1,15) for _ in range(10)]
    print (f"\nИсходный список случайных чисел:{numbers}")
    
    checklist1=[]
    rand_index=randint(0,len(numbers)-2)
    
    while numbers[rand_index]>=max(numbers[rand_index:]):
        rand_index=randint(0,len(numbers)-2)
    
    checklist1.append(numbers[rand_index])

    for i in range (rand_index,len(numbers)):
        if numbers[i]>max(checklist1):
            checklist1.append(numbers[i]) 
            
    print(f"Случайная возрастающая последовательность начиная с позиции {rand_index}: {checklist1}\n")
    


# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаю
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

def Task3():
    list1=[randint(1,15) for _ in range(10)]
    print(f"\nИсходный список чисел: {list1}")

    # checklist1=[]
    # checklist2=[]
    
    # for i in range(len(list1)):
    #     if list1[i] not in checklist1:
    #         checklist1.append(list1[i])
    #     else:
    #         checklist2.append(list1[i])

    # print(f"Список уникальных элементов: {checklist1}")
    # print(f"{len(checklist2)+len(set(checklist2))} элемента(ов) совпадают\n")
    
    print(len(list(filter(lambda x: list1.count(x)>1, list1))))
    print((list(map(lambda x: list1.count(x)>1, list1))).count(True))
    


