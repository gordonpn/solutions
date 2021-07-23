class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        
        result = 0
        rows = len(matrix)
        columns = len(matrix[0])
        
        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        result += 1
                    else:
                        cell = min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1]) + matrix[r][c]
                        result += cell
                        matrix[r][c] = cell
                
        return result