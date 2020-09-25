def solution(A):
    highest = sorted(A, reverse = True)[0]
    lowest = sorted(A)[0]
    local_highest = None
    local_lowest = None
    profit_tracker = []
    for x in range(len(A)):
        if local_lowest is None:
            local_lowest = A[x]
        else:
            if A[x] < local_lowest:
                local_lowest = A[x]
            if A[x] > local_lowest:
                local_highest = x
                profit = A[x]-local_lowest
                profit_tracker.append(profit)
    print(profit_tracker)
    result = sorted(profit_tracker, reverse= True)[0]
    return result