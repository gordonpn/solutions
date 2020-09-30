class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s_list = s.split(" ")
        while len(s_list[-1]) < 1:
            s_list.pop(-1)
            if len(s_list) < 1:
                return 0
        return len(s_list[-1])
        