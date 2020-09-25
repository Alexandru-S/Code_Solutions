# 57% soluton time complexity O(n)
def solution(N):
    factor_list = []
    for x in range(1, N + 1):
        if N % x == 0:
            factor_list.append(x)
    result = len(factor_list) if len(factor_list) > 0 else 0
    return result
