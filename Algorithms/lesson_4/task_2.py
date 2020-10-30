# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
# его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
import cProfile


def test(func) -> None:
    """
    Функция проверяет корректность вычисления функцией первых 25-ти простых чисел
    :param func: function
    :return: None
    """
    test_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i, item in enumerate(test_array):
        assert item == func(i + 1)
    print(f'Test of {func.__name__} function is OK!')


def eratosfen(number: int) -> int:
    """
    Поиск простого числа по индексу с помощью решета Эратосфена
    :param number: int
    :return: int
    """
    array = [0, 0]
    n = 2
    # расширяем исходный массив и записываем очередное простое число до тех пор, пока требуемые индекс не совпадет
    # с размером множества +1 (за счет нуля)
    while len(set(array)) < number + 1:
        array.append(n)
        i = 2
        while i < len(array):
            if array[i] != 0:
                j = i + i
                while j < len(array):
                    array[j] = 0
                    j = j + i
            i += 1
        n += 1
    array = list(set(array))
    array.remove(0)
    array.sort()
    # print(array)
    return array[-1]
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.eratosfen(10)"
# 1000 loops, best of 5: 139 usec per loop
# 1047 function calls in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.eratosfen(25)"
# 1000 loops, best of 5: 1.6 msec per loop
# 12472 function calls in 0.003 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.eratosfen(50)"
# 1000 loops, best of 5: 10.2 msec per loop
# 73475 function calls in 0.016 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.eratosfen(100)"
# 1000 loops, best of 5: 67 msec per loop
# 431878 function calls in 0.101 seconds

def simple_num(number: int) -> int:
    """
    Поиск простого числа по индексу с помощью оценки остатка от деления
    :param number: int
    :return: int
    """
    array = [2]
    i = 3
    while len(array) < number:
        flag = 0
        for j in range(len(array)):
            if i % array[j] == 0:
                flag = 1
                break
        if flag == 0:
            array.append(i)
        i += 1
    # print(array)
    return array[-1]
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.simple_num(10)"
# 1000 loops, best of 5: 17.5 usec per loop
# 68 function calls in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.simple_num(25)"
# 1000 loops, best of 5: 69.9 usec per loop
# 219 function calls in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.simple_num(50)"
# 1000 loops, best of 5: 200 usec per loop
# 508 function calls in 0.000 seconds
#
# D:\GeekBrains\Geek_University\lesson_4>python -m timeit -n 1000 -s "import task_2" "task_2.simple_num(100)"
# 1000 loops, best of 5: 617 usec per loop
# 1182 function calls in 0.001 seconds


# тест от 1го до 25го простого числа
test(eratosfen)
test(simple_num)

user_number = 10
# user_number = 25
# user_number = 50
# user_number = 100

print(f'Решето Эратосфена: {user_number}-й элемент {eratosfen(user_number)}')
print(f'Проверка делением: {user_number}-й элемент {simple_num(user_number)}')
print('-' * 50)
cProfile.run('eratosfen(user_number)')
cProfile.run('simple_num(user_number)')
