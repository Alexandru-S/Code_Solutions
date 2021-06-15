N = int(input())
arr = list(map(int, input().split(" ")))
arr.sort()

temp_val = None
xor_count = 0
for i in range(N):
    if not temp_val:
        temp_val = arr[i]
    else:
        result = temp_val ^ arr[i]
        if result == 0:
            xor_count += 1
        temp_val = result
print(xor_count)
