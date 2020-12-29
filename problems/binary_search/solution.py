class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        
        if target < nums[lo] or target > nums[hi]:
            return -1
        
        middle = len(nums) // 2
        
        while True:
            if target == nums[middle]:
                return middle
            if target == nums[lo]:
                return lo
            if target == nums[hi]:
                return hi
            if middle + 1 == hi and middle - 1 == lo:
                return -1
            if target < nums[middle]:
                hi = middle
                middle = lo + (hi - lo) // 2
                continue
            if target > nums[middle]:
                lo = middle
                middle = lo + (hi - lo) // 2
                continue
