# 100% accurate
import sys

n = int(input())


def findMin(arr, n):
    sumofelem = sum(arr)
    dp = [[0 for i in range(sumofelem + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for j in range(1, sumofelem + 1):
        dp[0][j] = False
    for i in range(1, n + 1):
        for j in range(1, sumofelem + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

    diff = sys.maxsize
    for j in range(sumofelem // 2, -1, -1):
        if dp[n][j] == True:
            diff = sumofelem - (2 * j)
            break

    return diff


packages = list(map(int, input().split(" ")))
packages.sort()
print(findMin(packages, n))
