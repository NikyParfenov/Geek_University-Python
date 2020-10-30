# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы. Примечание: попытайтесь решить задания
# без использования функций max, min, sum, sorted и их аналогов, в том числе написанных самостоятельно. В задачах 3,
# 4, 5, 6, 9, если искомый элемент(ы) встречается в массиве несколько раз, используйте один любой по вашему выбору.

from random import randint
from math import inf

# Задаем массив случайных элементов, вводим вспомогательный массив минимальных значений столбцов
matrix_rows = 10
matrix_lines = 5
matrix = [[randint(-100, 100) for _ in range(matrix_rows)] for _ in range(matrix_lines)]
min_items_array = [inf for _ in range(matrix_rows)]
result_item = -inf

# вывод матрицы
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

# Нахождение минимальных элементов в каждом столбце.
# Чтобы сразу искать максимум, внешний цикл будет по столбцам, внутренний по строкам.
for row in range(matrix_rows):
    for line in range(matrix_lines):
        if matrix[line][row] < min_items_array[row]:
            min_items_array[row] = matrix[line][row]
    # поиск максимального элемента среди минимальных
    if result_item < min_items_array[row]:
        result_item = min_items_array[row]

print(f' Максимальный элемент {result_item} среди минимальных элементов в столбцах:\n {min_items_array}')
