import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original_list = nums
        
        
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original_list
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffled_list = []
        copy_list = [x for x in self.original_list]
        
        while len(copy_list) > 0:
            random_index = random.randint(0, len(copy_list) - 1)
            shuffled_list.append(copy_list[random_index])
            copy_list.pop(random_index)
            
        return shuffled_list 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()