with open("test.txt") as f:
    adapters = f.read().splitlines()

a = [int(x) for x in adapters]

a.append(0)
a.append(max(a) + 3)
a.sort()

diffs = []

for i in range(len(a)):

    if i+1 < len(a):
        d = a[i+1] - a[i]
        diffs.append(d)

num3s = diffs.count(3)
num1s = diffs.count(1)
print(num3s)
print(num1s)
print(num3s*num1s)