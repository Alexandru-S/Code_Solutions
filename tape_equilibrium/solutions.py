A = [3, 1, 2, 4, 3]


def solution(A):
    s = sum(A)
    m = float("inf")
    left_sum = 0
    for x in A[:-1]:
        left_sum += x
        m = min(abs(s - 2 * left_sum), m)

    return m
