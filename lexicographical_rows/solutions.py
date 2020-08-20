import itertools

T = int(input())
for _ in range(T):
    k = int(input())
    out_ = Solve(k)
    print (out_)

albhabet = 'abcd'

new_list = [p for p in itertools.product(albhabet, repeat=4)]
properlist = []
for x in new_list:
    if x == x[::-1]:
        properlist.append(x)
print(properlist)

