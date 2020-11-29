from typing import List


def dropped_requests(request_time: List[int]):
    dropped = 0

    for i in range(3, len(request_time)):
        if request_time[i - 3] == request_time[i]:
            dropped += 1
        elif i > 19 and request_time[i] - request_time[i - 20] < 10:
            dropped += 1
        elif i > 59 and request_time[i] - request_time[i - 60] < 60:
            dropped += 1

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
