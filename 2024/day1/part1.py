with open("2024\day1\input.txt") as file:
    lists = file.read().splitlines()


locs1 = []
locs2 = []
for line in lists:
    x,y = line.split()

    locs1.append(int(x))
    locs2.append(int(y))

sorted_1 = sorted(locs1)
sorted_2 = sorted(locs2)

distance = 0

for i in range(len(sorted_1)):

    d = abs(sorted_1[i] - sorted_2[i])

    distance += d

print(distance)