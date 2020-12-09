with open("test.txt") as f:
    code = f.read().splitlines()

visited_indices = []
acc = 0

i = 0
while i < len(code):

    if i not in visited_indices:
        visited_indices.append(i)
        instruction = code[i].split()[0]
        num = int(code[i].split()[1])
        
        if instruction == "acc":
            acc += num
            i += 1
        elif instruction == "jmp":
            i += num
        else:
            i += 1
    else:
        break
    
print(visited_indices)
print(acc)