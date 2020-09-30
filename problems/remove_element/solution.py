class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        index = 0
        while True:
            if index > len(nums) - 1:
                break
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return len(nums)