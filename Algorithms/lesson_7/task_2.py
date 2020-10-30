# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
from random import randint


def merge_sort(array: list) -> list:
    """
    Функция сортирует массив слиянием
    :param array: list
    :return: list
    """
    def merge(left: list, right: list, result: list) -> list:
        """
        Функция рекурсивно сравнивает элементы и сортирует их в result
        :param left: list
        :param right: list
        :param result: list
        :return: list
        """
        result.append((left if left[0] < right[0] else right).pop(0))
        return merge(left, right, result) if left and right else result + left + right

    if len(array) == 1:
        return array
    else:
        return merge(merge_sort(array[int(len(array)/2):]), merge_sort(array[:int(len(array)/2)]), [])


# >>> Блок через лямбда-функцию
def merge_lambda(left: list, right: list, result: list) -> list:
    """
    Функция рекурсивно сравнивает элементы и сортирует их в result
    :param left: list
    :param right: list
    :param result: list
    :return: list
    """
    result.append((left if left[0] < right[0] else right).pop(0))
    return merge_lambda(left, right, result) if left and right else result + left + right


merge_sort_lambda = (lambda arr: arr if len(arr) == 1 else merge_lambda(merge_sort_lambda(arr[int(len(arr)/2):]),
                                                                        merge_sort_lambda(arr[:int(len(arr)/2)]),
                                                                        [])
                     )
# <<< Блок через лямбда-функцию

a = [randint(0, 50) for _ in range(30)]
print(f'Исходный массив:\n{a}')
print(f'Отсортированный массив (функция):\n{merge_sort(a)}')
print(f'Отсортированный массив (лямбда):\n{merge_sort_lambda(a)}')
