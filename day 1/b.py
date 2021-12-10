counter = 0
prevSum = 9999
with open('input.txt') as file:
    lines = file.readlines()
    x = range(0, len(lines) - 2)
    for i in x:
        curr = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if curr > prevSum:
            counter += 1
        prevSum = curr

print(counter)