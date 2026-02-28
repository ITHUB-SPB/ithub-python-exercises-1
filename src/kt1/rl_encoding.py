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


def decode(encoded_string: str) -> str:
    """Декодирует (восстанавливает) строку.

    :param encoded_string: str - строка, сжатая алгоритмом RLE.
    :return: str - восстановленная строка.
    """

    return encoded_string


def encode(initial_string: str) -> str:
    """Кодирует (сжимает) строку.

    :param initial_string: str - исходная строка, содержит символы [a-zA-Z ].
    :return: str - сжатая алгоритмом RLE строка.
    """

    return initial_string
