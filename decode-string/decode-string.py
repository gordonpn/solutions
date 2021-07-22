class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []
        k = 0
        
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                stack.append((result, k))
                result = ""
                k = 0
            elif c == "]":
                last_result, last_k = stack.pop()
                result = last_result + last_k * result
            else:
                result += c
                
        return result 
            