with open("test.txt") as f:
    code = f.read().splitlines()

jmp_nop = []

for x in range(len(code)):
    if code[x].split()[0] == "jmp" or code[x].split()[0] == "nop":
        jmp_nop.append(x)

code_map = {"jmp":"nop", "nop":"jmp"}

for jp in jmp_nop:
    visited_indices = []
    acc = 0
    i = 0
    while i < len(code) and i not in visited_indices:
        visited_indices.append(i)
        
        if i == jp:
            instruction = code_map[code[i].split()[0]]
            num = int(code[i].split()[1])
        else:
            instruction = code[i].split()[0]
            num = int(code[i].split()[1])
        
        if instruction == "acc":
            acc += num
            i += 1
        elif instruction == "jmp":
            i += num
        else:
            i += 1
    
    if i == len(code):
        print(acc)

