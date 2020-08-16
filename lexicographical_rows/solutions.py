import itertools
from itertools import permutations, combinations_with_replacement
def Solve (k):
    # Write your code here
    return k

T = int(input())
for _ in range(T):
    k = int(input())
    out_ = Solve(k)
    print (out_)

albhabet = 'abcd'
combinationlist = list(itertools.permutations(albhabet, 4))


new_list = [p for p in itertools.product(albhabet, repeat=4)]
properlist = []
for x in new_list:
    if x == x[::-1]:
        properlist.append(x)
print(properlist)

