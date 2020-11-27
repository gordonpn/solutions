def finalInstances(instances, averageUtil):
    """
    :type instances: int
    :type averageUtil: List[int]
    :rtype: int
    """
    index = 0
    while index < len(averageUtil):
        if averageUtil[index] < 25:
            if instances != 1:
                instances = -(instances // -2)
                index += 10
        elif averageUtil[index] > 60:
            if instances * 2 <= 2 * 10 ** 8:
                instances = instances * 2
                index += 10
        index += 1

    return instances


instances1 = 2
averageUtil1 = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]

instances2 = 1
averageUtil2 = [5, 10, 80]

instances3 = 5
averageUtil3 = [30, 5, 4, 8, 19, 89]

print(finalInstances(instances1, averageUtil1))  # 2
print(finalInstances(instances2, averageUtil2))  # 2
print(finalInstances(instances3, averageUtil3))  # 3
