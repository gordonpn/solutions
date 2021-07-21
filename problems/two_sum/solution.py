class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memoize = {}
        
        for index, num in enumerate(nums):
            
            seen_num_index = memoize.get(target - num)
            
            if seen_num_index is not None:
                return [seen_num_index, index]
                
            memoize[num] = index
