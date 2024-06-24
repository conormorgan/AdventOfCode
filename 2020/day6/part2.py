with open("test.txt") as f:
    groups = f.read().split("\n\n")

counts = []

for group in groups:
    answers = dict()
    people = group.splitlines()

    for p in people:
        for a in p:
            if a not in answers:
                answers[a] = 1
            else:
                answers[a] = answers[a] + 1
        num_people = len(people)
    all_answered = [k for k,v in answers.items() if v == num_people]


    counts.append(len(all_answered))

print(sum(counts))
