def abbreviate(phrase: str) -> str:
    """Формирует аббревиатуру из исходной фразы.

    Обрабатывает пунктуацию следующим образом:
    дефисы считает разделителями слов, наравне
    с пробелами, иную пунктуацию игнорирует.

    >>> abbreviate("Portable Network Graphics")
    'PNG'

    >>> abbreviate("As Soon As Possible")
    'ASAP'

    >>> abbreviate("Liquid-crystal display")
    'LCD'

    >>> abbreviate("Hello World!")
    'HW'

    :param phrase: str - исходная фраза.
    :return: str - аббревиатура.
    """
    result = ''
    words = phrase.replace("-"," ").split()

    for word in words:
        result += word[0].upper()

    return result

print(abbreviate("Portable Network Graphics"))