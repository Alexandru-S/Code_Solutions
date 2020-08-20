def solve (query, s, t):
    result = []
    for x in query:
        start_index = x[0]-1
        to_remove = s[start_index:x[1]]
        new_result = s.replace(to_remove, '')
        if t in new_result:
            result.append('Yes')
        else:
            result.append('No')
    return result

s = input()
t = input()
q = list(map(int, input().split(' ')))
query = []
for _ in range(q[0]):
    query.append(list(map(int, input().split())))

out_ = solve(query, s, t)
for i_out_ in out_:
    print (i_out_)