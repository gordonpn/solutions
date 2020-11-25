from typing import Dict, List, Tuple


def two_sums(nums: List[int], target: int):
    pairs: List[Tuple[int, int]] = []
    memoize: Dict[int, int] = {}

    for index, num in enumerate(nums):
        if target - num in memoize:
            pairs.append((num, nums[memoize.get(target - num)]))
        else:
            memoize[num] = index
    return len(set(pairs))


print(two_sums([1, 1, 2, 45, 46, 46], 47))  # 2
print(two_sums([1, 1], 2))  # 1
print(two_sums([1, 5, 1, 5], 6))  # 1
