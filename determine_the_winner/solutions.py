

T = int(input())

def calc_score(scores, decreases, student):
    tmp_score = 0
    for i, j, k in zip(scores, decreases, student):
        tmp_score += i - j*k
    return tmp_score

flash_global = 0 
cisco_global = 0

for x in range(T):
    scores = map(int, raw_input().split(' '))
    decreases = map(int, raw_input().split(' '))
    flash = map(int, raw_input().split(' '))
    cisco = map(int, raw_input().split(' '))
    flash_total = 0
    cisco_total = 0

    flash_total = calc_score(scores, decreases, flash)
    cisco_total = calc_score(scores, decreases, cisco)
    flash_global += flash_total
    cisco_global += cisco_total
    if flash_global == cisco_global:
        cisco.sort()
        flash.sort()
        if flash[-1] < cisco[-1]:
            print('Flash')
        elif flash[-1] > cisco[-1]:
            print('Cisco')
        else:
            print('Tie')
    else:
        if flash_global > cisco_global:
            print('Flash')
        else:
            print('Cisco')
