# 100% time complexity O(n)
def solution(A):
    max_sum = A[0]
    acc = 0
    for e in A:
        acc += e
        if acc > max_sum:
            max_sum = acc
        if acc < 0:
            acc = 0
    return max_sum
