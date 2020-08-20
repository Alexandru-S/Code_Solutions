from itertools import combinations


def getCombinations(arr, n):
	return list(combinations(arr, n))


def setLowToHigh(target_result):
	max_value = len(target_result) - 1
	count = 0
	for x in range(len(target_result)):
		if x != max_value:
			if target_result[x][0] == target_result[x + 1][0]:
				if target_result[x][1] > target_result[x + 1][1]:
					target_result[x], target_result[x + 1] = target_result[x + 1], target_result[x]
					count += 1

			if target_result[x][0] > target_result[x + 1][0]:
				target_result[x], target_result[x + 1] = target_result[x + 1], target_result[x]
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


#####################SECOND SOLUTION##############################################

def threeNumberSum2(array, targetSum):
	array.sort()
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			currentsum = array[i] + array[left] + array[right]
			if currentsum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currentsum < targetSum:
				left += 1
			elif currentsum > targetSum:
				right -= 1
	return triplets

