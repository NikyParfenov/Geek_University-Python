# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.
from analyser import show_size_args
from collections import deque


def num_reverse(number: str) -> str:
    reversed_num = ''
    for i in number:
        reversed_num = f'{i}{reversed_num}'
    return reversed_num


num = input('Введите целое число: ')
# №1 вариант со своей функцией
my_func_reverse = num_reverse(num)
print(f'Вариант с функцией: {my_func_reverse}')

# №2 вариант со встроенной функцией list
py_list_reverse = list(num)
py_list_reverse.reverse()
print(f'Вариант с list: {"".join(py_list_reverse)}')

# №3 вариант с deque
py_deque_reverse = deque(num)
py_deque_reverse.reverse()
print(f'Вариант с deque: {"".join(py_deque_reverse)}')

show_size_args(my_func_reverse, py_list_reverse, py_deque_reverse)

'''
Система: win32;
Python: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
Введите целое число: 1234567890
Вариант с функцией: 0987654321
Вариант с list: 0987654321
Вариант с deque: 0987654321
type=<class 'str'>, size = 59, object=0987654321
type=<class 'list'>, size = 200, object=['0', '9', '8', '7', '6', '5', '4', '3', '2', '1']
type=<class 'collections.deque'>, size = 632, object=deque(['0', '9', '8', '7', '6', '5', '4', '3', '2', '1'])
 '''
# Вывод: обычная работа со строкой наиболее оптимальна в данном случае.
# Интересно, что очередь deque ест неприлично много памяти...
