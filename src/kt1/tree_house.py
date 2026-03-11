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

    >>> get_good_coordinates([[9, 8, 7], [5, 3, 2], [6, 6, 7]])
    [{'row': 2, 'column': 1}]

    :param matrix: Matrix - двумерная матрица высот.
    :return: list[Coordinate] - перечень подходящих координат.
    """
    result = []

    for i in range (len(matrix)):
        max_row = max(matrix[i])

        for j in range (len(matrix[i])):
            column = []

            for k in range (len(matrix)):
                column.append(matrix[k][j])

            column_min = min(column)

            if matrix[i][j] == max_row and matrix[i][j] == column_min:
                result.append(Coordinate(row=i +1, column=j +1))

    return result
