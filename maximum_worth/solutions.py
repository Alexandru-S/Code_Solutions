import numpy as np

N = int(input())
limit = list(map(int, input().split(' ')))
shop_matrix = []

for _ in range(N):
    shop_matrix.append(list(map(int, input().split(' '))))


array1 = np.array(shop_matrix)
array_trans = array1.transpose()

shop_matrix = array_trans.tolist() 
new_shop = [ for x in ]
print(new_shop)
