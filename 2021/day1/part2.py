with open('test.txt') as file:
    depths = file.read().splitlines()

d = [int(x) for x in depths]

sums = []
for i in range(2, len(d)):

    sum = d[i] + d[i-1] + d[i-2]
    sums.append(sum)

increases = 0

for i in range(1,len(sums)):
        if sums[i] > sums[i-1] :
            increases += 1
            
print(increases)