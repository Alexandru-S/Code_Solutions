import itertools


N = int(input())
arr = list(map(int, input().split(' ')))

xor_count = 0
global_count = 0


for i in range(N):
    if global_count == 0:
        global_count = arr[i]
    else:
        result = arr[i] ^ global_count
        if result == 0:
            xor_count += 1
        global_count = result


print(xor_count)