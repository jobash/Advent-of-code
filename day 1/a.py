counter = 0
lastVal = 9999
with open('input.txt') as file:
    for line in file:
        if int(line) > lastVal:
            counter += 1
        lastVal = int(line)

print(counter)