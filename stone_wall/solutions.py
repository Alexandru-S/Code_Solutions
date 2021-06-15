def solution(H):
    last_block = None
    blocknum = 0
    for x in range(1, len(H)):
        if not last_block:
            last_block = H[x]
            continue
        elif H[x] == H[x - 1]:
            last_block = H[x]
        elif H[x] != H[x - 1]:
            if H[x] < H[x - 1]:
                blocknum += 1
            if H[x] > H[x - 1]:
                blocknum += 1
            last_block = H[x]
    return blocknum
