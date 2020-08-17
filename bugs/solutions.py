N = int(input())
bugs_array = []
for _ in range(N):
    task = list(map(int,input().split(' ')))
    if task[0] == 1:
        bugs_array.append(task[1])
        bugs_array.sort(reverse=True)
    if task[0] == 2:
        if len(bugs_array) < 3:
            print('Not enough enemies')
        else:
            location = (int(len(bugs_array)/3)) -1 if (len(bugs_array)/3) -1 >1 else 1
            print(bugs_array[location])
