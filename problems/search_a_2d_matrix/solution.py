class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_rows, max_cols = len(matrix), len(matrix[0])
        
        if target < matrix[0][0] or target > matrix[max_rows - 1][max_cols - 1]:
            return False
        
        nums = []
        
        for row in range(max_rows):
            nums.extend(matrix[row])
        
        start, end = 0, len(nums) - 1

        while start <= end:
            middle = start + (end - start) // 2

            if nums[start] == target or nums[end] == target or nums[middle] == target: 
                return True
            if target < nums[middle]:
                end = middle - 1
            elif target > nums[middle]:
                start = middle + 1

        return False
        