with open("test.txt") as grid:
    map = grid.read().splitlines()

tree_count = 0
i = 0

for line in range(len(map)):

    row_size = len(map[line])

    if map[line][i] == "#":
        tree_count += 1

    i = (i+3) % len(map[line])

print(tree_count)
        