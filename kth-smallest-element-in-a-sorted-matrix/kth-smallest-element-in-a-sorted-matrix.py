class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        merged_list = []
        
        for n in range(len(matrix)):
            merged_list.extend(matrix[n])
            
        sorted_list = sorted(merged_list)
        
        return sorted_list[k - 1]
