def lru_cache(num, pages, max_cache_size):
    misses = 0
    queue = []
    for index in range(num):
        if pages[index] not in queue:
            misses += 1
        if len(queue) >= max_cache_size:
            queue.pop(0)
        queue.append(pages[index])
    return misses


print(lru_cache(6, [1, 2, 1, 3, 1, 2], 2))  # 4
