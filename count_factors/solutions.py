# 100% soluton time complexity O(n)
def solution(N):
    tracking_list = []
    for x in range(1, int(N ** 0.5 + 1)):
        if N % x == 0:
            if x != N / x:
                tracking_list.append(x)
                tracking_list.append(N / x)
            else:
                tracking_list.append(x)
    return len(tracking_list)
