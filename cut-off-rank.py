from typing import List


def cut_off_rank(cut_off: int, num: int, scores: List[int]):
    scores.sort(reverse=True)
    ranks = [1]
    rank = 1
    for index in range(1, num):
        rank += 1
        if scores[index - 1] == scores[index]:
            ranks.append(ranks[index - 1])
        else:
            ranks.append(rank)

    print(ranks)
    return sum(score <= cut_off for score in ranks)


print(cut_off_rank(3, 4, [100, 50, 50, 25]))  # 3
print(cut_off_rank(4, 5, [2, 2, 3, 4, 5]))  # 5
