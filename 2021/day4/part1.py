with open('test.txt') as file:
    bingo = file.read().splitlines()

#print(bingo)
numbers = bingo[0].split(',')
boards = [[]]
for i in range(2,len(bingo)):
    if len(bingo[i])>0:
        boards[-1].append(bingo[i].split())
    else:
        boards.append([])

def checkWinner(board, line, col):

    win = all(cell == line[0] for cell in line)

    if not win:
        column = []
        for l in board:
            column.append(l[col])
        win = all(cell == line[0] for cell in line)
    
    return win

def sumOfWinningBoard(board):

    total = 0
    for line in board:
        total += sum([int(x) for x in line if x != "-1"])
    
    return total

won = False
for num in numbers:

    for board in boards:
        for line in board:
            for i in range(len(line)):
                if line[i] == num:
                    line[i] = "-1"
                    # marked a number so check board
                    if checkWinner(board, line, i):
                        won = True
                        total = sumOfWinningBoard(board) * int(num)
                        break
            
            if won:
                break
        
        if won:
            break
    if won:
        break

# for board in boards:
#     for line in board:
#         print(line)
#     print("=======")


print(total)