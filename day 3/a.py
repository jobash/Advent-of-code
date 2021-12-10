ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
with open('input.txt') as file:
    for line in file:
        lst = list(line)
        x = range(0, len(lst))
        for i in x:
            if lst[i] == "1":
                ones[i] += 1
            elif lst[i] == "0":
                zeros[i] += 1

gamma = ""
epsilon = ""
for i in range(0, len(ones)):
    if ones[i] > zeros[i]:
        gamma += "1"
        epsilon += "0"
    else:
        epsilon += "1"
        gamma += "0"

print(int(gamma, 2) * int(epsilon, 2))