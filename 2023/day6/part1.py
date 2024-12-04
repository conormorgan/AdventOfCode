with open('day6\input.txt') as file:
    records = file.read().splitlines()

times = [int(x) for x in records[0].split(":")[1].split()]
distances = [int(x) for x in records[1].split(":")[1].split()]

races = list(zip(times,distances))

num_ways = 1

for race in races:
    count = 0
    time, record = race

    for t in range(1,time):

        distance = t * (time - t)
        #print(distance)

        if distance > record:
            count += 1

    num_ways = num_ways * count

print(num_ways)
