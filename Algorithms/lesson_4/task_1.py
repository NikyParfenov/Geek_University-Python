# Задач 4 из урока 2. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n)
# вводится с клавиатуры. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.
import functools
import cProfile


# через цикл
def sum_half_num(counter: int) -> float:
    result = 0
    tmp = 1
    for i in range(counter):
        result += tmp
        tmp /= -2
    return result
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.sum_half_num(10)"
# 1000 loops, best of 5: 1.22 usec per loop
# 4 function calls in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.sum_half_num(100)"
# 1000 loops, best of 5: 8.24 usec per loop
# 4 function calls in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.sum_half_num(450)"
# 1000 loops, best of 5: 38.4 usec per loop
# 4 function calls in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.sum_half_num(900)"
# 1000 loops, best of 5: 80.5 usec per loop
# 4 function calls in 0.000 seconds


# через рекурсию
def recursion_func(counter: int) -> float:
    if counter == 1:

        return 1
    return 1 + recursion_func(counter - 1) / -2
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func(10)"
# 1000 loops, best of 5: 1.83 usec per loop
# 13 function calls (4 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func(100)"
# 1000 loops, best of 5: 19.8 usec per loop
# 103 function calls (4 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func(450)"
# 1000 loops, best of 5: 100 usec per loop
# 453 function calls (4 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func(900)"
# 1000 loops, best of 5: 213 usec per loop
# 903 function calls (4 primitive calls) in 0.001 seconds


# через рекурсию c докоратором
@functools.lru_cache(None)
def recursion_func_deco(counter: int) -> float:
    if counter == 1:
        return 1
    return 1 + recursion_func_deco(counter - 1) / -2
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_deco(10)"
# 1000 loops, best of 5: 104 nsec per loop
# 13 function calls (4 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_deco(100)"
# 1000 loops, best of 5: 104 nsec per loop
# 103 function calls (4 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_deco(450)"
# 1000 loops, best of 5: 106 nsec per loop
# 453 function calls (4 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_deco(900)"
# RecursionError: maximum recursion depth exceeded in comparison
# 499 function calls (4 primitive calls) in 0.000 seconds + RecursionError


# меморизация со словарем
def recursion_func_dict(counter):
    rec_dict = {1: 1}

    def _recursion_func_dict(counter):
        if counter in rec_dict:
            return rec_dict[counter]
        rec_dict[counter] = 1 + _recursion_func_dict(counter - 1) / -2
        return rec_dict[counter]

    return _recursion_func_dict(counter)
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_dict(10)"
# 1000 loops, best of 5: 3.29 usec per loop
# 14 function calls (5 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_dict(100)"
# 1000 loops, best of 5: 34.8 usec per loop
# 104 function calls (5 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_dict(450)"
# 1000 loops, best of 5: 170 usec per loop
# 454 function calls (5 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_dict(900)"
# 1000 loops, best of 5: 354 usec per loop
# RecursionError


# меморизация со списком
def recursion_func_list(counter):
    rec_list = [None] * 1000
    rec_list[1] = 1

    def _recursion_func_list(counter):
        if rec_list[counter] is None:
            rec_list[counter] = 1 + _recursion_func_list(counter - 1) / -2
        return rec_list[counter]

    return _recursion_func_list(counter)
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_list(10)"
# 1000 loops, best of 5: 8.79 usec per loop
# 14 function calls (5 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_list(100)"
# 1000 loops, best of 5: 35.2 usec per loop
# 104 function calls (5 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_list(450)"
# 1000 loops, best of 5: 152 usec per loop
# 454 function calls (5 primitive calls) in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_1" "task_1.recursion_func_list(900)"
# 1000 loops, best of 5: 322 usec per loop
# RecursionError


user_num = 10
# user_num = 100
# user_num = 450
# user_num = 900

print(f'Через стандартный цикл: {sum_half_num(user_num)}')
print(f'Через рекурсивную функ: {recursion_func(user_num)}')
print(f'Рекурсия + декоратор:   {recursion_func_deco(user_num)}')
print(f'Рекурсия + словарь:     {recursion_func_dict(user_num)}')
print(f'Рекурсия + список:      {recursion_func_list(user_num)}')
print('-' * 50)
cProfile.run('sum_half_num(user_num)')
cProfile.run('recursion_func(user_num)')
cProfile.run('recursion_func_deco(user_num)')
cProfile.run('recursion_func_dict(user_num)')
cProfile.run('recursion_func_list(user_num)')
