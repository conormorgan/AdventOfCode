with open('test.txt') as file:
    binary = file.read().splitlines()

gamma = ""
epsilon = ""

size = len(binary[0])

positions = dict()
for bin in binary:

    for i in range(size):
        if str(i) in positions:
            positions[str(i)] += bin[i]
        else:
            positions[str(i)] = bin[i]

for key in positions:

    bits = positions[key]
    ones = bits.count("1")
    if ones >= len(bits)/2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
g = int(gamma, 2)
e = int(epsilon, 2)

print(g * e)
