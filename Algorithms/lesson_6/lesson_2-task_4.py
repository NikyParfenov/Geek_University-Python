# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.
from analyser import show_size_kwargs


# пример через цикл
def sum_half_num(counter: int) -> tuple:
    result = 0
    tmp = 1
    for i in range(counter):
        result += tmp
        tmp /= -2
    var = locals()
    return result, var


# пример через рекурсию
def recursion_func(counter: int) -> tuple:
    if counter == 1:
        var = locals()
        return 1, var
    var = locals()
    return 1 + recursion_func(counter - 1)[0] / -2, var


user_num = int(input('Введите количество элементов: '))

print('Сумма элементов (ч/з цикл):', sum_half_num(user_num)[0])
show_size_kwargs(sum_half_num(user_num)[1])

print('Сумма элементов (рекурсия):', recursion_func(user_num)[0])
show_size_kwargs(recursion_func(user_num)[1])

'''
Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
Введите количество элементов: 5
Сумма элементов (ч/з цикл): 0.6875
name=counter, type=<class 'int'>, size=28, object=5
name=result, type=<class 'float'>, size=24, object=0.6875
name=tmp, type=<class 'float'>, size=24, object=-0.03125
name=i, type=<class 'int'>, size=28, object=4
Total size=104
Сумма элементов (рекурсия): 0.6875
name=counter, type=<class 'int'>, size=28, object=5
Total size=28
'''
# Вывод: с точки зрения затрат памяти на переменные, рекурсия определенно выигрывает.
