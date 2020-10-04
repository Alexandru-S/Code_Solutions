# 50% time complexity O(B -A)
def solution(A, B, K):
    list_of_num = list(range(A, B + 1))
    tracker = 0
    if A % K == 0:
        tracker += 1
    return int((B/K)) - int((A /K)) + int(tracker)
