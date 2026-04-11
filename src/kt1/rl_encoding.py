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
    decoded = []
    counter = 0
    for char in encoded_string:
        if char.isdigit():
            counter += int(char)
        else:
            if counter != 0:
                decoded.append(char * counter)
                counter = 0
            else:
                decoded.append(char)
    return "".join(decoded)


def encode(initial_string: str) -> str:
    """Кодирует (сжимает) строку.

    :param initial_string: str - исходная строка, содержит символы [a-zA-Z ].
    :return: str - сжатая алгоритмом RLE строка.
    """

    if len(initial_string) == 0:
        return ""
    encoded = []
    counter = 1
    
    for i in range(1, len(initial_string)):
        if initial_string[i] == initial_string[i-1]:
            counter += 1
        else:
            encoded.append(f"{counter}{initial_string[i-1]}" if counter > 1 else initial_string[i-1])
            counter = 1
    
    encoded.append(f"{counter}{initial_string[-1]}" if counter > 1 else initial_string[-1])
    return ''.join(encoded)
