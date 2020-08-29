

def twoNumberSum(array, targetSum):
    tracking_array = []
    for i in array:
        for j in array:
            if j+i == targetSum and j != i:
                tracking_array.append([i, j])

    for x in tracking_array:
        x.sort()
    result = [ list(t) for t in set(tuple(x) for x in tracking_array)]
    return result[0] if len(result) >=1 else result
