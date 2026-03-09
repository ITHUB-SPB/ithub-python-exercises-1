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
    result = ""
    i = 0
    while i < len(encoded_string):
        num = ""
        while i < len(encoded_string) and encoded_string[i].isdigit():
            num += encoded_string[i]
            i += 1
        if num:
            result += encoded_string[i] * int(num)
        else:
            result += encoded_string[i]
        i += 1
    return result


def encode(initial_string: str) -> str:
    """Кодирует (сжимает) строку.

    :param initial_string: str - исходная строка, содержит символы [a-zA-Z ].
    :return: str - сжатая алгоритмом RLE строка.
    """
    if not initial_string:
        return ""
    
    result = ""
    count = 1
    for i in range(1, len(initial_string)):
        if initial_string[i] == initial_string[i - 1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += initial_string[i - 1]
            count = 1
    if count > 1:
        result += str(count)
    result += initial_string[-1]
    return result
