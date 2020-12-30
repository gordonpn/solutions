class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        if not nums:
            return result

        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1

        result = list(result.items())
        result = sorted(result, key=lambda x: x[1], reverse=True)

        return [result[n][0] for n in range(k)]
