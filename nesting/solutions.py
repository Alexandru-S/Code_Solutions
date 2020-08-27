# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    left_count = 0
    right_count = 0
    if len(S) == 0:
        return 0
    else:
        if int(len(S)) % 2 != 0:
            return 0
        else:
            for x in range(int(len(S)/2)):
                if S[x] == '(':
                    left_count+=1
                elif S[x] ==')':
                    right_count+=1
                otherway = (-(x) -1)
                if S[otherway] == '(':
                    left_count+=1
                elif S[otherway] ==')':
                    right_count+=1
            if (left_count - right_count) == 0:
                return 1
            else:
                return 0