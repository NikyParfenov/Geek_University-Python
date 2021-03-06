# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу. Примечание: попытайтесь решить задания без использования функций max, min, sum, sorted и их аналогов,
# в том числе написанных самостоятельно.

# Ввод не проверяется и не корректируется. Подразумевается, что введут корректные значения.
matrix = [input(f'Введите 4 целочисленных элемента {i+1}-й строки через пробел: ').split(' ') for i in range(4)]

# Расчет последнего столбца
for line in matrix:
    temp = 0
    for item in line:
        temp += int(item)
        # print(f'{item:>4}', end='')
    line.append(f'{temp}')
    # print(f'{line[-1]:>4}')

# Вывод матрицы. Вместо второго прогона цикла, матрицу можно вывести двумя print'ами в цикле выше.
for line in matrix:
    for item in line:
        print(f'{item:>4}', end='')
    print()
