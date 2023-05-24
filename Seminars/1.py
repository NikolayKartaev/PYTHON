def counter(function1):
    def wrap(*args, **kwargs):
        wrap.count_function += 1
        return function1(*args, **kwargs)
    wrap.count_function = 0
    return wrap

@counter
def FUN(a,b):
    return a+b


FUN(10,14)
FUN(10,14)

print('Число вызовов функции:', FUN.count_function)
