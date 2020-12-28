class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        seen_nums = []
        
        for num in nums:
            if num in seen_nums:
                return num
            seen_nums.append(num)