m = 1000
n = 1000
matrix = [ [0]*m for _ in range(n) ]

lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    parts = line.split('->')
    startParts = parts[0].split(',')
    endParts = parts[1].split(',')
    x1 = int(startParts[0].rstrip())
    y1 = int(startParts[1].rstrip())
    x2 = int(endParts[0].rstrip())
    y2 = int(endParts[1].rstrip())
    if x1 == x2:
        if y2 <= y1:
            while y2 <= y1:
                matrix[x1][y1] += 1
                y1 -= 1
        else:
            while y1 <= y2:
                matrix[x1][y1] += 1
                y1 += 1
    elif y1 == y2:
        if x2 <= x1:
            while x2 <= x1:
                matrix[x1][y1] += 1
                x1 -= 1
        else:
            while x1 <= x2:
                matrix[x1][y1] += 1
                x1 += 1

counter = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        if matrix[i][j] > 1:
            counter += 1
print(counter)