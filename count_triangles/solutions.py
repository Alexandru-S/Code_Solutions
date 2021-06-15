# 63% time complexity O(n**2)
def solution(A):
    A.sort()
    count = 0
    for x in range(len(A) - 1, 0, -1):
        l = 0
        r = x - 1
        while l < r:
            if A[l] + A[r] > A[x]:
                count += r - l
                r -= 1
            else:
                l += 1
    return count
