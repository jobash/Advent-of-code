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

    lst = {}
    if on:
        lst.update({(x_min, x_max, y_min, y_max, z_min, z_max): 1})
    for c in cubes:
        intersection = getIntersection(x_min, x_max, y_min, y_max, z_min, z_max, c[0], c[1], c[2], c[3], c[4], c[5])
        if intersection != None:
            lst.update({(intersection[0], intersection[1], intersection[2], intersection[3], intersection[4], intersection[5]): -1 if on else 1})
    cubes.update(lst)
        
sum = 0
for c, value in cubes.items():
    sum = sum + ((c[1] + 1 - c[0])*(c[3] + 1 - c[2])*(c[5] + 1 - c[4]))*value
print(sum)