# 100% O(n^2) time complexity
def twoNumberSum(array, targetSum):
    tracking_array = []
    for i in array:
        for j in array:
            if j + i == targetSum and j != i:
                tracking_array.append([i, j])

    for x in tracking_array:
        x.sort()
    result = [list(t) for t in set(tuple(x) for x in tracking_array)]
    return result[0] if len(result) >= 1 else result


# 100% O(n) time complexity
def twoNumberSum(array, targetSum):
    if len(array) == 0 or len(array) == 1:
        return []
    dictionary = {}
    answer = []
    for i in range(len(array)):
        second_number = targetSum - array[i]
        if second_number in dictionary.keys():
            second_index = array.index(second_number)
            if i != second_index:
                return sorted([array[i], array[second_index]])
        dictionary.update({array[i]: i})
    return []
