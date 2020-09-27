# 63% time complexity O(n**3)
def solution(A):
    # Count of triangles
    count = 0
    n = len(A)

    # The three loops select three
    # different values from array
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (A[i] + A[j] > A[k] and
                        A[i] + A[k] > A[j] and
                        A[k] + A[j] > A[i]):
                    count += 1
    return count