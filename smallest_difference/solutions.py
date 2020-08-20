def smallestDifference(arrayOne, arrayTwo):
	tracking_array = []
	arrayOne.sort()
	arrayTwo.sort()
	idx = 0
	idy = 0
	smallest = float('inf')
	current = float('inf')
	smallest_pair = []
	
	while idx < len(arrayOne) and idy < len(arrayTwo):
		firstNum = arrayOne[idx]
		secondNum = arrayTwo[idy]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idx += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idy += 1
		else:
			return [firstNum, secondNum]
	
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
			
	return smallestPair
