class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_longest = 0
        start = 0
        end = 0
        seen = set()
        str_len = len(s)

        if str_len == 0:
            return 0
        if str_len == 1:
            return 1

        while start < str_len and end < str_len:
            if s[end] not in seen:
                seen.add(s[end])
                end += 1
                len_longest = max(len_longest, end - start)
            else:
                seen.remove(s[start])
                start += 1

        return len_longest                