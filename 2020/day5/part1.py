with open("test.txt") as f:
    seats = f.read().splitlines()

seat_ids = []

for seat in seats:

    lower_lim = 0
    upper_lim = 127

    upper_col = 7
    lower_col = 0

    for s in seat[:-3]:

        diff = (upper_lim - lower_lim + 1)/2
        if s == "F":
            upper_lim = upper_lim - diff
        else:

            lower_lim = lower_lim + diff

    if lower_lim == upper_lim:
        row = lower_lim
    else:
        print("Broken ================================")

    for c in seat[-3:]:
        
        diff = (upper_col - lower_col + 1)/2

        if c == "L":
            upper_col -= diff
        else:
            lower_col += diff

    if lower_col == upper_col:
        column = lower_col
    else:
        print("Broken Column ================================")

    seat = (row * 8) + column
    seat_ids.append(seat)

max_value = max(seat_ids)
print("Max seat ID")
print(max_value)