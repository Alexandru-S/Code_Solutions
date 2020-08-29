def solution(X, A):
    tupple = list(enumerate(A))
    result = list(filter(lambda x: x[1] == X, tupple))
    if result:
        return result[0][0]
    else:
        return -1