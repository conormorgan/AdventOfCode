import re

with open("2024\day3\input.txt") as file:
    memory = file.read()

def find_muls(m):

    total_mul = 0
    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)",m)

    for mul in muls:

        x,y = (int(x) for x in mul[4:-1].split(","))

        total_mul += x * y 
    
    return total_mul

total = 0
donts = memory.split("don't()")

# first index is always a do()
total += find_muls(donts[0])

for dont in donts[1:]:

    if "do()" in dont:

        # first value in the list is directly after dont(), so skip first value
        dos = dont.split("do()")[1:]

        for d in dos:
            total += find_muls(d)

print(total)

# Can use regex to get all instances of do() and don't() too

# enabled = True
# total = 0

# muls = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", memory)

# for mul in muls:

#     if mul == "do()":
#         enabled = True
#     elif mul == "don't()":
#         enabled = False
#     elif enabled:

#         x,y = [int(i) for i in mul[4:-1].split(",")]

#         total += x * y 

# print(total)