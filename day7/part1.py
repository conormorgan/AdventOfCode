with open("test.txt") as f:
    rules = f.read().splitlines()

r = dict()
for rule in rules:

    contains = dict()
    contents = rule.split("contain")[1].split(",")

    if len(contents) == 1:
        if contents[0] == " no other bags.":
            contains["empty"] = 0
        else:
            count = contents[0][:-1].split()[0]
            bag = " ".join(contents[0][:-1].split()[1:3])

            contains[bag] = count
    else:
        for c in contents:
            count = c.split()[0]
            bag = c.split()[1] + " " + c.split()[2]

            contains[bag] = count

    top_level_bag = ' '.join(rule.split("contain")[0].split()[0:2])
    r[top_level_bag] = contains

def getGoldBags(bag, rules):

    bags_inside = rules[bag]
    for b in bags_inside:
        if b == "shiny gold" or (b != "empty" and getGoldBags(b,rules)):
            return True
        elif b == "empty":
            return False

count = 0
for b in r:
    if getGoldBags(b,r):
        count += 1
print(count)