from itertools import combinations

def getListofCombinations(arr, n):
	return list(combinations(arr, n))

def isValidSubsequence(array, sequence):
	subsequences = getListofCombinations(array, len(sequence))
	found = False
	for x in subsequences:
		if list(x) == sequence:
			found = True
	return found
