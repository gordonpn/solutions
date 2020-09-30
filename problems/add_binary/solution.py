class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_diff = len(a) - len(b)
        if len_diff < 0:
            a = "0" * abs(len_diff) + a
        elif len_diff > 0:
            b = "0" * abs(len_diff) + b
       
        carry = 0
        result = ""
        a = a[::-1]
        b = b[::-1]
        for index in range(len(a)):
            sum = carry + int(a[index]) + int(b[index])
            carry = 0
            
            if sum == 3:
                carry = 1
                result = "1" + result
            elif sum == 2:
                carry = 1
                result = "0" + result
            else:
                result = str(sum) + result
                
            if index >= len(a) - 1 and carry > 0:
                result = "1" + result
                
        return result