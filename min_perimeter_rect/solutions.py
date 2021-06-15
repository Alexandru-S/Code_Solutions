from functools import reduce


def get_perimeter(A, B):
    return 2 * (A + B)


def solution(N):
    factor_list = list(factors(N))
    pointer = int(len(factor_list) / 2)
    result = get_perimeter(factor_list[pointer - 1], factor_list[-pointer])
    return result


def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
        )
    )
