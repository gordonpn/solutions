class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in complements:
                return [complements.get(diff), index]
            else:
                complements[num] = index
        