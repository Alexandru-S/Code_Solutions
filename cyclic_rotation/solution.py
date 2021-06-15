# 100% time complexity O(n)
def solution(A, K):
    if len(A) == 0:
        return []
    K = K % len(A) if K > len(A) else K
    return A[-K:] + A[:-K]
