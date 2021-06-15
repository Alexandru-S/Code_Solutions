# 100% time complexity O(n)
def solution(X, A):
    steps = set([i for i in range(1, X + 1)])
    frogy_steps = set()
    for index, leaf in enumerate(A):
        frogy_steps.add(leaf)
        if frogy_steps == steps:
            return index
    return -1
