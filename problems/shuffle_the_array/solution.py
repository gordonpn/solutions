class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_nums = []
        first_half = nums[:len(nums)//2]
        second_half = nums[len(nums)//2:]
        
        while len(first_half) > 0:
            shuffled_nums.append(first_half.pop(0))
            shuffled_nums.append(second_half.pop(0))
            
        return shuffled_nums
            