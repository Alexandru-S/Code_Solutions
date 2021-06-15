# 100% time complexity O(n)
def solution(A):
    if len(A) < 3:
        return 0
    else:
        A.sort()
        for x in range(len(A) - 2):
            if A[x] + A[x + 1] > A[x + 2]:
                return 1
        return 0
