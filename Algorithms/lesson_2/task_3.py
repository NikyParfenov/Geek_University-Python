# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843. В заданиях 2, 3, 4, 7, 8, 9 пользователь вводит только натуральные числа.


def num_reverse(number: str) -> str:
    reversed_num = ''
    for i in number:
        reversed_num = f'{i}{reversed_num}'
    return reversed_num


num = input('Введите целое число: ')
print(num_reverse(num))
