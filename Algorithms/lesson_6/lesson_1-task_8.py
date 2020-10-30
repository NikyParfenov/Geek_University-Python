# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
from analyser import show_size_kwargs
import statistics


def mid_calc(a, b, c):
    if (b > a > c) or (b < a < c):
        mid = a
    elif (a > b > c) or (a < b < c):
        mid = b
    elif (a > c > b) or (a < c < b):
        mid = c
    else:
        # среднего числа нет (None), введены одинаковые числа
        mid = None
        print('Среди введенных чисел есть одинаковые!')
    print(f'Среднее из трёх введённых чисел: {mid}')
    return locals()


def stat_calc(a, b, c):
    num_list = [a, b, c]
    mid = statistics.median(num_list)
    print(f'Среднее из трёх введённых чисел: {mid}')
    return locals()


print('Введите три числа')
num_1 = float(input('Первое число: '))
num_2 = float(input('Второе число: '))
num_3 = float(input('Третье число: '))
show_size_kwargs(mid_calc(num_1, num_2, num_3))
show_size_kwargs(stat_calc(num_1, num_2, num_3))

'''
Система: win32;
Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
Введите три числа
Первое число: 1
Второе число: 5
Третье число: 9
Среднее из трёх введённых чисел: 5.0
name=a, type=<class 'float'>, size=24, object=1.0
name=b, type=<class 'float'>, size=24, object=5.0
name=c, type=<class 'float'>, size=24, object=9.0
name=mid, type=<class 'float'>, size=24, object=5.0
Total size=96
Среднее из трёх введённых чисел: 5.0
name=a, type=<class 'float'>, size=24, object=1.0
name=b, type=<class 'float'>, size=24, object=5.0
name=c, type=<class 'float'>, size=24, object=9.0
name=num_list, type=<class 'list'>, size=88, object=[1.0, 5.0, 9.0]
name=mid, type=<class 'float'>, size=24, object=5.0
Total size=184
'''
# Вывод: из-за того, что функция statistic.median() требует на вход список, то этот вариант потребяет памяти больше
