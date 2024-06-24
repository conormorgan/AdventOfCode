with open('test.txt') as file:
    bingo = file.read().splitlines()

numbers = bingo[0].split(',')
boards = [[]]
for i in range(2,len(bingo)):
    if len(bingo[i])>0:
        boards[-1].append(bingo[i].split())
    else:
        boards.append([])

def checkWinner(board, line, col, num):

    
    if all(cell == line[0] for cell in line):
        return True

    column = []
    for l in board:
        column.append(l[col])

    if all(col == column[0] for col in column):
        return True
    
    return False

def sumOfWinningBoard(board):

    total = 0
    for line in board:
        total += sum([int(x) for x in line if x != "-1"])
    
    return total

won = False
winningBoards = set()
numBoards = len(boards)


for num in numbers:

    for b,board in enumerate(boards):

        for line in board:

            for c in range(len(line)):

                if line[c] == num:

                    line[c] = "-1"
                    # marked a number so check board
                    if checkWinner(board, line, c, num):

                        if b not in winningBoards and len(winningBoards) == numBoards-1:
                            won = True
                            total = sumOfWinningBoard(board) * int(num)

                            break
                        else:
                            winningBoards.add(b)
            
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