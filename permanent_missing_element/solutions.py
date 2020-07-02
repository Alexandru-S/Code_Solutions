def solution(A):
    if len(A) == 0:
        return 1
    A.sort()
    if A[0] != 1:
        return 1
    if len(A) == 1 and A[0] == 1:
        return 2
    for i in A:
        if A[i]+1 != A[i+1]:
            return A[i]+1
    return A[-1] +1