with open('test.txt') as file:
    directions = file.read().splitlines()

horizontal = 0
depth = 0

for d in directions:

    split = d.split()
    direction = split[0]
    mag = int(split[1])

    if direction == "forward":
        horizontal += mag

    if direction == "down":
        depth += mag
    
    if direction == "up":
        depth -= mag

print(horizontal * depth)