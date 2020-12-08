with open("test.txt") as f:
    groups = f.read().split("\n\n")

counts = []

for group in groups:
    answers = set()
    people = group.splitlines()

    for p in people:
        for answer in p:
            answers.add(answer)
    
    counts.append(len(answers))

print(sum(counts))
