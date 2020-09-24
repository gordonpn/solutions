class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for index in range(len(s)):
            if s[index] in ('(', '[', '{'):
                stack.append(s[index])
            if s[index] in (')', ']', '}'):
                if len(stack) < 1:
                    return False
                if s[index] == ')' and stack[-1] == '(':
                    stack.pop()
                elif s[index] == ']' and stack[-1] == '[':
                    stack.pop()
                elif s[index] == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
                    
                
               
                