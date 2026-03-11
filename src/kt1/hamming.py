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
    
    distance_count = 0
    for i in range(len(string_1)):          #колво символов
        if string_1[i] != string_2[i]:
            distance_count += 1
    
    return distance_count