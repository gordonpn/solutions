class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) == 1:
            return S
        
        S = list(S)
        
        i = 1
        while True:
            if len(S) <= 1 or i == len(S):
                return "".join(S)
            if S[i - 1] == S[i]:
                S.pop(i)
                S.pop(i - 1)
                if i > 1:
                    i -= 1
            else:
                i += 1
