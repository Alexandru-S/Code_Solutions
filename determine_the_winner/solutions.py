T = int(input())


flash_global = 0
cisco_global = 0

f_times = []
c_times = []


def calc_score(scores, decreases, student):
    tmp_score = 0
    for i, j, k in zip(scores, decreases, student):
        valid_score = i - j * k if i / 2 < i - j * k else i / 2
        tmp_score += valid_score
    return tmp_score


for _ in range(T):
    s = list(map(int, input().split(" ")))
    d = list(map(int, input().split(" ")))
    f = list(map(int, input().split(" ")))
    c = list(map(int, input().split(" ")))
    f_times += f
    c_times += c

    flash_total = calc_score(s, d, f)
    cisco_total = calc_score(s, d, c)
    flash_global += flash_total
    cisco_global += cisco_total

    if flash_total == cisco_total:
        f_times.sort()
        c_times.sort()
        if f[0] < c[0]:
            print("Flash")
        elif f[0] > c[0]:
            print("Cisco")
        else:
            print("Tie")
    else:
        if flash_total > cisco_total:
            print("Flash")
        else:
            print("Cisco")
