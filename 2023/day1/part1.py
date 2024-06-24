with open('sample.txt') as file:
    lines = file.read().splitlines()

for l in lines:
    print(l)