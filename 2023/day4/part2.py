with open('day4\input.txt') as file:
    cards = file.read().splitlines()

card_win_counts = {}
card_counts = {}
for card in cards:

    card_id, card_nums = card.split(":")
    cid = int(card_id.split()[-1])
    winning, mine = card_nums.split("|")

    win_nums = set(winning.split())
    my_nums = mine.split()

    intersect = win_nums.intersection(my_nums)

    num_of_copies = len(intersect)

    card_win_counts[cid] = num_of_copies
    card_counts[cid] = 1


for count_id in card_counts.keys():
    
    for copy in range(card_counts[count_id]):
        num_copies = card_win_counts[count_id]
        for c in range(count_id + 1, count_id + num_copies + 1):
            card_counts[c] += 1

print(sum(card_counts.values()))