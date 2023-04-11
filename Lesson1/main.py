# a = 5
# b = 10
# c = 20.5
# print(f"{a} + {b} + {c} = {a+b+c}")
# print("{} + {} + {} = {}".format(a, b, c, a+b+c))

# d = input()
# f = input("Введите число")

# r = 15
# print(r+5)
# print(type(r))

# r = str(r)
# print(r+"5")
# print(type(r))

# n = int(input())
# flag = True
# i = 2

# while flag:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n//2:
#         print(n)
#         flag = False
#     i += 1


# for i in range(5):
#     line=""
#     for j in range(5):
#         line+="*"
#     print(line)

# text = '123456789'
# print(text[0::3])
# n = 1
# print(n)
# print(type(n))
# print()

# n = 2.5
# print(n)
# print(type(n))
# print()

# n = "'example1'"
# print(n)
# print(type(n))
# print()

# n = '"example2"'
# print(n)
# print(type(n))
# print()

# n = '\'example3\''
# print(n)
# print(type(n))
# print()

# a = 5
# b = 10.50
# c = 'hello'
# print (f"{a} - {b} - {c}")
# print ("{} - {} - {}".format(a,b,c))


# print("Введите число a:")
# a = input()
# b = input("Введите число b: ")
# c = 5.2
# d = 5
# print(f"a = {a}")
# print(type(a))

# print(f"b = {b}")
# print(type(b))

# print(f"c = {c}")
# print(type(c))

# c = int(c)
# print(type(c))

# print(f"d = {d}")
# print(type(d))


# print("Введите число a:")
# a = int(input())
# b = int(input("Введите число b: "))
# print(a, "+", b, "=", a+b)


# a = 5.542434345
# b = 4.55322245
# print(round(a*b, 4))

def CheckEvenOrOdd(value):
    if value % 2 == 0:
        return ("четное")
    else:
        return ("нечетное")


def Task2_1(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            if i % 2 == 0:
                print(f"{i} - четное")
            else:
                print(f"{i} - нечетное")
    print(f"Количество делителей: {count} - by Task2_1")


def Task2_2(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1
            print(f"{i} - {CheckEvenOrOdd(i)}")
    print(f"Количество делителей: {count} - by Task2_2")

# number = int(input("Введите число: "))
# print()
# Task2_1(number)
# print()
# Task2_2(number)


def FindBoolValue(a, b):
    result = not a or b
    if result == True:
        return 1
    else:
        return 0


print('X Y R')
for x in range(2):
    for y in range(2):
        print(x, end=' ')
        print(y, end=' ')
        print(FindBoolValue(x, y))

# x = int(input("Введите X: "))
# y = int(input("Введите Y: "))
# FindBoolValue(x,y)

print()
for x in range(2):
    for y in range(2):
        print(f"{x} {y} {int(not x or y)}")
