class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        current_start = 0
        current_sum = nums[current_start]
        current_max = nums[current_start]
        
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            current_max = max(current_max, current_sum)

        return current_max