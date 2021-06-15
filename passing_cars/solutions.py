# 100% time complexity O(n)
def solution(A):
    count = 0
    multiple = 0
    for x in A:
        if x == 0:
            count += 1
        else:
            multiple += count
    if multiple > 1000000000:
        return -1
    return multiple
