with open('test.txt') as file:
    depths = file.read().splitlines()

d = [int(x) for x in depths]
increases = 0

for i in range(1,len(d)):
        if d[i] > d[i-1] :
            increases += 1
            
print(increases)
list_comp = len([d[i] for i in range(1,len(d)) if d[i] > d[i-1]])
print(list_comp)