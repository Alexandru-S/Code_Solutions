# 100% time comlpexity O(n+m)
def solution(N, A):
    counter_list = [0] * N
    max_1 = 0
    max_2 = 0
    for x in A:
        if 1 <= x <= N:
            if max_1 > counter_list[x - 1]:
                counter_list[x - 1] = max_1
            counter_list[x - 1] += 1
            if max_2 < counter_list[x - 1]:
                max_2 = counter_list[x - 1]
        else:
            max_1 = max_2
    counter_list = [max(max_1, i) for i in counter_list]
    return counter_list
