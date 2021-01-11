from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        index = 0

        while index < len(nums) - 1:
            if nums[index] == nums[index + 1]:
                nums.pop(index)
            else:
                index += 1

        return len(nums)
