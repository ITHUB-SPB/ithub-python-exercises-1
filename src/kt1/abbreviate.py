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
    clean = phrase.replace('-', ' ')
    clean = ''.join(c for c in clean if c.isalpha() or c == ' ')
    
    return ''.join(word[0] for word in clean.split() if word).upper()
