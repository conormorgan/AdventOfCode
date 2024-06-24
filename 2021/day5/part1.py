with open('sample.txt') as file:
    vents = file.read().splitlines()

allvents = {}

for vent in vents:

    split = vent.split('->')
    start = split[0].strip()
    end = split[1].strip()
    
    x_1 = int(start.split(",")[0])
    x_2 = int(end.split(",")[0])
    
    if x_1 > x_2:
        x_start = x_2
        x_end = x_1
    else:
        x_start = x_1
        x_end = x_2

    y_1 = int(start.split(",")[1])
    y_2 = int(end.split(",")[1])
    
    if y_1 > y_2:
        y_start = y_2
        y_end = y_1
    else:
        y_start = y_1
        y_end = y_2

    points = []
    
    if x_start == x_end:
        for y in range(y_start,y_end + 1):
            points.append(str(x_start) + "," + str(y))

    if y_start == y_end:
        for x in range(x_start,x_end + 1):
            points.append(str(x) + "," + str(y_start))
    
    for p in points:
        if p in allvents:
            allvents[p] += 1
        else:
            allvents[p] = 1

overlaps = len([p for p in allvents if allvents[p] > 1])
print(overlaps)