from typing import List


def treasure_island(treasure_map: List[List[str]]) -> int:
    stack = [((0, 0), 0)]
    max_row = len(treasure_map)
    max_col = len(treasure_map[0])
    visited = set()

    while stack:
        position, steps = stack.pop(0)
        i, j = position
        visited.add(position)

        right = treasure_map[i][j + 1] if j < max_col - 1 else None
        left = treasure_map[i][j - 1] if j > 0 else None
        down = treasure_map[i + 1][j] if i < max_row - 1 else None
        up = treasure_map[i - 1][j] if i > 0 else None

        if right == "X" or left == "X" or down == "X" or up == "X":
            return steps + 1

        right_pos = (i, j + 1)
        down_pos = (i + 1, j)
        left_pos = (i, j - 1)
        up_pos = (i - 1, j)
        if right == "O" and right_pos not in visited:
            stack.append((right_pos, steps + 1))
        if down == "O" and down_pos not in visited:
            stack.append((down_pos, steps + 1))
        if left == "O" and left_pos not in visited:
            stack.append((left_pos, steps + 1))
        if up == "O" and up_pos not in visited:
            stack.append((up_pos, steps + 1))

    return -1


map1 = [
    ["O", "O", "O", "O"],
    ["D", "O", "D", "O"],
    ["O", "O", "O", "O"],
    ["X", "D", "D", "O"],
]
map2 = [
    ["O", "O", "O", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "O", "O"],
    ["X", "O", "D", "O"],
]
map3 = [
    ["O", "O", "O", "O"],
    ["D", "O", "D", "O"],
    ["D", "D", "D", "O"],
    ["X", "O", "O", "O"],
]
map4 = [
    ["O", "O", "D", "X"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["O", "O", "O", "O"],
]
map5 = [
    ["O", "O", "D", "X"],
    ["D", "O", "D", "D"],
    ["D", "O", "D", "O"],
    ["O", "O", "O", "O"],
]
map6 = [
    ["O", "O", "D", "X"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["D", "O", "D", "O"],
    ["O", "O", "O", "O"],
]

assert treasure_island(map1) == 5
assert treasure_island(map2) == 5
assert treasure_island(map3) == 9
assert treasure_island(map4) == 9
assert treasure_island(map5) == -1
assert treasure_island(map6) == 31
