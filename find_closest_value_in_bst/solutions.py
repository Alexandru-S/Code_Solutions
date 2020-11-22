def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, tree.value)


def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	if target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	else:
		return closest


class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
