class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_rows, max_cols = len(matrix), len(matrix[0])
        
        for row in reversed(range(max_rows)):
            if matrix[row][0] == target:
                return True
            if matrix[row][0] < target:
                for col in range(max_cols):
                    if matrix[row][col] == target:
                        return True
                    if matrix[row][col] > target:
                        for inner_row in reversed(range(row)):
                            if matrix[inner_row][col] == target:
                                return True
            
        return False
            