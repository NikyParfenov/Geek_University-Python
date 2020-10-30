# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому
# использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
from collections import deque, OrderedDict

num_1 = list(input('Введите первое шестнадцатиричное число: ').upper())
num_2 = list(input('Введите второе шестнадцатиричное число: ').upper())
# num_1 = list('A2')
# num_2 = list('C4F')
print(f'Введенные числа: {num_1}, {num_2}')
hexadecimal = {'A': '10',
               'B': '11',
               'C': '12',
               'D': '13',
               'E': '14',
               'F': '15',
               }
decimal = dict(zip(hexadecimal.values(), hexadecimal.keys()))

length = max(len(num_1), len(num_2))
# блок приведения к одному размеру
if len(num_1) > len(num_2):
    while len(num_2) != len(num_1):
        num_2 = deque(num_2)
        num_2.appendleft('0')
elif len(num_2) > len(num_1):
    while len(num_2) != len(num_1):
        num_1 = deque(num_1)
        num_1.appendleft('0')

sum_dict = OrderedDict({length - i: 0 for i in range(length)})
for i in range(length):
    # блок замены A, B, C, D, E, F
    if hexadecimal.get(num_1[i]) is not None:
        num_1[i] = hexadecimal[num_1[i]]
    if hexadecimal.get(num_2[i]) is not None:
        num_2[i] = hexadecimal[num_2[i]]

    # блок суммирования
    temp = int(num_1[i]) + int(num_2[i])
    if temp < 16:
        sum_dict[length - i] += temp
    else:
        sum_dict[length - i] += temp - 16
        sum_dict[length - i + 1] += 1

result_sum = []
for i in range(length):
    if sum_dict[length - i] > 9:
        result_sum.append(decimal[str(sum_dict[length - i])])
    else:
        result_sum.append(sum_dict[length - i])
print(f'Сложение: {result_sum}')

# блок умножения
dec_num_1 = 0
dec_num_2 = 0
# перевод в десятичку
for i in range(length):
    dec_num_1 += int(num_1[length-i-1]) * 16**i
    dec_num_2 += int(num_2[length-i-1]) * 16**i
result = dec_num_1 * dec_num_2
result_mult = deque()
# перевод обратно в шестнадцатиричную
while result >= 16:
    temp = result % 16
    if 10 < temp < 16:
        temp = decimal[str(temp)]
    result_mult.appendleft(temp)
    result //= 16

if result < 10:
    result_mult.appendleft(result)
elif result < 16:
    result_mult.appendleft(decimal[str(result)])

print(f'Умножение: {list(result_mult)}')
