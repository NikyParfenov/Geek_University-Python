# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import random, randint


def graph_maker(vertex):
    # создаем случайный список смежности, следим, чтобы ключ не совпадал с узлом из списка
    matrix = {i: [j for j in range(vertex) if round(random(), 0) > 0 and i != j] for i in range(vertex)}

    # если в списке смежности i-я вершина получилась без связи, насильно создаем одну случайную, согласно усл-ю задачи
    for check in range(vertex):
        if len(matrix[check]) == 0:
            while True:
                matrix[check] = [randint(0, vertex-1)]
                if check != matrix[check][0]:
                    break
    print('Список смежности:')
    for i, j in matrix.items():
        print(f'{i}: {j}')
    return matrix


def dfs(start, graph, is_visited=None):
    if is_visited is None:
        is_visited = [False] * len(graph)
    is_visited[start] = True
    for i in graph[start]:
        if not is_visited[i]:
            dfs(i, graph, is_visited)
    result = {i: is_visited[i] for i in range(len(graph))}
    return result


v = int(input('Введите число вершин: '))
g = graph_maker(v)
s = int(input('Введите начальную врешину: '))
for k, v in dfs(0, g).items():
    print(f'Узел: {k}; Пройден: {v}')
