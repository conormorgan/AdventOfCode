with open("2024\day2\input.txt") as file:
    reports = file.read().splitlines()

def get_diffs(ls):
    diffs = []

    for i in range(1,len(ls)):
        l1 = ls[i - 1]
        l2 = ls[i]       

        diff = l1 - l2
        diffs.append(diff)

    return diffs

def safe(ls):
    
    ds = get_diffs(ls)
    all_in_neg_range = all(d < 0 and abs(d) > 0 and abs(d) <= 3 for d in ds)
    all_in_pos_range = all(d > 0 and abs(d) > 0 and abs(d) <= 3 for d in ds)

    return all_in_neg_range or all_in_pos_range

count = 0
for report in reports:
    levels = [int(x) for x in report.split()]

    # checks through all values that if removing each level still makes the levels safe
    # Only need to check the levels that cause the initial error?
    all_combos = []
    for i in range(len(levels)):
        res = safe(levels[:i] + levels[i + 1:])
        all_combos.append(res)

    if any(all_combos):
        count += 1

print(count)


