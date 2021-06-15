# 100% time complexity O(n)
def solution(S):
    if int(len(S) % 2) != 0:
        return 0
    else:
        if int(len(S)) == 0 or S == "":
            return 1
        count = 0
        for x in S:
            if x == "(":
                count += 1
            else:
                if count == 0:
                    return 0
                count -= 1
        if count == 0:
            return 1
        else:
            return 0
