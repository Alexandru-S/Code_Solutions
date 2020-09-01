#100% time complexity O(n)
def solution(S):
    if int(len(S) % 2) != 0:
        return 0
    if int(len(S)) == 0:
        return 1
    else:
        opening_brackets = ['(', '{', '[']
        closing_brackets = [')', '}', ']']
        bracket_count = [0, 0, 0]
        last_opened_bracket = None
        for x in S:
            for y in range(len(bracket_count)):
                if last_opened_bracket:
                    if x == closing_brackets[y]:
                        if x != closing_brackets[opening_brackets.index(last_opened_bracket)]:
                            return 0
                        else:
                            last_opened_bracket = None
                if x == closing_brackets[y] or x == opening_brackets[y]:
                    if x == closing_brackets[y] and bracket_count[y] == 0:
                        return 0
                    elif x == opening_brackets[y]:
                        bracket_count[y]+=1
                        last_opened_bracket = x
                    elif x == closing_brackets[y] and bracket_count[y] != 0:
                        bracket_count[y] -=1
        if sum(bracket_count) > 0:
            return 0
        else:
            return 1