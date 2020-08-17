#97% accuracy
n = int(input())

def flipBit(binary):
    if(binary == 0):
        return len(binary)
    currLen = 0
    prevLen = 0
    maxLen = 0

    while(binary > 0):
        if ((binary & 1) == 0):
            currLen += 1
        elif ((binary & 1) == 1):
            prevLen = 0 if (binary & 2) == 1 else currLen
            currLen = 0
    
        maxLen = max(prevLen + currLen, maxLen)
        binary >>= 1
    return maxLen + 1



bit_length = str(n.bit_length())
binary = format(n, '
