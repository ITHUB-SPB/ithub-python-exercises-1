def abbreviate(phrase: str) -> str:
    """Формирует аббревиатуру из исходной фразы.

    Обрабатывает пунктуацию следующим образом:
    дефисы считает разделителями слов, наравне
    с пробелами, иную пунктуацию игнорирует.

    >>> abbreviate("Portable Network Graphics")
    PNG

    >>> abbreviate("As Soon As Possible")
    ASAP

    >>> abbreviate("Liquid-crystal display")
    LCD

    >>> abbreviate("Hello World!")
    HW

    :param phrase: str - исходная фраза.
    :return: str - аббревиатура.
    """
    formated_phrase = phrase.replace('-', ' ')
    final_phrase = ''.join(char if char.isalpha() or char == ' ' else '' for char in formated_phrase)
    return ''.join(word[0].upper() for word in final_phrase.split())
    
