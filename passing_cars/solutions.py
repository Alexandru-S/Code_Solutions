def solution(A):
    count = 0
    multiple = 0
    for x in A:
        if x == 0:
            count+=1
        else:
            multiple += count
    return multiple