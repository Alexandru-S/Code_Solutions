A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5

def solution(X, A):
    if len(A) == 0:
        return -1
    numbers_object = {i:A[i] for i in range(len(A))}
    result = list(numbers_object.keys())[list(numbers_object.values()).index(X)]
    return result
solution(X,A)