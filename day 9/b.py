matrix = []
seenNodes = set()
def getBasinSize(number: int, row: int, col: int):
    size = 0
    if (row - 1, col) not in seenNodes and row > 0 and int(matrix[row - 1][col]) > number and int(matrix[row - 1][col]) < 9:
        seenNodes.add((row - 1, col))
        size += 1 + getBasinSize(int(matrix[row - 1][col]), row - 1, col)
    if (row + 1, col) not in seenNodes and row < len(matrix) - 1 and int(matrix[row + 1][col]) > number and int(matrix[row + 1][col]) < 9:
        seenNodes.add((row + 1, col))
        size += 1 + getBasinSize(int(matrix[row + 1][col]), row + 1, col)
    if (row, col - 1) not in seenNodes and col > 0 and int(matrix[row][col - 1]) > number and int(matrix[row][col - 1]) < 9:
        seenNodes.add((row, col - 1))
        size += 1 + getBasinSize(int(matrix[row][col - 1]), row, col - 1)
    if (row, col + 1) not in seenNodes and col < len(matrix[row]) - 1 and int(matrix[row][col + 1]) > number and int(matrix[row][col + 1]) < 9:
        seenNodes.add((row, col + 1))
        size += 1 + getBasinSize(int(matrix[row][col + 1]), row, col + 1)
    return size


lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    row = list(line)
    matrix.append(row)
basins = []
rowLength = len(matrix)
for row in range(0, rowLength):
    colLength = len(matrix[row])
    for col in range(0, colLength):
        lowPoint = True
        number = int(matrix[row][col])
        if col > 0:
            lowPoint = lowPoint and number < int(matrix[row][col - 1])
        if col < colLength - 1:
            lowPoint = lowPoint and number < int(matrix[row][col + 1])
        if row > 0:
            lowPoint = lowPoint and number < int(matrix[row - 1][col])
        if row < rowLength - 1:
            lowPoint = lowPoint and number < int(matrix[row + 1][col])
        if lowPoint:
            seenNodes = set()
            basins.append(1 + getBasinSize(number, row, col))

basins = sorted(basins, reverse=True)
print(basins[0] * basins[1] * basins[2])
