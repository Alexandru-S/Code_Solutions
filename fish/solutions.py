# 100% time complexity O(n)
def solution(H):
    N = len(H)
    stones = 0
    stack = [0] * N
    stack_num = 0

    for i in range(N):
        while stack_num > 0 and stack[stack_num - 1] > H[i]:
            stack_num -= 1
        if stack_num > 0 and stack[stack_num - 1] == H[i]:
            pass
        else:
            stones += 1
            stack[stack_num] = H[i]
            stack_num += 1
    return stones
