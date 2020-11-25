from typing import List


def lru_cache(num: int, pages: List[int], max_cache_size: int):
    misses = 0
    cache: List[int] = []
    for index in range(num):
        if pages[index] not in cache:
            misses += 1
        if len(cache) >= max_cache_size:
            cache.pop(0)
        cache.append(pages[index])
    return misses


print(lru_cache(6, [1, 2, 1, 3, 1, 2], 2))  # 4
