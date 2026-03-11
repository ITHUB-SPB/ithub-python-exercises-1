"""
RLE (Run-length encoding) это простой способ сжатия данных, где последовательности одинаковых символов заменяются следующим образом:

"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"

Здесь мы перешли от 53 символов к всего лишь 13.

RLE кодирует без потерь, позволяя в последствии легко и безопасно декодировать сжатые данные:

          кодирование     декодирование
---------------v----------------v-------------------
"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"

Реализуйте методы для кодирования и восстановления строк.
"""
from itertools import count


def decode(encoded_string: str) -> str:
    """Декодирует (восстанавливает) строку.

    :param encoded_string: str - строка, сжатая алгоритмом RLE.
    :return: str - восстановленная строка.
    """
    result = ''
    number = ''

    for char in encoded_string:
        if char.isdigit():
            number += char
        else:
            if number == '':
                result += char
            else:
                result += char * int(number)
                number = ''

    return result


def encode(initial_string: str) -> str:
    """Кодирует (сжимает) строку.

    :param initial_string: str - исходная строка, содержит символы [a-zA-Z ].
    :return: str - сжатая алгоритмом RLE строка.
    """
    result = ''
    count = 1

    for i in range(len(initial_string) - 1):
        if initial_string[i] == initial_string[i+1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += initial_string[i]
            count = 1

    if count > 1:
        result += str(count)
    result += initial_string[-1]

    return result
