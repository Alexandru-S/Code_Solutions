import numpy as np
N = int(input())
limit = list(map(int, input().split(' ')))
shop_matrix = []

for _ in range(N):
    shop_matrix.append(list(map(int, input().split(' '))))

array1 = np.array(shop_matrix)
array_trans = array1.transpose()

shop_matrix = array_trans.tolist()
sorted_matrix = []

for x in shop_matrix:
    new_arr = sorted(x, reverse=True)
    sorted_matrix.append(new_arr)

print('=-===', sorted_matrix)

priced_matrix = []
for x in range(N):
    print('highest price', )
    highest = sorted_matrix.index(max(sorted_matrix))
    price =
