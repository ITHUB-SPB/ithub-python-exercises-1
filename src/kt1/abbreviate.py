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

    CorrectPhrase = phrase.replace('-', ' ').replace('_', ' ')
    
    result = ""
    for char in CorrectPhrase:
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z') or char == ' ':
            result += char
    

    words = result.split()
    abbreviation = ""
    for word in words:
        if word:
            abbreviation += word[0].upper()
    
    return abbreviation