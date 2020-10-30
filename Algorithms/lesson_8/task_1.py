# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


def handshake(number):
    matrix_hand = [[(1 if i != j else 0) for j in range(number)] for i in range(number)]
    print('Граф друзей:')
    for i in range(number):
        print(matrix_hand[i])
    if number == 0:
        print('Тебя не существует')
    elif number == 1:
        print('У тебя нет друзей, смирись')
    else:
        # суммируем элементы матрицы смежности и делим на 2, чтобы убрать задвоение
        # (i-й здоровается с j-м, а j-й здоровается с i-м должно считаться за одно рукопожатие)
        print(f'Число рукопожатий: {int(sum(map(sum, matrix_hand)) / 2)}')


n = int(input('Введите число людей: '))
handshake(n)
