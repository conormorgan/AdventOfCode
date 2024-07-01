with open('day4\input.txt') as file:
    cards = file.read().splitlines()

scores = []

for card in cards:

    card_id, card_nums = card.split(":")
    cid = card_id.split()[-1]
    winning, mine = card_nums.split("|")

    win_nums = set(winning.split())
    my_nums = mine.split()

    intersect = win_nums.intersection(my_nums)

    score = 0
    if len(intersect) > 0:

        score = 2 ** (len(intersect) - 1)

    scores.append(score)

print(scores)
print(sum(scores))
