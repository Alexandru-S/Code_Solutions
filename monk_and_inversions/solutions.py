T = int(input())

for _ in range(T):
    N = int(input())
    matrixN = []
    for x in range(N):
        matrixN.append(list(map(int, input().split(" "))))

    c = 0
    for i in range(N):
        for j in range(N):
            for p in range(N):
                for q in range(N):
                    if i <= p and j <= q:
                        if matrixN[i][j] > matrixN[p][q]:
                            c += 1
    print(c)
