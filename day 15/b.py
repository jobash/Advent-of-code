import math
import heapq

matrix = []
lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    matrix.append([int(char) for char in list(line)])

x_length = len(matrix)
y_length = len(matrix[0])
dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]

def dijkstra(tiles):
    D = [[math.inf for _ in range(tiles*y_length)] for _ in range(tiles*x_length)]
    queue = [(0, 0, 0)]

    while queue:
        (dist, row, col) = heapq.heappop(queue)
        if row < 0 or row >= tiles*x_length or col < 0 or col >= tiles*y_length:
            continue

        value = matrix[row % x_length][col % y_length] + (row//x_length) + (col//y_length)
        while value > 9:
            value -= 9

        cost = dist + value
        if D[row][col] == math.inf or cost < D[row][col]:
            D[row][col] = cost
        else:
            continue
        
        if row == tiles * x_length - 1 and col == tiles * y_length - 1:
            break
        for dir in range(4):
            neighbor_x = row + dir_x[dir]
            neighbor_y = col + dir_y[dir]
            heapq.heappush(queue, (cost, neighbor_x, neighbor_y))


    return D[tiles*x_length-1][tiles*y_length-1] - matrix[0][0]

print(dijkstra(5))
