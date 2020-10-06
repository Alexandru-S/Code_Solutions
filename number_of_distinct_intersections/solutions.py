# 100% time complexity O(n)
def solution(A):
    disks = []
    left_limits = []
    right_limits = []
    for x in range(len(A)):
        left_limits.append(x - A[x])
        right_limits.append(x + A[x])
    left_limits.sort()
    right_limits.sort()
    start_point = 0
    end_point = 0
    intersection = 0
    opendiscs = 0
    while start_point < len(A):
        if left_limits[start_point] <= right_limits[end_point]:
            intersection += opendiscs
            if intersection > 10000000:
                return -1
            opendiscs += 1
            start_point += 1
        else:
            opendiscs -= 1
            end_point += 1
    return intersection
