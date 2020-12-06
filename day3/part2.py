with open("test.txt") as grid:
    map = grid.read().splitlines()

tree_counts = []
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for slope in slopes:

    i = 0
    tree_count = 0
    right = slope[0]
    down = slope[1]

    for line in range(0,len(map),down):

        width = len(map[line])
        
        if map[line][i] == "#":
            tree_count+=1

        i = (i + right) % width

    tree_counts.append(tree_count)

total = 1
for count in tree_counts:
    total*=count

print(total)
