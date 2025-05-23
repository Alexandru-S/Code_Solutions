# convert number to binary new way
n = 1
binary = format(n, "08b")
print(binary)

# convert binary to digits
binarry = "00001111"
digit_rep = int(binary, 2)

# get a list of all combinations in a list
import itertools

list = [1, 2, 3]
combination_list = list(itertools.combinations(list, 2))

# get paliandrome new way
def new_pal():
    sample_string = "LoL"
    reversed = sample_string[::-1]
    if reversed == sample_string:
        return True


# get factors of a number
def factors(n):
    return set(
        reduce(
            list.__add__,
            ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
        )
    )


test_str = "heloo world and to everyone"
# get all substrings of a string
res = [
    test_str[i:j] for i in range(len(test_str)) for j in range(i + 1, len(test_str) + 1)
]


def all_subsets(arr):
    return chain(*map(lambda x: combinations(arr, x), range(len(arr) + 1)))

    for x in all_subsets(arr):
        print(x)


test_list = ["a", "b", "c"]
# Bitwise OR among List elements
# Using reduce() + lambda + "|" operator
res = reduce(lambda x, y: x | y, test_list)
