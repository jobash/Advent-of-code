import math
import sys
sys.setrecursionlimit(10000)

matrix = []
lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    matrix.append([int(char) for char in list(line)])

costMatrix = [[math.inf]*len(matrix) * 5 for _ in range(len(matrix[0]) * 5)]

def calculateCosts(x, y, currentCost):
    normalized_x = x % len(matrix)
    normalized_y = y % len(matrix[0])
    if x < len(costMatrix) - 1:
        x_mult = math.floor((x + 1) / len(matrix))
        y_mult = math.floor(y / len(matrix[0]))
        numberToAdd = 1 * (x_mult + y_mult)
        matrixVal = (matrix[(normalized_x + 1) % len(matrix)][normalized_y] + numberToAdd)
        if matrixVal > len(matrix):
            matrixVal -= len(matrix)
        if currentCost + matrixVal < costMatrix[x + 1][y]:
            costMatrix[x + 1][y] = currentCost + matrixVal
            calculateCosts(x + 1, y, currentCost + matrixVal)
    if y < len(costMatrix[0]) - 1:
        x_mult = math.floor(x / len(matrix))
        y_mult = math.floor((y + 1) / len(matrix[0]))
        numberToAdd = 1 * (x_mult + y_mult)
        matrixVal = (matrix[normalized_x][(normalized_y + 1) % len(matrix[0])] + numberToAdd)
        if matrixVal > len(matrix[0]):
            matrixVal -= len(matrix[0])
        if currentCost + matrixVal < costMatrix[x][y + 1]:
            costMatrix[x][y + 1] = currentCost + matrixVal
            calculateCosts(x, y + 1, currentCost + matrixVal)

currentCost = 0
start_x = 0
start_y = 0
costMatrix[start_x][start_y] = 0
calculateCosts(start_x, start_y, currentCost)
goal_x = len(costMatrix) - 1
goal_y = len(costMatrix[0]) - 1
#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in costMatrix]))
print(costMatrix[goal_x][goal_y])
