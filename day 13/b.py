matrix = [[' ']*1311 for _ in range(895)]

def foldMatrix(axis, pos):
    global matrix
    if axis == 'x':
        for i in range(0, len(matrix)):
            for j in range(0, pos):
                matrix[i][j] = '#' if matrix[i][j] == '#' or matrix[i][- j - 1] == '#' else ' '
            matrix[i] = matrix[i][0:pos]
    else:
        for i in range(0, pos):
            for j in range(0, len(matrix[0])):
                matrix[i][j] = '#' if matrix[i][j] == '#' or matrix[-i - 1][j] == '#' else ' '
        matrix = matrix[0:pos]

lines = [line.rstrip() for line in open('input.txt')]
folds = False
for line in lines:
    if len(line) == 0:
        folds = True
        continue
    if not folds:
        parts = line.split(',')
        col = int(parts[0])
        row = int(parts[1])
        matrix[row][col] = '#'
    if folds:
        parts = line.split()
        dir = parts[2].split('=')
        foldMatrix(dir[0], int(dir[1]))

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

