with open('day5\sample.txt') as file:
    almanac = file.read().split("\n\n")

s = almanac[0].splitlines()[0].split(":")[-1].split()
seeds = [int(x) for x in s]
print(seeds)

locs = []
for seed in seeds:
    val = seed
    for a in almanac:
        data = a.splitlines()
        if len(data) > 1:
            
            for i in range(1, len(data)):
                dest, source, r = (int(x) for x in data[i].split())
                
                if val >= source and val < source + r:
                    diff = val - source

                    val = dest + diff

                    break
    locs.append(val)

print(min(locs))