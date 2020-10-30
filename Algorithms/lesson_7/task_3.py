# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
# сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
from random import randint
from math import inf
from statistics import median

m = 10
array = [randint(-100, 101) for _ in range(2 * m + 1)]
print(f'Исходный массив:\n{array}')
print(f'Проверка медианы через встроенную функцию: {median(array)}')

while len(array) > 1:
    min_item = inf
    max_item = - inf
    for i in range(len(array)):
        if array[i] > max_item:
            max_item = array[i]
        if array[i] < min_item:
            min_item = array[i]
    array.remove(max_item)
    array.remove(min_item)

    # строки 15-23 можно заменить на эти две строки ниже, но решил расписать поиск мин/макс через цикл
    # array.remove(max(array))
    # array.remove(min(array))

print(f'Медиана по алгоритму: {array[0]}')
