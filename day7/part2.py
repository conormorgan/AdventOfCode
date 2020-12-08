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

            contains[bag] = int(count)
    else:
        for c in contents:
            count = c.split()[0]
            bag = c.split()[1] + " " + c.split()[2]

            contains[bag] = int(count)

    top_level_bag = ' '.join(rule.split("contain")[0].split()[0:2])
    r[top_level_bag] = contains

def getBagCounts(bag, r):

    count = 0
    for b in r[bag]:

        if b == "empty":
            return 0
        else:
            count += r[bag][b] + r[bag][b]*getBagCounts(b,r)
    return count

count = getBagCounts("shiny gold",r)
print(count)

