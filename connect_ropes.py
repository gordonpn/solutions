from typing import List


def connectRopes(ropes: List[int]):
    total_cost = 0
    while len(ropes) > 1:
        min_first = ropes.pop(ropes.index(min(ropes)))
        min_second = ropes.pop(ropes.index(min(ropes)))

        cost = min_first + min_second
        total_cost += cost

        ropes.append(cost)

    return total_cost


ropes1 = [8, 4, 6, 12]
ropes2 = [20, 4, 8, 2]
ropes3 = [1, 2, 5, 10, 35, 89]
ropes4 = [2, 2, 3, 3]

print(connectRopes(ropes1))  # 58
print(connectRopes(ropes2))  # 54
print(connectRopes(ropes3))  # 224
print(connectRopes(ropes4))  # 20
