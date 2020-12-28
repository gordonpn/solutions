class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        original_len = len(nums)
        nums = set(nums)
        results = []
        
        for n in range(1, original_len + 1):
            if n not in nums:
                results.append(n)
                
        return results
                
