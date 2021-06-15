import itertools


def solve(arr):
    all_combinations = []
    for x in range(1, len(arr) + 1):
        for subset in itertools.combinations(arr, x):
            if len(subset) > 1:
                result = None
                for y in subset:
                    if not result:
                        result = y
                    else:
                        result = result | y
                all_combinations.append(result)
    return sum(all_combinations)


n = int(input())
arr = list(map(int, input().split(" ")))

out_ = solve(arr)
print(out_)
