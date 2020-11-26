class Solution:
    def climbStairs(self, n: int) -> int:
        memoize = {}
        memoize[0] = 0
        memoize[1] = 1
        memoize[2] = 2

        if n in memoize:
            return memoize[n]

        for steps in range(3, n + 1):
            memoize[steps] = memoize[steps - 1] + memoize[steps - 2]

        return memoize[n]
