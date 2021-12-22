lines = [line.rstrip() for line in open('input.txt')]

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