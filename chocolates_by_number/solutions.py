# 12% time complexity O(n)
def solution(N, M):
    counter = True
    tracking_list = []
    list_index = 0
    while counter:
        if list_index > N - 1:
            list_index = list_index - N
        if list_index in tracking_list:
            counter = False
        else:
            tracking_list.append(list_index)

        list_index += M
    return len(tracking_list)
