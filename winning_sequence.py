def winning_sequence(num: int, lower_end: int, upper_end: int):
    possibilities = (upper_end - lower_end) * 2 + 1
    if possibilities < num:
        return [-1]
    results = []

    decreasing_half = range(min(num - 1, upper_end - lower_end + 1))
    for digit in decreasing_half:
        results.append(upper_end - digit)
    increasing_half = range(num - len(results))
    for digit in increasing_half:
        results.insert(0, upper_end - 1 - digit)

    return results


print(winning_sequence(5, 3, 10))  # [9,10,9,8,7]
