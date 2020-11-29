from typing import List


def earliest_delivery(
    num_of_buildings: int, building_open_time: List[int], off_load_time: List[int]
):
    building_open_time = sorted(building_open_time)
    off_load_time = sorted(off_load_time)
    slowest = 0

    for index in range(num_of_buildings):
        dock_index = num_of_buildings * 4 - index * 4 - 1

        slowest = max(slowest, building_open_time[index] + off_load_time[dock_index])

    return slowest


num_of_buildings1 = 2
building_open_time1 = [8, 10]
off_load_time1 = [2, 2, 3, 1, 8, 7, 4, 5]

print(earliest_delivery(num_of_buildings1, building_open_time1, off_load_time1))  # 16
