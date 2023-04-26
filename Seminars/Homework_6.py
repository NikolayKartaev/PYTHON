from random import randint
 
# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

def Task1():
    N = int(input("Введите число N: "))
    
    NN = int(str(N)+str(N))
    NNN = int(str(N)+str(N)+str(N)) 
    
    print(f"N={N}, выражение {N} + {NN} + {NNN} = {N + NN + NNN}")
    

# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет,
# есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def Task2():
    numbers = [randint(0,9) for _ in range(15)]
    string2find=input("Введите трёхзначное натуральное число: ")
    
    # for i in range(len(numbers)):               --- преобразование из списка в строку при помощи цикла
    #     string1+=str(numbers[i])
    
    # string1= (''.join(str(i) for i in numbers)) --- преобразование из списка в строку при помощи генератора
    
    string1= (''.join(map(str, numbers)))      #  --- преобразование из списка в строку при помощи map
    
    
    if string2find in string1:
            print(f"\nВ массиве {numbers} последовательность из трех элементов числа {string2find} - НАЙДЕНА\n")
    else:
            print(f"\nНЕ ОБНАРУЖЕНА последовательность из трех элементов числа {string2find} в массиве {numbers}\nZZ")
    

# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def prime_numbers(N):
    prime_list = []
    for n in range(2, N):
        count = 0
        for i in range(2, n//2+1):
            if n % i == 0:
                count += 1
        if count == 0:
            prime_list.append(n)
    return prime_list

print("Простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11:")
for a in prime_numbers(12):
    for b in prime_numbers(12):
        if b>a:
            fraction=str(a)+"/"+str(b) 
            print(fraction, end=" ")
