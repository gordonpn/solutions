# Given a string "wal" find if it is a subsequence of a larger string such as "todaywalaetsmaasdfwrtabcd".

# Example:
# isSubSeq("walmart", "todaywalaetsmaasdfwrtabcd");//true

# Note: A subsequence of a string is a new string which is formed from the original string by deleting some
# (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).


def isSubSeq(string: str, long_str: str):
    if not str:
        return True
    found: bool = False
    index: int = 0
    for c in long_str:
        if index != 0 and (index + 1) == len(string):
            return True
        if c == string[index]:
            index += 1

    return found


print(isSubSeq("walmart", "todaywalaetsmaasdfwrtabcd"))
