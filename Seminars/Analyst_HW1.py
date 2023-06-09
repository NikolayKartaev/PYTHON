# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def Task2():

    number = input("Введите трехзначное число: ")
    result = int(number[:1])+int(number[1:2])+int(number[2:3])

    print(f"Сумма цифр числа {number} равна {result}")


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def Task4():
    result=int(input("Введите общее количество изготовленных журавликов: "))
    while result%6!=0:
        print("Введите число кратное 6: ", end='')
        result=int(input())
    Pete=Sergey=int(result/6)
    Kate=(Pete+Sergey)*2
    
    print("Катя сделала {} журавликов, Петя сделал {} журавликов, Сережа сделал {} журавликов".format(Kate, Pete, Sergey))


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

def Task6():
    ticket_number=input("Введите шестизначное число:")
    while len(ticket_number)!=6:
        print("Введите шестизначное число: ", end='')
        ticket_number=input()
    first_half=second_half=0
    for i in range(int(len(ticket_number)/2)):
        first_half+=int(ticket_number[i])
        second_half+=int(ticket_number[int(i+len(ticket_number)/2)])
        
    if first_half==second_half:
        print("YES")
    else:
        print("NO")



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def Task8():
    n=int(input("Введите число n: "))
    m=int(input("Введите число m: "))
    k=int(input("Введите число k: "))
      
    if (k<m and k<n) or (n*m%2==0 and k%2!=0 and(k!=n and k!=m)) or (k%n!=0 and k%m!=0) or k==n*m:
        print("no")
    else:
        print('yes')
        


        
        




    
        

    