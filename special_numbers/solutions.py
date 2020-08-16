import itertools

def getAlph(alph ,N):
    new_list = [''.join(p) for p in itertools.product(alph, repeat=N)]
    full_alph = [ x for x in new_list if x == x[::-1]]
    return full_alph

def Solve (k):
    alph = 'abcd'
    k_shift = k-1
    bits = k_shift.bit_length()
    print('bits',bits)
    if bits > 2:
        if bits%2 == 0:
            N = bits
        else:
            N = bits+1
    else:
        N = 2
    print('n', N)
    print(getAlph(alph,N))
    return k

T = int(input())
for _ in range(T):
    k = int(input())

    out_ = Solve(k)
    print (out_)
