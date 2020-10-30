# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл
# с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили
# творчество, фантазию и создали универсальный код для замера памяти.
import sys
print(f'Система: {sys.platform};\nPython: {sys.version}')


def show_size(x, level=0) -> None:
    print('\t' * level, f'type={x.__class__}, size={sys.getsizeof(x)}, object={x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
    elif not isinstance(x, str):
        for xx in x:
            show_size(xx, level + 1)


def show_size_args(*args) -> None:
    for arg in args:
        print(f'type={arg.__class__}, size={sys.getsizeof(arg)}, object={arg}')


def show_size_kwargs(kwargs_dict: dict) -> None:
    total_var_size = 0
    for i, value in kwargs_dict.items():
        print(f'name={i}, type={value.__class__}, size={sys.getsizeof(value)}, object={value}')
        total_var_size += sys.getsizeof(value)
    print(f'Total size={total_var_size}')
