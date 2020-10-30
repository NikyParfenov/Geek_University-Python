# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
# наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import deque

companies = {}
comp_num = int(input('Введите число компаний: '))
average_profit = 0

for i in range(comp_num):
    comp = input(f'Имя компании {i+1}: ')
    companies[comp] = sum(map(float, input('Прибыль компании за 4 квартала через пробел: ').split(' ')))
    average_profit += companies[comp]

average_profit /= comp_num

# создаем очередь из прибылей больше/меньше средней
comparison = deque('0')
for i, value in companies.items():
    if value >= average_profit:
        comparison.append(i)
    else:
        comparison.appendleft(i)

print(companies)
print(f'Компании с прибылью меньше средней {average_profit}:')
for i, item in enumerate(comparison):
    if i == comparison.index('0'):
        print(f'\nКомпании с прибылью выше или равной средней {average_profit}:')
        continue
    print(item, end='; ')
