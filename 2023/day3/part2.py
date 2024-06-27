with open('day3\input.txt') as file:
    schematic = file.read().splitlines()

gear_ratios = []

row_count = len(schematic)
col_count = len(schematic[0])

def get_surrounding_numbers(grid,gear_x,gear_y):

    nums = []

    previous_y = gear_y - 1 if gear_y - 1 >= 0 else 0
    last_y = gear_y + 1 if gear_y + 1 <= row_count else row_count - 1

    previous_x = gear_x - 1 if gear_x - 1 >= 0 else 0
    last_x = gear_x + 1 if gear_x + 1 < col_count else col_count - 1

    for y in range(previous_y, last_y + 1):
        for x in range(previous_x, last_x + 1):
            
            char = grid[y][x]

            if str.isnumeric(char):

                num = get_full_number(grid[y],x)

                if num not in nums:
                    nums.append(num)

    return nums

def get_full_number(line, i):

    n = ""
    char = line[i]
    j = i + 1
    char_j = line[j]

    while str.isnumeric(char) and i >= 0:
        n = char + n
        i-=1
        char = line[i]

    while j < col_count and str.isnumeric(char_j):

        n = n + char_j
        j+=1
        if j < col_count:
            char_j = line[j]

    # add number coordinates to end of num to use as an id in case of same number repeating
    n = n + "-" + str(i) + str(j)

    return n

for y in range(row_count):

    line = schematic[y]

    for x in range(col_count):

        char = line[x]

        if char == "*":
            nums = get_surrounding_numbers(schematic, x, y)

            #print(nums)

            if len(nums) == 2:

                # remove number ids
                ns = list(map(lambda n : int(n.split("-")[0]), nums))

                gear_ratios.append(ns[0] * ns[1])
        

#print(gear_ratios)
print(sum(gear_ratios))