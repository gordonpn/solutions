class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        num = 0
        end = -1
        for i in range(len(s)//2):
            s[i], s[end] = s[end], s[i]
            end -= 1
        