import itertools


def getAlph(alph, N):
    new_list = ["".join(p) for p in itertools.product(alph, repeat=N)]
    full_alph = [x for x in new_list if x == x[::-1]]
    return full_alph


def Solve(k):
    alph = "abcd"
    k_shift = k - 1
    bits = k_shift.bit_length()
    print("bits", bits)
    if bits > 2:
        if bits % 2 == 0:
            N = bits
        else:
            N = bits + 1
    else:
        N = 2
    print("n", N)
    print(getAlph(alph, N))
    return k


T = int(input())
for _ in range(T):
    k = int(input())

    out_ = Solve(k)
    print(out_)
#####################SECOND WAY###############################################

from itertools import chain, combinations
from functools import reduce


def all_subsets(arr):
    return chain(*map(lambda x: combinations(arr, x), range(len(arr) + 1)))


def solve(arr):
    all_comb = []

    for x in all_subsets(arr):
        if len(x) <= 1:
            continue
        if len(x) > 1:
            all_comb.append(list(x))
    sum_arr = []
    for substr in all_comb:
        res = reduce(lambda x, y: x | y, substr)
        sum_arr.append(res)
    return sum(sum_arr) % 1000000007


n = int(input())
if n == 1 or n == 0:
    print(0)
else:
    arr = list(map(int, input().split(" ")))
    out_ = solve(arr)
    print(out_)
