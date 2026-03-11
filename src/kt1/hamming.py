"""
Расстояние Хэмминга применяется в разных областях науки и инженерии, и крайне просто в расчете:
подсчитывается количество отличий между несколькими последовательностями равной длины.

Рассмотрим пример с двумя цепями ДНК, которые кодируются символами C, A, G и T.

    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^

Здесь подсвечены участки цепей, где присутствуют отличия (символы не совпадают).
Просуммировав их, получим 7 - это и есть расстояние Хэмминга.
"""


def distance(string_1: str, string_2: str) -> int:
    """Вычисляет расстояние Хэмминга для двух строк.

    >>> distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
    7

    >>> distance("GAGCCTACTAACGGGAT", "CATCG")
    ValueError("Strings must be of equal length.")

    :param string_1: str - первая строка.
    :param string_2: str - вторая строка.
    :return: int - расстояние Хэмминга между строками.
    :throws: ValueError - при несовпадении длин последовательностей.
    """
    
    if len(string_1) != len(string_2):
        raise ValueError("Strings must be of equal length.")
    
    count = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            count += 1
    
    return count
