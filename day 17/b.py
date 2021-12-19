line = [line.rstrip() for line in open('input.txt')][0]

parts = line.split()
min_x = int(parts[2].split('..')[0][2:])
max_x = int(parts[2].split('..')[1][:-1])
min_y = int(parts[3].split('..')[0][2:])
max_y = int(parts[3].split('..')[1])


count = 0
for i in range(max_x + 1):
    for j in range(min_y - 1, 500):
        x = 0
        y = 0
        dx = i
        dy = j
        for step in range(1000):
            x += dx
            y += dy
            if dx > 0:
                dx -= 1
            dy -= 1
            if min_x <= x <= max_x and min_y <= y <= max_y:
                count += 1
                break
print(count)