# 50% time complexity O(B -A)
def solution(A, B, K):
    list_of_num = list(range(A, B + 1))
    tracker = []
    for x in list_of_num:
        if x % K == 0:
            tracker.append(x)
    return len(tracker)
