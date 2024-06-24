with open('day1\\test.txt') as file:
    lines = file.read().splitlines()

total = 0
for line in lines:
    
    nums = []

    for char in line:
        if char.isdigit():
            nums.append(char)

    val_char = nums[0] + nums[-1]

    val = int(val_char)

    total += val

print(total)

