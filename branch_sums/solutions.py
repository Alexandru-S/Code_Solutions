# 100% , time complexity O(n)
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calcBranchSums(root, 0, sums)
    return sums


def calcBranchSums(node, runningSum, sums):
    if node is None:
        return
    nuw_running_sum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(nuw_running_sum)
        return
    calcBranchSums(node.left, nuw_running_sum, sums)
    calcBranchSums(node.right, nuw_running_sum, sums)
