nmx = list(map(int, input().split(" ")))
n = nmx[0]  # 2
m = nmx[1]  # 5
x = nmx[2]  # 3
matrix = [list(map(int, input().split(" "))) for x in range(n)]
count = 0
for x in matrix:
    for y in x:
        if y >= 3:
            count += 1
print(count)
for x in range(len(matrix)):
    for y in matrix:
        for z in y:

            if z >= 3:
                count += 1

print(matrix)
