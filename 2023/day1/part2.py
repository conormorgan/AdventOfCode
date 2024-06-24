with open('day1\\test.txt') as file:
    lines = file.read().splitlines()

numbers = { 
    "one" : "one1one",
    "two": "two2two",    
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six" : "six6six",
    "seven" : "seven7seven",
    "eight" : "eight8eight",
    "nine" : "nine9nine"
    }

total = 0
for line in lines:
    
    for num in numbers.keys():
        
        if num in line:
            line = line.replace(num, numbers[num])

    nums = []
    for char in line:
        if char.isdigit():
            nums.append(char)

    #print(line)

    val_char = nums[0] + nums[-1]

    val = int(val_char)

    total += val

print(f"Value: {total}")