# 100% time complexity O(n)
def solution(A):
    min_avg = (A[0] + A[1]) / 2.0
    min_pos = 0

    for x in range(0, len(A) - 2):
        if (A[x] + A[x + 1]) / 2.0 < min_avg:
            min_avg = (A[x] + A[x + 1]) / 2.0
            min_pos = x
        if (A[x] + A[x + 1] + A[x + 2]) / 3.0 < min_avg:
            min_avg = (A[x] + A[x + 1] + A[x + 2]) / 3.0
            min_pos = x
    if (A[-1] + A[-2]) / 2.0 < min_avg:
        min_avg = (A[-1] + A[-2]) / 2.0
        min_pos = len(A) - 2
    return min_pos
