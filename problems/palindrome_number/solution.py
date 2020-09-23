class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        end = -1
        for start in range(len(x_str)//2):
            if x_str[start] != x_str[end]:
                return False
            end -= 1
        return True