# 2. Закодируйте любую строку по алгоритму Хаффмана.
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def step(self, code, edge):
        # На путеводном камне написано:
        # налево пойдешь - 0 получишь, направо - 1
        self.left.step(code, edge + "0")
        self.right.step(code, edge + "1")


class Leaf(namedtuple("Leaf", ["letter"])):
    def step(self, code, edge):
        code[self.letter] = edge or "0"


def huffman(text):
    """
    Функция дробит текст на листья (Leaf), а затем пошагово собирается все это во вложенные друг в
    друга узлы (Node(Node(...)))
    :param text:
    :return:
    """
    huffman_list = []
    for letter, frequency in Counter(text).items():
        huffman_list.append((frequency, len(huffman_list), Leaf(letter)))
    huffman_list.sort(reverse=True)
    count = len(huffman_list)
    while len(huffman_list) > 1:
        freq_1, count_1, left = huffman_list.pop()
        freq_2, count_2, right = huffman_list.pop()
        huffman_list.append((freq_1 + freq_2, count, Node(left, right)))
        huffman_list.sort(reverse=True)
        count += 1

    code = {}
    if huffman_list:
        [(freq, count, root)] = huffman_list
        root.step(code, "")
    return code


user_text = 'beep boop beer!'
func = huffman(user_text)
print(func)
print(" ".join(func[letter] for letter in user_text))
