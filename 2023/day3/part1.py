with open('day3\input.txt') as file:
    schematic = file.read().splitlines()

symbols = "!\"#$%&'()*+,-/:;<=>?@[\]^_`{|}~"
part_nums = []

row_count = len(schematic)
col_count = len(schematic[0])

print(row_count)
print(col_count)

def check_if_symbol_touches(grid, current_y, x1, x2):

    previous_y = current_y - 1 if current_y - 1 >= 0 else 0
    last_y = current_y + 1 if current_y + 1 <= row_count else row_count - 1

    previous_x = x1 - 1 if x1 - 1 >= 0 else 0
    last_x = x2 + 1 if x2 + 1 < col_count else col_count - 1

    # print(f"previous y {previous_y} last y {last_y}")
    # print(f"previous x {previous_x} last x {last_x}")

    for y in range(previous_y, last_y + 1):
        for x in range(previous_x, last_x + 1):
            
            char = grid[y][x]

            # print(char)

            if char in symbols:
                return True
    
    return False


for y in range(row_count):

    line = schematic[y]
    num = ""

    for x in range(col_count):

        char = line[x]

        if str.isnumeric(char):
            num += char

        if x + 1 == col_count and num != "":
            
            start_x = start_x = x - len(num)
            end_x = x
            
            # print(f"row {y} start {start_x} end {end_x} number {num}")

            is_part = check_if_symbol_touches(schematic, y, start_x, end_x)
            
            if is_part:
                part_nums.append(int(num))

            num = ""

        if not str.isnumeric(char) and num != "":

            start_x = x - len(num)
            end_x = x - 1

            # print(f"row {y} start {start_x} end {end_x} number {num}")

            is_part = check_if_symbol_touches(schematic, y, start_x, end_x)
            
            if is_part:
                part_nums.append(int(num))

            num = ""

# print(part_nums)
print(sum(part_nums))