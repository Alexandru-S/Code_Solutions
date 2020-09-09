# 100% time complexity O(n)
def solution(A, B):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1
    survivals = 0
    stack = []
    for i ,value in enumerate(A):
        if B[i] == 0:
            while len(stack) != 0:
                if stack[-1] > value:
                    break
                else:
                    stack.pop()
            else:
                survivals +=1
        else:
            stack.append(value)
    survivals += len(stack)
    return survivals
