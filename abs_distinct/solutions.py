# 100% time complexity O(n)
def solution(A):
    newlist = [abs(n) for n in A]
    return len(list(set(newlist)))
