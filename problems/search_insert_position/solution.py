class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index in range(len(nums)):
            if nums[index] >= target:
                return index
            elif nums[index] < target and index == len(nums) - 1:
                return index + 1