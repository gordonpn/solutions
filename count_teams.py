from typing import List


def count_teams(
    num: int, skills: List[int], min_associates: int, min_level: int, max_level: int
):
    skills = [skill for skill in skills if min_level <= skill <= max_level]
    len_skills = len(skills)
    power_sets = []
    for associates in range(min_associates, len_skills):
        for index, num in enumerate(skills):
            power_set = set()
            position = index

            for _ in range(associates):
                position += 1
                power_set.add(skills[len_skills - position])

            power_sets.append(power_set)

    power_sets.append(set(skills))
    print(power_sets)
    return len(power_sets)


num1 = 6
skills1 = [12, 4, 6, 13, 5, 10]
min_associates1 = 3
min_level1 = 4
max_level1 = 10

print(count_teams(num1, skills1, min_associates1, min_level1, max_level1))
