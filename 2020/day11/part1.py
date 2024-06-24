with open("sample.txt") as f:
    rows = f.read().splitlines()

rows_list = []
for row in rows:
    row_list = []
    for seat in row:
        row_list.append(seat)
    rows_list.append(row_list)

row_length = len(rows_list[0])

def getOccupiedSeats(i, j, r):

    occupied_seats = 0

    diffs = [-1,0,1]

    for d1 in diffs:

        if i + d1 >= 0 and i + d1 < row_length:

            for d2 in diffs:

                if j + d2 >= 0 and j + d2 < row_length:

                    if d1 != 0 and d2 != 0:
                        
                        #print("seat row {0} col {1}".format(i+d1, j+d2))
                        seat = r[i+d1][j+d2]

                        if seat == "#":
                            occupied_seats += 1
    # # Row above
    # if i - 1 >= 0:

    #     for d in diffs:
    #         if j+d >= 0 and j + d < row_length:
    #             seat = r[i-1][j+d]
    #             if seat == "#":
    #                 occupied_seats += 1

    # # Current Row

    # for d in diffs:
    #     if d != 0:
    #         if j+d >= 0 and j + d < row_length:
    #             seat = r[i][j+d]
    #             if seat == "#":
    #                 occupied_seats += 1

    # # Row below
    # if i + 1 < row_length:

    #     for d in diffs:
    #         if j+d >= 0 and j + d < row_length:
    #             seat = r[i+1][j+d]
    #             if seat == "#":
    #                 occupied_seats += 1

    return occupied_seats

def getNewGrid(grid):
    new_rows = []
    for i in range(len(grid)):
        new_row = []
        for j in range(row_length):
            seat = grid[i][j]

            if seat == "L":
                occupied = getOccupiedSeats(i,j,grid)
                if occupied == 0:
                    new_row.append("#")
                else:
                    new_row.append("L")

            if seat == ".":
                new_row.append(".")

            if seat == "#":
                occupied = getOccupiedSeats(i,j,grid)
                if occupied >= 4:
                    new_row.append("L")
                else:
                    new_row.append("#")

        new_rows.append(new_row)

    return new_rows

def printGrid(grid):
    print("----------------------")
    for row in grid:
        row_string = ""
        for seat in row:
            row_string += seat
        print(row_string)

grids_equal = False
old_grid = rows_list
while not grids_equal:
    new_grid = getNewGrid(old_grid)

    if new_grid == old_grid:
        grids_equal = True
    else:
        old_grid = new_grid

#printGrid(rows_list)
printGrid(new_grid)

seat_count = 0
for row in new_grid:
    for seat in row:
        if seat == "#":
            seat_count += 1
print("final seat count: " + str(seat_count))
print("solution not working")