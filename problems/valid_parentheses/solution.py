class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == ")":
                if not stack:
                    return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
                
            elif c == "]":
                if not stack:
                    return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
                
            elif c == "}":
                if not stack:
                    return False
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
            
        if stack:
            return False
        return True