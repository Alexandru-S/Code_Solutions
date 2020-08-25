def checkDuplicates(A):
    if len(A) == len(set(A)):
        return False
    else:
        return True


def solution(A):
    A.sort()
    n = len(A) + 1
    if checkDuplicates(A):
        return 0
    else:
        A_check = list(range(1, n))
        if A == A_check:
            return 1
        else:
            return 0