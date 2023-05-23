# Задача 1. Создайте пользовательский аналог метода map().
def Zadacha1():
    def function_map(function, our_list):
        return [function(x) for x in our_list]

    list1=[int(input("Элементы списка: ")) for _ in range(int(input("Кол-во элементов списка: ")))]
    print(f"Исходный список: {list1}")
    print(f"Конечный список: {function_map(lambda x: x+5,list1)}") # проверяем работоспособность

# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
def Zadacha2():
    def times(N, greeting1):
        def repeat(function):
            def decorator():
                for _ in range(N):
                    function(greeting1)
            return decorator
        return repeat

    @times(int(input("Cколько раз повторять? ")), input("Что повторять: "))
    def greetings(greet):
        print(greet,end='\t')
        
    greetings()

    
# Задача 3. Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000.
# Когда игрок угадывает его, бот выводит количество сделанных ходов.