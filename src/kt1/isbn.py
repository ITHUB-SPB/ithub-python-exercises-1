def is_valid(isbn: str) -> bool:
    """Проверяет строку на соответствие ISBN-10
    по формату и проверочному правилу.

    Например, для кода 3-598-21508-8 мы получим следующее:
    (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 -> 0

    >>> is_valid("3-598-21508-8")
    True

    :param isbn: str - код, с разделяющими дефисами или без них.
    :return: bool - логическое значение корректности.
    """
    isbn = isbn.replace('-', '')
    
    if len(isbn) != 10:
        return False
    
    total = 0
    
    for i in range(9):
        if not isbn[i].isdigit():                    #обрб первые 9 симвл
            return False
        total += int(isbn[i]) * (10 - i)
    
    last_char = isbn[9]
    if last_char == 'X' or last_char == 'x':
        total += 10                                 #обрб ласт симвл
    elif last_char.isdigit():
        total += int(last_char)
    else:
        return False
    
    return total % 11 == 0