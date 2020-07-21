class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for index, value in enumerate(nums):
            search = target - value
            if numsDict.get(search) is not None:
                return [numsDict[search], index]
            numsDict[value] = index
            