class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        
        for num in nums:
            results += [i + [num] for i in results]
            
        return results