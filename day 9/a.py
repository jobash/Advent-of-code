matrix = []

lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    row = list(line)
    matrix.append(row)
sum = 0
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
            sum += (number + 1)

print(sum)
