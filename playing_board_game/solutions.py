from functools import reduce


def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
        )
    )


T = int(input())
dice = set([3, 5, 10])

numbers = [int(input()) for _ in range(T)]

for x in numbers:
    count = 0
    result = factors(x)
    new_result = result.intersection(dice)
    print("newresult", new_result)
    count = len(new_result)
    print(count)
