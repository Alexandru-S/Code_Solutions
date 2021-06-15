# 100% time complexity O(n)
def solution(M, A):
    accessed = [-1] * (M + 1)  # -1: not accessed before
    # Non-negative: the previous occurrence position
    front, back = 0, 0
    result = 0
    for front in range(len(A)):
        if accessed[A[front]] == -1:
            # Met with a new unique item
            accessed[A[front]] = front
        else:
            # Met with a duplicate item
            # Compute the number of distinct slices between newBack-1 and back
            # position.
            newBack = accessed[A[front]] + 1
            result += (newBack - back) * (front - back + front - newBack + 1) / 2
            if result >= 1000000000:
                return 1000000000
            # Restore and set the accessed array
            for index in range(back, newBack):
                accessed[A[index]] = -1
            accessed[A[front]] = front
            back = newBack
    # Process the last slices
    result += (front - back + 1) * (front - back + 2) / 2
    return int(min(result, 1000000000))
