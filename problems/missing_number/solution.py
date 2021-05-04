class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        
        for num in range(len(nums) + 1):
            if num not in numsSet:
                return num