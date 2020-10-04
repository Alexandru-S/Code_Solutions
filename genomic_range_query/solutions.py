# 62% time complexity O(n*m)
def solution(S, P, Q):
    tracker = []
    for p, q in zip(P, Q):
        coord_string = list(set(S[p:q + 1]))
        if 'A' in coord_string:
            tracker.append(1)
        elif 'C' in coord_string:
            tracker.append(2)
        elif 'G' in coord_string:
            tracker.append(3)
        elif 'T' in coord_string:
            tracker.append(4)
    return tracker
