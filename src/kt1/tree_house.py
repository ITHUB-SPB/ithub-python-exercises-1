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
    if not matrix or not matrix[0]:
        return []
    
    result = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for r in range(rows):
        row_max = max(matrix[r])
        
        for c in range(cols):
            height = matrix[r][c]
            if height != row_max:
                continue
            
            col_min = min(matrix[i][c] for i in range(rows))
            if height == col_min:
                result.append({"row": r + 1, "column": c + 1})
    
    return result