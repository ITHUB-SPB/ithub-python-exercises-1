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
    
    if len(matrix) > 0:
        first_row_len = len(matrix[0])
        for row in matrix:
            if len(row) != first_row_len:
                raise ValueError("irregular matrix")
    
    result = []
    
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            is_max_in_row = all(value >= cell for cell in row)
            is_min_in_col = all(value <= matrix[r][col_idx] for r in range(len(matrix)))
            
            if is_max_in_row and is_min_in_col:
                result.append(Coordinate(row=row_idx + 1, column=col_idx + 1))
    
    return result
