from typing import List


def dropped_requests(request_time: List[int]):
    dropped = 0
    trans_second = 0
    trans_ten_seconds = 0
    trans_minute = 0

    for transaction in request_time:
        pass

    return dropped


sample1 = [1, 1, 1, 1, 2]
sample2 = [
    1,
    1,
    1,
    1,
    2,
    2,
    2,
    3,
    3,
    3,
    4,
    4,
    4,
    5,
    5,
    5,
    6,
    6,
    6,
    7,
    7,
    7,
    7,
    11,
    11,
    11,
    11,
]

print(dropped_requests(sample1))  # 1
print(dropped_requests(sample2))  # 7
