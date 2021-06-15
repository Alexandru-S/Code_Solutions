T = int(input())
for _ in range(T):
    nk = list(map(int, input().split(" ")))
    n = nk[0]
    k = nk[1]
    A = list(map(int, input().split(" ")))
    if n == 0:
        print([])
    result = k % n if k > n else k
    rotated_array = A[-result:] + A[:-result]
    str_rep = " ".join([str(x) for x in rotated_array])
    print(str_rep)
