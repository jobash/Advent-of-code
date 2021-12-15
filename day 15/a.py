import math

matrix = []
lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    matrix.append([int(char) for char in list(line)])

costMatrix = [[math.inf]*len(matrix) for _ in range(len(matrix[0]))]

def calculateCosts(x, y, currentCost):
    if x < len(matrix) - 1:
        if currentCost + matrix[x + 1][y] < costMatrix[x + 1][y]:
            costMatrix[x + 1][y] = currentCost + matrix[x + 1][y]
            calculateCosts(x + 1, y, currentCost + matrix[x + 1][y])
    if y < len(matrix[0]) - 1:
        if currentCost + matrix[x][y + 1] < costMatrix[x][y + 1]:
            costMatrix[x][y + 1] = currentCost + matrix[x][y + 1]
            calculateCosts(x, y + 1, currentCost + matrix[x][y + 1])

currentCost = 0
start_x = 0
start_y = 0
costMatrix[start_x][start_y] = 0
calculateCosts(start_x, start_y, currentCost)
goal_x = len(matrix) - 1
goal_y = len(matrix[0]) - 1
print(costMatrix[goal_x][goal_y])
