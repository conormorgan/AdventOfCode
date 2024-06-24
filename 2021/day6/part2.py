with open('test.txt') as file:
    f = file.readline()

fish_list = [int(x) for x in f.split(",")]

fish_dict = {}
for f in fish_list:
    if f in fish_dict:
        fish_dict[f] += 1
    else:
        fish_dict[f] = 1

# Uses dictionary, not list
def repopulate(fish):

    new_dict = {}

    # Just decrease the key for these fish
    normal_fish = [1,2,3,4,5,6,8]
    for f in normal_fish:
        if f in fish:
            new_dict[f-1] = fish[f]
    
    if 0 in fish:
        new_dict[8] = fish[0]
        if 7 in fish:
            new_dict[6] = fish[0] + fish[7]
        else:
            new_dict[6] = fish[0]
    else:
        if 7 in fish:
            new_dict[6] = fish[7]
    
    return new_dict
        


for day in range(256):

     fish_dict = repopulate(fish_dict)

total = 0
for fish in fish_dict:

    total += fish_dict[fish]

print(total)