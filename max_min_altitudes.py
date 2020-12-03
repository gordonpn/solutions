from typing import List


def max_min_altitudes(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    if rows == 0:
        return 0

    columns = len(matrix[0])
    if columns == 0:
        return 0

    for i in range(2, rows):
        matrix[i][0] = min(matrix[i][0], matrix[i - 1][0])

    for j in range(2, columns):
        matrix[0][j] = min(matrix[0][j], matrix[0][j - 1])

    for i in range(1, rows):
        for j in range(1, columns):
            matrix[i][j] = max(
                min(matrix[i][j], matrix[i][j - 1]), min(matrix[i][j], matrix[i - 1][j])
            )

    matrix[rows - 1][columns - 1] = max(
        matrix[rows - 1][columns - 2], matrix[rows - 2][columns - 1]
    )

    print(matrix)

    return matrix[rows - 1][columns - 1]


matrix1 = [[5, 1], [4, 5]]
matrix2 = [[1, 2, 3], [4, 5, 1]]
matrix3 = [[6, 7, 8], [5, 4, 2], [8, 7, 6]]
matrix4 = [[7, 5, 3], [2, 0, 9], [4, 5, 9]]
matrix5 = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

print(max_min_altitudes(matrix1))  # 4
print(max_min_altitudes(matrix2))  # 4
print(max_min_altitudes(matrix3))  # 5
print(max_min_altitudes(matrix4))  # 3
print(max_min_altitudes(matrix5))  # 1
