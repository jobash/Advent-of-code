line = [line.rstrip() for line in open('input.txt')][0]

parts = line.split()
min_x = int(parts[2].split('..')[0][2:])
max_x = int(parts[2].split('..')[1][:-1])
min_y = int(parts[3].split('..')[0][2:])
max_y = int(parts[3].split('..')[1])

v_max = abs(min_y)
h_max = (v_max-1)*v_max/2
print(h_max)
