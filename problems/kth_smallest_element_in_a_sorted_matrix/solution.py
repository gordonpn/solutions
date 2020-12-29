class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sorted_list = []
        n = len(matrix)
        
        while len(sorted_list) < k:
            smallest = math.inf
            list_index = None
            for i in range(n):
                if matrix[i]:
                    if matrix[i][0] < smallest:
                        smallest = matrix[i][0]
                        list_index = i
                        
            if list_index is not None:
                sorted_list.append(matrix[list_index].pop(0))
                
        return sorted_list[-1]