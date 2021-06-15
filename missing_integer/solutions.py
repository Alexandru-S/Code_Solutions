# 100% time complexity O(n)
def solution(A):
    simple_A = sorted(list(set(A)))
    if max(simple_A) < 0:
        return 1
    else:
        m = set(range(1, len(A)))
        if len(m) == 0:
            if A[0] == 1:
                return 2
            else:
                return 1
        l = set(simple_A)
        result = min(m - l, default=None)
        if result is None:
            return max(l) + 1
        else:
            return result
