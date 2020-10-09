# 100% time complexity O(n)
def solution(N):
    start = 0
    count = 0
    binary = format(int(N), '08b')
    tracking = []
    for x in binary:
        if start == 1 and x == '0':
            count += 1
        if start == 0 and x == '1':
            start = 1
        if start == 1 and x == '1':
            tracking.append(count)
            count = 0

    if len(tracking):
        tracking.sort()
        return tracking[-1]
    else:
        return 0
