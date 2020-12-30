class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]

        for num in nums:
            local_results = []
            for previous_subset in results:
                local_results += [previous_subset + [num]]
            results += local_results

        return results
