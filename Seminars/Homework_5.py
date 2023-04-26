from random import randint

# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

def Task1():
    print(list(filter(lambda x: x > 5, [randint(1, 10) for _ in range(10)])))



# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

def Task2():
    numbers=[randint(1,15) for _ in range(10)]
    print (numbers)
    
    checklist1=[]
    checklist1.append(numbers[randint(0,9)])
    print(checklist1)

    for i in numbers:
        if element>max(checklist1):
            checklist1.append(element) 
    
    print(checklist1)
    

# Task2()

nums = [randint(1,15) for _ in range(10)]
print(nums)
# Первый вариант

def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(nums))


# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадаю
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

def Task3():
    list1=[randint(1,15) for _ in range(10)]
    print(f"Исходный список чисел: {list1}")

    checklist1=[]
    checklist2=[]
    
    for i in range(len(list1)):
        if list1[i] not in checklist1:
            checklist1.append(list1[i])
        else:
            checklist2.append(list1[i])

    print(f"Список уникальных элементов: {checklist1}")
    print(f"{len(checklist2)+len(set(checklist2))} элемента(ов) совпадают")


