class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x < 0
        x = abs(x)
        if x >= pow(2, 31):
            return 0
        num_str = str(x)
        stack = []
        reversed_string = ""
        for c in num_str:
            stack.append(c)
        while stack:
            reversed_string += stack.pop()
        final_int = int(reversed_string)
        if final_int > pow(2, 31):
            return 0
        if is_negative:
            final_int = final_int * -1
        return final_int
        