class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memoize = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            
            if memoize.get(diff) is None:
                memoize[num] = index
            else:
                return [index, memoize[diff]]
            
