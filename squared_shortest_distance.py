from typing import List


def squared_shortest_distance(
    num_robots: int, position_x: List[int], position_y: List[int]
):
    coordinates = list(zip(position_x, position_y))
    coordinates = list(set(coordinates))
    distances = {}
    print(f"{coordinates=}")

    for robot_one in range(len(coordinates)):
        for robot_two in range(len(coordinates)):
            if robot_one == robot_two:
                continue
            if str(robot_two) + str(robot_one) in distances:
                continue

            distance = (coordinates[robot_two][0] - coordinates[robot_one][0]) ** 2 + (
                coordinates[robot_two][1] - coordinates[robot_one][1]
            ) ** 2

            distances[str(robot_one) + str(robot_two)] = distance

    print(f"{distances=}")
    distances_list = list(distances.items())
    distances_list.sort(key=lambda x: x[1])
    return distances_list[0][1]


print(squared_shortest_distance(3, [0, 1, 2], [0, 1, 4]))  # 2
print(squared_shortest_distance(3, [0, 2, 0], [0, 3, 0]))  # 13
