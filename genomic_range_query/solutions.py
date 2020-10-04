# 100% time complexity O(n+m)
def solution(S, P, Q):
    tracker = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i]+1]:
            tracker.append(1)
        elif 'C' in S[P[i]:Q[i]+1]:
            tracker.append(2)
        elif 'G' in S[P[i]:Q[i]+1]:
            tracker.append(3)
        else:
            tracker.append(4)
    return tracker
