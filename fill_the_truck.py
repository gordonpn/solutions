from typing import List


def fillTheTruck(
    num: int, boxes: List[int], unitSize: int, unitsPerBox: List[int], truckSize: int
) -> int:
    product_list = []
    units_sum = 0

    for n in range(num):
        units = [unitsPerBox[n]] * boxes[n]
        product_list += units

    product_list.sort(reverse=True)

    for n in range(truckSize):
        if n >= len(product_list):
            break
        units_sum += product_list[n]

    return units_sum


num1 = 3
boxes1 = [1, 2, 3]
unitSize1 = 3
unitsPerBox1 = [3, 2, 1]
truckSize1 = 3

num2 = 5
boxes2 = [1, 3, 2, 2, 1]
unitSize2 = 5
unitsPerBox2 = [9, 8, 9, 5, 8]
truckSize2 = 4

num3 = 5
boxes3 = [2, 2, 3, 1, 1]
unitSize3 = 5
unitsPerBox3 = [2, 3, 5, 1, 5]
truckSize3 = 20

print(fillTheTruck(num1, boxes1, unitSize1, unitsPerBox1, truckSize1))  # 7
print(fillTheTruck(num2, boxes2, unitSize2, unitsPerBox2, truckSize2))  # 35
print(fillTheTruck(num3, boxes3, unitSize3, unitsPerBox3, truckSize3))  # 31
