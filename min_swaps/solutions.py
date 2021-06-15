def minSwaps(N, arr):
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(N)}
    ans = 0
    for i in range(N):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1

            if cycle_size > 0:
                ans += cycle_size - 1
        return ans


N = int(input())
arr = list(map(int, input().split(" ")))
steps = []

if arr == sorted(arr) or arr == sorted(arr, reverse=True):
    print(0)
else:
    print(minSwaps(N, arr))
