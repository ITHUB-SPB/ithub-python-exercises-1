from typing import TypedDict, List

type Matrix = list[list[int]]


class Coordinate(TypedDict):
    row: int
    column: int


def get_good_coordinates(matrix: Matrix) -> list[Coordinate]:
    """
    Определяет координаты подходящих деревьев.
    Дерево подходит, если оно самое высокое в строке и самое низкое в столбце.
    (Седловая точка матрицы)

    >>> saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])
    [ { "row": 2, "column": 1 } ]

    :param matrix: Matrix - двумерная матрица высот.
    :return: list[Coordinate] - перечень подходящих координат.
    :raises ValueError: если матрица пустая или не прямоугольная
    """
    # Проверка на пустую матрицу
    if not matrix:
        raise ValueError("matrix cannot be empty")
    
    # Проверка на наличие хотя бы одной строки
    if len(matrix) == 0:
        raise ValueError("matrix cannot be empty")
    
    rows = len(matrix)
    
    # Проверяем, что все строки имеют одинаковую длину
    if rows > 0:
        # Проверяем, что первая строка не пустая
        if len(matrix[0]) == 0:
            raise ValueError("matrix rows cannot be empty")
        
        cols = len(matrix[0])
        
        # Проверяем каждую строку
        for i in range(rows):
            if len(matrix[i]) != cols:
                # ВАЖНО: здесь должно быть исключение, а не return []
                raise ValueError("irregular matrix")
    else:
        raise ValueError("matrix cannot be empty")
    
    good_coordinates = []
    
    # Для каждого элемента проверяем условия
    for i in range(rows):
        for j in range(cols):
            current_value = matrix[i][j]
            
            # Проверяем, является ли элемент максимальным в своей строке
            is_max_in_row = True
            for col in range(cols):                                                          #я не знаю
                if matrix[i][col] > current_value:
                    is_max_in_row = False
                    break
            
            # Проверяем, является ли элемент минимальным в своем столбце
            is_min_in_col = True
            for row in range(rows):
                if matrix[row][j] < current_value:
                    is_min_in_col = False
                    break
            
            # Если оба условия выполняются, добавляем координаты
            if is_max_in_row and is_min_in_col:
                good_coordinates.append(Coordinate(row=i + 1, column=j + 1))
    
    return good_coordinates