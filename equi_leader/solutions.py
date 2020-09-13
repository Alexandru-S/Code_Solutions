100% time complexity O(n)
def solution(A):
    candidate_ele = ''
    candidate_cnt = 0

    for value in A:
        if candidate_ele == '':
            candidate_ele = value
            candidate_cnt = 1
        else:
            if value != candidate_ele:
                candidate_cnt -= 1
                if candidate_cnt == 0:
                    candidate_ele = ''
            else:
                candidate_cnt += 1

    if candidate_cnt == 0:
        return 0

    cnt = 0
    last_idx = 0

    for idx, value in enumerate(A):
        if value == candidate_ele:
            cnt += 1
            last_idx = idx

    if cnt < len(A) // 2:
        return 0

    equi_cnt = 0
    cnt_to_the_left = 0
    for idx, value in enumerate(A):
        if value == candidate_ele:
            cnt_to_the_left += 1
        if cnt_to_the_left > (idx + 1) // 2 and \
                cnt - cnt_to_the_left > (len(A) - idx - 1) // 2:
            equi_cnt += 1

    return equi_cnt