# 77% correct time complexity O(n)
def solution(A):
    local_lowest = None
    profit_tracker = []
    for x in range(len(A)):
        if local_lowest is None:
            local_lowest = A[x]
        else:
            if A[x] < local_lowest:
                local_lowest = A[x]
            if A[x] > local_lowest:
                profit = A[x] - local_lowest
                profit_tracker.append(profit)
    result = sorted(profit_tracker, reverse=True)[0]
    return result
