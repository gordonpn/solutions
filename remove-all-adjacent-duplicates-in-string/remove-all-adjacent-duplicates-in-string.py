class Solution:
    def removeDuplicates(self, S: str) -> str:
        if len(S) <= 1:
            return S
        
        stack = []
        
        for ch in S:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
                
        return "".join(stack)
