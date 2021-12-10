pos = [0, 0]
with open('input.txt') as file:
    for line in file:
        dir, num = line.split()
        if dir == "forward":
            pos[0] += int(num)
        elif dir == "down":
            pos[1] += int(num)
        elif dir == "up":
            pos[1] -= int(num)

print(pos[0] * pos[1])