from typing import List


def multiprocessor_system(num: int, ability: List[int], processes: int):
    seconds = 0
    while processes > 0:
        seconds += 1
        this_ability = max(ability)
        position = ability.index(max(ability))
        processes -= this_ability
        ability[position] = this_ability // 2

    return seconds


print(multiprocessor_system(5, [3, 1, 7, 2, 4], 15))  # 4
