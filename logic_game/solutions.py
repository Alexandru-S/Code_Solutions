# 100% works
for _ in range(int(input())):
    n = int(input())
    num = 0
    val = 0
    while n != 1:
        if n % 2 == 1:
            val += 2 ** (num + 1)
        n = n // 2
        num += 1
    if val != 0:
        print(val)
    else:
        print(pow(2, num))
