class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        curr_max = 1
        curr_min = 1
        max_product = 0
        minus_inf = -math.inf
        
        for num in nums:
            min_ = curr_min * num
            max_ = curr_max * num
            curr_min = min(min_, max_, num)
            curr_max = max(min_, max_, num)
            max_product = max(minus_inf, curr_max, max_product)
        
        return max_product