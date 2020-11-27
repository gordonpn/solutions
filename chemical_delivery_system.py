from typing import List


def chemical_delivery_system(
    num_orders: int,
    requirements: List[int],
    flask_types: int,
    total_marks: int,
    markings: List[List[int]],
):
    waste_per_flask = {index: 0 for index in range(flask_types)}

    for requirement in requirements:
        for flask in range(flask_types):
            skips = 0
            for flask_index, marking in markings:
                if flask_index != flask:
                    continue
                if requirement > marking:
                    skips += 1
                    if skips == flask_types:
                        del waste_per_flask[flask_index]
                elif requirement <= marking:
                    if flask_index in waste_per_flask:
                        waste = marking - requirement
                        waste_per_flask[flask_index] += waste
                    break

    if len(waste_per_flask) == 0:
        return -1
    return min(waste_per_flask, key=waste_per_flask.get)


print(
    chemical_delivery_system(
        4,
        [4, 6, 6, 7],
        3,
        9,
        [[0, 3], [0, 5], [0, 7], [1, 6], [1, 8], [1, 9], [2, 3], [2, 5], [2, 6]],
    )
)  # 0
