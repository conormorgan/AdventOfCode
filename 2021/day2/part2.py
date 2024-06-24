with open('test.txt') as file:
    directions = file.read().splitlines()

horizontal = 0
depth = 0
aim = 0

for d in directions:

    split = d.split()
    direction = split[0]
    mag = int(split[1])

    if direction == "forward":
        horizontal += mag
        depth += aim * mag

    if direction == "down":
        aim += mag
    
    if direction == "up":
        aim -= mag

print(horizontal * depth)