import math


def primeTnumber(xi):
    if xi > 0 and xi <4:
        return 'NO'
    sqrt = math.sqrt(xi)
    if sqrt in prime_list:
        return 'YES'
    else:
        return 'NO'


def generatePrimes(start, stop):
    prime_list = []
    for x in range(start, stop +1):
        if x > 1:
            for i in range(2, x):
                if x%i == 0:
                    break;
                else:
                    prime_list.append(x)
    prime_list = list(set(prime_list))
    prime_list.insert(0, 2)
    return prime_list


n = int(input())
numbers_array = list(map(int, input().split(' ')))
prime_list = generatePrimes(1, 1012)

for x in range(n):
    print(primeTnumber(numbers_array[x]))
