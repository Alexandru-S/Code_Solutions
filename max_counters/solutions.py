#66% time comlpexity O(n*m)
def solution(N, A):
    counter_list = [0] * N
    for x in A:
        if 1 <=  x <= N:
            counter_list = increase(x, counter_list)
        else:
            counter_list = max_counter(counter_list)
    return counter_list


def increase(x, counter_list):
    counter_list[x - 1] += 1
    return counter_list


def max_counter(counter_list):
    result = [max(counter_list)] * len(counter_list)
    return result

