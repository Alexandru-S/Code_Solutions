#66% time comlpexity O(n*m)
from itertools import repeat

def solution(N, A):
    counter_list = list(repeat(0, N))
    for x in A:
        if x <= N:
            counter_list = increase(x, counter_list)
        else:
            counter_list = max_counter(counter_list)
    return counter_list


def increase(x, counter_list):
    index_loc = x - 1
    counter_list[index_loc] += 1
    return counter_list


def max_counter(counter_list):
    max_count = sorted(counter_list, reverse=True)[0]
    result = list(repeat(max_count, len(counter_list)))
    return result
