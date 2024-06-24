with open("test.txt") as f:
    numbers = f.read().splitlines()

numbers = [int(x) for x in numbers]

print(numbers)

target = 41682220
target_not_found = True
i = 0

while i < len(numbers) and target_not_found:
    added_nums = []

    n = numbers[i:]

    for j in range(len(n)):
        if sum(added_nums) >= target:
            break
        else:
            added_nums.append(n[j])
            
    if sum(added_nums) == target:
        target_not_found = False

        
    i+=1
    
    
print(added_nums)
final = min(added_nums) + max(added_nums)
print(final)
