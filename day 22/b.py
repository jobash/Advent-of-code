lines = [line.rstrip() for line in open('input.txt')]


def getIntersection(x1, x2, y1, y2, z1, z2, a1, a2, b1, b2, c1, c2):
    if x1 > a2 or x2 < a1 or y1 > b2 or y2 < b1 or z1 > c2 or z2 < c1:
        return None

    return (max(x1, a1), min(x2, a2), max(y1, b1), min(y2, b2), max(z1, c1), min(z2, c2))

cubes = {}
for line in lines:
    parts = line.split()
    on = parts[0] == "on"
    vars = parts[1].split(',')
    x_min = int(vars[0].split('..')[0][2:])
    x_max = int(vars[0].split('..')[1])
    y_min = int(vars[1].split('..')[0][2:])
    y_max = int(vars[1].split('..')[1])
    z_min = int(vars[2].split('..')[0][2:])
    z_max = int(vars[2].split('..')[1])

    if x_min < -50 or y_min < -50 or z_min < -50 or x_min > 50 or y_min > 50 or z_min > 50:
        continue
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            for k in range(z_min, z_max + 1):
                if on:
                    cubes.update({(i,j,k): 1})
                else:
                    try:
                        del cubes[(i,j,k)]
                    except:
                        pass

print(len(cubes))