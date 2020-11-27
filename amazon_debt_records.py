from typing import List


class debtRecord:
    borrower = ""
    lender = ""
    amount = 0

    def __init__(self, borrower, lender, amount):
        self.borrower = borrower
        self.lender = lender
        self.amount = amount


def minimumDebtMembers(records: List[debtRecord]) -> List[str]:
    debt = {record.borrower: 0 for record in records}
    for record in records:
        if record.lender not in debt:
            debt[record.lender] = 0
        debt[record.borrower] -= record.amount
        debt[record.lender] += record.amount
    debt = {name: amount for name, amount in debt.items() if amount < 0}
    if not debt:
        return ["Nobody has a negative balance"]

    debt_list = list(debt.items())
    min_value = min(debt_list, key=lambda x: x[1])[1]
    values = [amount for name, amount in debt_list]
    num_min = values.count(min_value)
    debt_list.sort(key=lambda x: x[1])

    result = [debt_list[i][0] for i in range(num_min)]
    return sorted(result)


records1 = [
    debtRecord("Alex", "Blake", 2),
    debtRecord("Blake", "Alex", 2),
    debtRecord("Casey", "Alex", 5),
    debtRecord("Blake", "Casey", 7),
    debtRecord("Alex", "Blake", 4),
    debtRecord("Alex", "Casey", 4),
]  # ['Alex', 'Blake']

records2 = [
    debtRecord("Jeff", "Ivy", 3),
    debtRecord("Jeff", "Greg", 6),
    debtRecord("Ivy", "Casey", 5),
    debtRecord("Ellen", "Casey", 4),
    debtRecord("Alex", "Jeff", 8),
    debtRecord("Ivy", "Ellen", 8),
    debtRecord("Ivy", "Casey", 4),
    debtRecord("Ivy", "Alex", 2),
    debtRecord("Frank", "Ivy", 8),
    debtRecord("Casey", "David", 4),
]  # ['Frank', 'Ivy']

print(minimumDebtMembers(records2))
