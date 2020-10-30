# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.
from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    vis_parents = [[]] * length
    cost[start] = 0
    min_cost = 0
    fin = start

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for i in range(length):
        j = i
        temp = deque()
        while parent[j] != fin and parent[j] != -1:
            temp.appendleft(parent[j])
            j = parent[j]
        temp.appendleft(fin if cost[i] != float('inf') else None)
        temp.append(i) if parent[i] != -1 else ()
        vis_parents[i] = list(temp)

    result = {}
    for z in range(length):
        result[z] = (cost[z], vis_parents[z])
    return result


s = int(input('Введите начальную вершину: '))
for key, value in dijkstra(g, s).items():
    print(f'Node: {key:>1}; Weight: {value[0]:>3}; Path: {value[1]}')
