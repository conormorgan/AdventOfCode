with open("2024\day1\input.txt") as file:
    lists = file.read().splitlines()


locs1 = []
locs2 = []
for line in lists:
    x,y = line.split()

    locs1.append(int(x))
    locs2.append(int(y))

counts = {}

for loc in locs2:
    if loc in counts:
        counts[loc] += 1
    else:
        counts[loc] = 1

similarity = 0

for l in locs1:

    if l in counts:

        similarity += (l * counts[l])

print(similarity)