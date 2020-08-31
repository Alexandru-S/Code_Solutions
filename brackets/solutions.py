def solution(S):
    if int(len(S)) == 0:
        return 1
    else:
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        bracket_count = [0, 0, 0]
        for x in S:
            for y in range(len(bracket_count)):
                if x == closing_brackets[y] and bracket_count[y] == 0:
                    return 0
                elif x == opening_brackets[y]:
                    bracket_count[y]+=1
                else:
                    bracket_count[y] -=1
        return 1