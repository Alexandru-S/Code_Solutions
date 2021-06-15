import collections


mainstring = str(input())

all_substrings = [
    mainstring[i:j]
    for i in range(len(mainstring))
    for j in range(i + 1, len(mainstring) + 1)
    if len(mainstring[i:j]) > 2
]

main_diff = []

for x in all_substrings:
    col1 = collections.Counter(x).most_common()
    most_common = col1[0][1]
    least_common = col1[-1][1]
    main_diff.append(most_common - least_common)


print(sum(main_diff))
