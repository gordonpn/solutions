class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        if len(s) < 1:
            return -1

        seen = set()

        for i in range(len(s)):
            if s[i] not in s[i + 1 :] and s[i] not in seen:
                return i
            seen.add(s[i])

        return -1

