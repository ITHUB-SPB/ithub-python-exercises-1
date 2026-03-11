def decode(encoded_string: str) -> str:
    """Декодирует (восстанавливает) строку.

    :param encoded_string: str - строка, сжатая алгоритмом RLE.
    :return: str - восстановленная строка.
    """
    if not encoded_string:
        return ""
    
    decoded = ""
    i = 0
    
    while i < len(encoded_string):
        count_str = ""
        while i < len(encoded_string) and encoded_string[i].isdigit():              #собр число
            count_str += encoded_string[i]
            i += 1
        
        if count_str:
            count = int(count_str)
            if i < len(encoded_string):
                decoded += encoded_string[i] * count
                i += 1
        else:                                               #если нет симвл то одиноч
            decoded += encoded_string[i]
            i += 1
    
    return decoded


def encode(initial_string: str) -> str:
    """Кодирует (сжимает) строку.

    :param initial_string: str - исходная строка, содержит символы [a-zA-Z ].
    :return: str - сжатая алгоритмом RLE строка.
    """
    if not initial_string:
        return ""
    
    encoded = ""
    count = 1
    current_char = initial_string[0]
    
    for i in range(1, len(initial_string)):
        if initial_string[i] == current_char:
            count += 1
        else:
            if count > 1:
                encoded += str(count)
            encoded += current_char
            current_char = initial_string[i]
            count = 1
    
    if count > 1:
        encoded += str(count)                #добав в группу
    encoded += current_char
    
    return encoded