"""
Вам дана схема (вид сверху), на которой указана высота деревьев.

      ↓
      1  2  3  4
    |-----------
  1 | 9  8  7  8
→ 2 |[5] 3  2  4
  3 | 6  6  7  1

Необходимо определить по схеме деревья, подходящие для постройки дома на дереве.
Такое дерево должно быть самым высоким в строке и при этом самым низким в столбце.

Таких деревьев может не быть вовсе, может быть одно или сразу несколько.
На схеме выше отмечено одно подходящее дерево.
"""

from typing import TypedDict

type Matrix = list[list[int]]


class Coordinate(TypedDict):
    row: int
    column: int


def get_good_coordinates(matrix: Matrix) -> list[Coordinate]:
    """
    Определяет координаты подходящих деревьев.

    >>> saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]])
    [ { "row": 2, "column": 1 } ]

    :param matrix: Matrix - двумерная матрица высот.
    :return: list[Coordinate] - перечень подходящих координат.
    """
    
    if not matrix:
        return []
    
    rows = len(matrix)
    if rows == 0:
        return []
    
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise ValueError("irregular matrix")
    
    row_maximums = []
    for i in range(rows):
        max_val = matrix[i][0]
        for j in range(cols):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
        row_maximums.append(max_val)
    
    col_minimums = []
    for j in range(cols):
        min_val = matrix[0][j]
        for i in range(rows):
            if matrix[i][j] < min_val:
                min_val = matrix[i][j]
        col_minimums.append(min_val)
    
    result = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == row_maximums[i] and matrix[i][j] == col_minimums[j]:
                result.append({"row": i + 1, "column": j + 1})  
    
    return result
