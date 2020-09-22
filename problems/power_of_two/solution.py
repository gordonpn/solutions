class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = 0
        counter = 0
        while result <= n:
            result = pow(2, counter)
            if result == n:
                return True
            counter += 1
        return False
        