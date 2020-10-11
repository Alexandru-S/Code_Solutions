# 100% time complexity O(n)
def solution(A):
    A.sort()
    for i in reversed(range(len(A))):
        if len(A) == 1:
            break
        if i == len(A):
            continue
        if A[i] == A[i-1]:
            A.pop(i)
            A.pop(i-1)
            i = i -2
    return A[0]
