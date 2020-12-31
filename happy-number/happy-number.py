class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def get_new_sum(n):
            nums = list(str(n))
            new_sum = 0
            for num in nums:
                new_sum += int(num) ** 2
            return new_sum
            
        while n != 1:
            seen.add(n)
            
            n = get_new_sum(n)
            
            if n in seen:
                return False
                
        return True
