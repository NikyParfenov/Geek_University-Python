# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
# пользователя, а указать явно, в программе.

var_list = [12345, 'qwerty', True, 1.2345, None]

for i in var_list:
    print(f'Переменная <{i}> имеет тип {type(i)}')
