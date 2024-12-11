with open("2024\day2\input.txt") as file:
    reports = file.read().splitlines()

count = 0
for report in reports:
    levels = [int(x) for x in report.split()]

    diffs = []

    for i in range(1,len(levels)):
        l1 = levels[i - 1]
        l2 = levels[i]       

        diff = l1 - l2
        diffs.append(diff)

    all_in_neg_range = all(d < 0 and abs(d) > 0 and abs(d) <= 3 for d in diffs)
    all_in_pos_range = all(d > 0 and abs(d) > 0 and abs(d) <= 3 for d in diffs)

    if all_in_neg_range or all_in_pos_range:
        count += 1

print(count)


