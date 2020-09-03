def solution(A, B):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1
    surviving_fish = []
    current_fish = None
    for index, value in enumerate(A):
        if index == 0:
            if index == 0:
                current_fish = A[index]
                surviving_fish.append(A[index])
                current_fish = None
            else:
                if current_fish is None:
                    current_fish = A[index]
                if current_fish > A[index - 1]:
                    A[index - 1] = 0
                elif current_fish < A[index - 1]:
                    A[index] = 0
                    current_fish = None
        else:
            if index == len(A) - 1:
                current_fish = A[index]
                surviving_fish.append(A[index])
                current_fish = None
            else:
                if current_fish is None:
                    current_fish = A[index]
                if current_fish > A[index + 1]:
                    A[index + 1] = 0
                elif current_fish < A[index + 1]:
                    A[index] = 0
                    current_fish = None
    return len(surviving_fish)

