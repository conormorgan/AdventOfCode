with open('day6\input.txt') as file:
    records = file.read().splitlines()

time = int("".join(records[0].split(":")[1].split()))
distance = int("".join(records[1].split(":")[1].split()))

race = (time,distance)
num_ways = 1

count = 0
time, record = race

half_t = int((time + 1)/2)

for t in range(1,half_t):

    distance = t * (time - t)

    if distance > record:
        count += 1

num_ways = num_ways * count

print(num_ways * 2)
