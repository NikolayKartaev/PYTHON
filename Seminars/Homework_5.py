from random import randint

def Task1():
    numbers = [randint(1,10) for _ in range(10)]
    print(numbers)  
    print(list(filter(lambda x: x>5, numbers)))
    
Task1()
    