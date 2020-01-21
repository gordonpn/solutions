class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        index: int = 0
        for c in t:
            if index != 0 and (index + 1) == len(s):
                return True
            if c == s[index]:
                index += 1
                
        return False