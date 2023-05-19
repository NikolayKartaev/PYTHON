# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5

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

def prime(N): #НАХОДИМ СПИСОК ПРОСТЫХ ЧИСЕЛ
    primelist=list()
    for i in range(2,N):
        count=0
        for j in range(2, i//2+1 ):
            if  i%j==0:
                count+=1
        if count==0:
            primelist.append(i)
    print(primelist)
    
def Zadacha():
    L=int(input())
    ListM=list()
    primenumber=2
    while L !=1:
        if L%primenumber==0:
            ListM.append(primenumber)
            L//=primenumber
        else:
            primenumber+=1
    
    print("{}".format(list(el for el in ListM)))
    
        



def find_multiplier(N):
    LIST = []
    prime = 2
    while N !=1:
        if N % prime == 0:
            LIST.append(prime)
            N //= prime
        else:
            prime += 1
    if N > 1:
        LIST.append(N)
    return LIST


# N = int(input("Введите число N: "))
# print(f"{N} -> {find_multiplier(N)}")


# Задача 2. В первом списке находится информация об ассортименте мороженного, во втором списке - информация о том, какое мороженное есть на складе.
# Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. "Сливочное", «Бурёнка", «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»




def Task2():
    product_range = ["«Сливочное»", "«Бурёнка»", "«Вафелька»", "«Сладкоежка»"]
    in_stock = ["«Сливочное»", "«Вафелька»", "«Сладкоежка»"]
    out_of_stock = set(product_range).difference(set(in_stock))
    print(*out_of_stock)


# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 0.001-> 3.142 0.00001-> 3.14159

def Task3():
    pi = 3.141592653589793238462643383279
    n = str(input("Введите десятичную дробь: ")).split(".")
    print(round(pi, len(n[1])))
