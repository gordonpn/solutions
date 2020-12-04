def fibonacci_recursive(n: int):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


term = 9
print(fibonacci_recursive(term))

for i in range(1, term + 1):
    print(fibonacci_recursive(i))
