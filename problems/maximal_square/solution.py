class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        max_rows, max_cols = len(matrix), len(matrix[0])
        
        def helper(row, col):
            if row >= max_rows or col >= max_cols:
                return 0
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            right = helper(row, col + 1)
            down = helper(row + 1, col)
            diag = helper(row + 1, col + 1)
            
            dp[(row, col)] = 0
            if matrix[row][col] == "1":
                dp[(row, col)] = 1 + min(right, down, diag)
        
        for row in reversed(range(max_rows)):
            for col in reversed(range(max_cols)):
                helper(row, col)
                
        return max(dp.values()) ** 2