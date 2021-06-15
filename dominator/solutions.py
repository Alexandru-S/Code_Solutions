# 100% time complexity O(n)
def solution(A):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return 0
    tracking_dict = {}
    N = len(A)
    for x in A:
        tracking_dict[x] = tracking_dict[x] + 1 if x in tracking_dict else 1
    sorted_dict = {
        k: v
        for k, v in sorted(
            tracking_dict.items(), key=lambda item: item[1], reverse=True
        )
    }
    treshhold = N / 2
    denominator = list(sorted_dict.values())[0]
    dominator = list(sorted_dict.keys())[0]
    if denominator > treshhold:
        return A.index(dominator)
    else:
        return -1
