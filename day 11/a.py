matrix = []
lines = [line.rstrip() for line in open('input.txt')]
flashes = 0
for line in lines:
    row = list(map(int, line))
    matrix.append(row)

flashed = []

def flash(row, col):
    if (row, col) in flashed:
        return
    flashed.append((row, col))
    if row > 0:
        if matrix[row - 1][col] < 10:
            matrix[row - 1][col] += 1
            if matrix[row - 1][col] > 9:
                flash(row - 1, col)
        if col > 0:
            if matrix[row - 1][col - 1] < 10:
                matrix[row - 1][col - 1] += 1
                if matrix[row - 1][col - 1] > 9:
                    flash(row - 1, col - 1)
        if col < len(matrix[row]) - 1:
            if matrix[row - 1][col + 1] < 10:
                matrix[row - 1][col + 1] += 1
                if matrix[row - 1][col + 1] > 9:
                    flash(row - 1, col + 1)
    if row < len(matrix) - 1:
        if matrix[row + 1][col] < 10:
            matrix[row + 1][col] += 1
            if matrix[row + 1][col]  > 9:
                flash(row + 1, col)
        if col > 0:
            if matrix[row + 1][col - 1] < 10:
                matrix[row + 1][col - 1] += 1
                if matrix[row + 1][col - 1] > 9:
                    flash(row + 1, col - 1)
        if col < len(matrix[row]) - 1:
            if matrix[row + 1][col + 1] < 10:
                matrix[row + 1][col + 1] += 1
                if matrix[row + 1][col + 1] > 9:
                    flash(row + 1, col + 1)
    if col > 0:
        if matrix[row][col - 1] < 10:
            matrix[row][col - 1] += 1
            if matrix[row][col - 1] > 9:
                flash(row, col - 1)
    if col < len(matrix[0]) - 1:
        if matrix[row][col + 1] < 10:
            matrix[row][col + 1] += 1
            if matrix[row][col + 1] > 9:
                flash(row, col + 1)


for step in range(0, 100):
    flashed.clear()
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            matrix[row][col] += 1

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] > 9:
                flash(row, col)

    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if matrix[row][col] > 9:
                flashes += 1
                matrix[row][col] = 0
print(flashes)