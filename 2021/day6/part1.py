with open('sample.txt') as file:
    f = file.readline()

fish = [int(x) for x in f.split(",")]

def repopulate(fish):

    new_fish = []
    for f in fish:
        
        if f == 0:
            new_fish.append(6)
            new_fish.append(8)
        
        if f > 0:
            new_fish.append(f - 1)
    
    return new_fish



for day in range(256):
    fish = repopulate(fish)

print(len(fish))