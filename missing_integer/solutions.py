# 88% O(n)
def solution(A):
    simple_A = sorted(list(set(A)))
    if max(simple_A) < 0:
        return 1
    else:
        m = set(range(1,len(A)))
        l = set(simple_A)
        result = min(m - l, default=None)
        if result  is None:
            return max(l) + 1
        else:
            return result
