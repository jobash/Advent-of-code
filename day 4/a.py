class Square():
    def __init__(self) -> None:
        self.boardIndex = -1
        self.xPos = 0
        self.yPos = 0
        self.num = -1
        self.marked = False
    def __repr__(self):
        return str(self.num) + (" X" if self.marked else " -") + ("\n" if self.yPos == 4 else "") + ("\n" if self.yPos == 4 and self.xPos == 4 else "") 
    def __str__(self):
        return str(self.num) + (" X" if self.marked else " -") + ("\n" if self.yPos == 4 else "") + ("\n" if self.yPos == 4 and self.xPos == 4 else "")

squares: list[Square] = []

def applyNumber(number: int):
    for i in range(0, len(squares)):
        if squares[i].num == number:
            squares[i].marked = True

def checkRowAndCol(square: Square):
    row = filter(lambda sq: sq.boardIndex == square.boardIndex and sq.yPos == square.yPos, squares)
    allMarked = True
    for val in row:
        allMarked = allMarked and val.marked
    if allMarked:
        return square.boardIndex
    
    col = filter(lambda sq: sq.boardIndex == square.boardIndex and sq.xPos == square.xPos, squares)
    allMarked = True
    for val in col:
        allMarked = allMarked and val.marked
    if allMarked:
        return square.boardIndex

def checkBoards():
    for square in squares:
        if square.marked:
            bIndex = checkRowAndCol(square)
            if bIndex != None:
                return bIndex


def createBoard(lines: list[str], bIndex: int):
    for i in range(0, len(lines)):
        nums = lines[i].split()
        for j in range(0, len(nums)):
            square = Square()
            square.xPos = i
            square.yPos = j
            square.boardIndex = bIndex
            square.num = int(nums[j])
            squares.append(square)

with open('input.txt') as file:
    lines = file.readlines()
    numbers = lines[0]
    lastNumber = -1
    boardIndex = 1
    winner = None
    for i in range(2, len(lines), 6):
        createBoard(lines[i:i+5], boardIndex)
        boardIndex += 1
    
    for number in numbers.split(','):
        applyNumber(int(number))
        lastNumber = int(number)
        winner = checkBoards()
        if winner != None:
            break

    winningBoard = filter(lambda sq: sq.boardIndex == winner, squares)
    sum = 0
    for sq in winningBoard:
        if not sq.marked:
            sum += sq.num
    print(sum * lastNumber)