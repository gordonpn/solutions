from typing import List


def cut_off_rank(cut_off: int, num: int, scores: List[int]):
    scores.sort(reverse=True)
    ranks = [1]
    for rank, index in enumerate(range(1, num), start=2):
        if scores[index - 1] == scores[index]:
            ranks.append(ranks[index - 1])
        else:
            ranks.append(rank)

    print(f"scores: {scores}")
    print(f"ranks: {ranks}")
    print(f"cut_off: {cut_off}")
    return sum(score <= cut_off for score in ranks)


print(cut_off_rank(3, 4, [100, 50, 50, 25]))  # 3
print(cut_off_rank(4, 5, [2, 2, 3, 4, 5]))  # 5
