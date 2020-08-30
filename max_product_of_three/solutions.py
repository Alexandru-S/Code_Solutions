def solution(A):
    A.sort()
    return A[-3] * A[-2] * A[-1]