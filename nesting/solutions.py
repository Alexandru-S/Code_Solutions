# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    left_count = 0
    right_count = 0
    if len(S) == 0:
        return 0
    else:
        for x in S:
            if x == '(':
                left_count+=1
            elif x ==')':
                right_count+=1
        if (left_count - right_count) == 0:
            return 1
        else:
            return 0
