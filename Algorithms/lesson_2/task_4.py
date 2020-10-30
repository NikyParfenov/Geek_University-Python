# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с
# клавиатуры. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.


# пример через цикл
def sum_half_num(counter: int) -> float:
    result = 0
    tmp = 1
    for i in range(counter):
        result += tmp
        tmp /= -2
    return result


# пример через рекурсию
def recursion_func(counter: int) -> float:
    if counter == 1:
        return 1
    return 1 + recursion_func(counter - 1) / -2


user_num = int(input('Введите количество элементов: '))
print('Сумма элементов (ч/з цикл):', sum_half_num(user_num))
print('Сумма элементов (рекурсия):', recursion_func(user_num))
