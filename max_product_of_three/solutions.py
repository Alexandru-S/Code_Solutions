# 100% time complexity O(n)
def solution(A):
    A.sort()
    n = len(A)
    return max(A[0] * A[1] * A[n - 1],  A[n - 1] * A[n - 2] * A[n - 3])