from itertools import combinations


def getCombinations(arr, n):
    return list(combinations(arr, n))


def setLowToHigh(target_result):
    max_var = len(target_result) - 1
    count = 0
    for x, value in enumerate(target_result):
        if x != max_var:
            if value[0] == target_result[x + 1][0]:
                if value[1] > target_result[x + 1][1]:
                    value, target_result[x + 1] = target_result[x + 1], value
                    count += 1
            if value[0] > target_result[x + 1][0]:
                value, target_result[x + 1] = target_result[x + 1], value
                count += 1
    if count == 0:
        return True
    else:
        return False


def threeNumberSum(array, targetSum):
    comb_result = getCombinations(array, 3)
    target_result = []
    for x in comb_result:
        lst = sorted(list(x))
        if sum(lst) == targetSum:
            target_result.append(lst)
    fixed_array = False
    while fixed_array == False:
        fixed_array = setLowToHigh(target_result)
    return target_result
