from typing import TypedDict

type Matrix = list[list[int]]


class Coordinate(TypedDict):
    row: int
    column: int


def get_good_coordinates(matrix: Matrix) -> list[Coordinate]:   
    if not matrix:
        return []
    
    first_row_len = len(matrix[0])
    if first_row_len == 0:
        return []
    
    for row in matrix:
        if len(row) != first_row_len:
            raise ValueError("irregular matrix")
    
    rows = len(matrix)
    cols = first_row_len
    
    row_max_values = []
    for i in range(rows):
        row_max_values.append(max(matrix[i]))
    
    col_min_values = []
    for j in range(cols):
        col_values = [matrix[i][j] for i in range(rows)]
        col_min_values.append(min(col_values))
    
    result = []
    for i in range(rows):
        for j in range(cols):
            if (matrix[i][j] == row_max_values[i] and 
                matrix[i][j] == col_min_values[j]):
                result.append(Coordinate(row=i+1, column=j+1))
    
    result.sort(key=lambda coord: (coord["row"], coord["column"]))
    
    return result