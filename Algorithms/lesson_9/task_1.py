# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.


def subline_counter(text: str, output=False) -> dict:
    """
    Функция подсчета числа подстрок в строке. Флаг output отвечает за вывод/невывод самих подстрок.
    :param text: str
    :param output: bool
    :return: dict
    """
    assert len(text) > 0, 'Вы задали пустую строку'
    subdict = {}
    z = 0

    # Ну раз нельзя использовать встроенные, напишем свою. За основу взял sha1 с урока, но сделал её рабочей
    def sec_hash_alg(data: str) -> int:
        """
        Функция из нормального текста делает какую-то хрень, в итоге получаем хеш. Магия!)))
        :param data: str
        :return: int
        """
        data = ''.join(format(ord(i), 'b') for i in data)
        h0 = 0x67452301
        h1 = 0xEFCDAB89
        h2 = 0x98BADCFE
        h3 = 0x10325476
        h4 = 0xC3D2E1F0
        length = len(data)
        data = bin(int(data, 2) << 1 + 1)

        if len(str(data)) % 512 > 448:
            data = bin(int(data, 2) << 64)
        data = bin(int(data, 2) << (448 - len(str(data)) % 512))
        data = bin(int(data, 2) << 64 + length - 5)

        part_512 = str(data[2:])
        w = []
        for i in range(16):
            w.append(int(part_512[:32]))
            part_512 = part_512[32:]
        for i in range(16, 80):
            w.append((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]) << 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (a << 5) + f + e + k + w[i]
            e = d
            d = c
            c = b << 30
            b = a
            a = temp

        h0 += a
        h1 += b
        h2 += c
        h3 += d
        h4 += e

        hash = h0 + h1 + h2 + h3 + h4
        return hash

    while z < len(text):
        for j in range(z + 1, len(text) + 1):
            sub = text[z:j]
            # Строку целиком не включаем, поэтому пропускаем вычисление и сравнивание хэша
            if len(sub) == len(text):
                continue
            h_sub = hex(sec_hash_alg(sub))
            counter = 0

            for i in range(len(text) - len(sub) + 1):
                if h_sub == hex(sec_hash_alg(text[i: i + len(sub)])):
                    counter += 1
            # Ислючаем возможное дублирование подстрок
            if subdict.get(sub) is None:
                subdict[sub] = counter
        z += 1

    if output:
        print('*' * 21)
        print('Подстрока: Вхождений')
        for key, value in subdict.items():
            print(f'{key}: {value}')
    return subdict


user_text = input('Введите текст: ')
# ВНИМАНИЕ! Если не нужен вывод подстрок и совпадений, то True поменять на False или убрать вообще
print(f'Обнаружено подстрок: {len(subline_counter(user_text, True).keys())}\n')
