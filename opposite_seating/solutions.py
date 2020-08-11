num=int(input())

for x in range(num):
    position = 'NA'
    row = 0
    seat = int(input())
    opposite_seat = 0
    if seat < 6:
        if seat == 1:
            print("12 WS")
        if seat == 2:
            print("11 MS")
        if seat == 3:
            print("10 AS")
        if seat == 4:
            print("9 AS")
        if seat == 5:
            print("8 MS")

    if seat%6 == 0:
        row = seat//6
    else:
        row = (seat // 6) + 1

    if seat%6 == 0 or seat%6 == 1:
        position = 'WS'
    if seat%6 == 2 or seat%6 == 5:
        position = 'MS'
    if seat%6 == 3 or seat%6 == 4:
        position = 'AS'

    max_row_number = row*6
    min_row_number = ((row-1)*6)+1

    if row%2 != 0:
        opposite_seat = seat + (max_row_number - seat) *2 + 1
    if row%2 == 0:
        opposite_seat = (seat - min_row_number) *2 + 1

    print('%s %s' % (opposite_seat, position))
        
