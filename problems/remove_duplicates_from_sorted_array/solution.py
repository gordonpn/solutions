class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        index = 0
        while True:
            if index >= len(nums) - 1:
                break
            if (nums[index] == nums[index + 1]):
                nums.pop(index)
            else:
                index += 1 
        return len(nums)