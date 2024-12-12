import re

with open("2024\day3\input.txt") as file:
    memory = file.readlines()

total = 0
for m in memory:

    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)",m)

    for mul in muls:

        x,y = (int(x) for x in mul[4:-1].split(","))

        total += x * y 

print(total)