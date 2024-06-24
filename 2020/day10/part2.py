from typing import Dict


with open("test.txt") as f:
    adapters_txt = f.read().splitlines()

adapters = [int(x) for x in adapters_txt]
adapters.append(0)
adapters.sort()

print(adapters)

ways_to_connect = dict()
ways_to_connect[0] = 1

for a in adapters[1:]:
    ways_to_connect[a] = ways_to_connect.get(a-1,0) + ways_to_connect.get(a-2,0) + ways_to_connect.get(a-3,0)

print(ways_to_connect[adapters[-1]])