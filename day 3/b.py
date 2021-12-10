ones = []
zeros = []
oxygenValue = ""
co2Value = ""
with open('input.txt') as file:
    lines = file.readlines()
    oxygen = lines
    co2 = lines
    for i in range(0, 13):
        if len(oxygen) == 1:
            oxygenValue = oxygen[0]
            break
        for line in oxygen:
            lst = list(line)
            if lst[i] == "1":
                ones.append(line)
            else:
                zeros.append(line)
        if len(ones) >= len(zeros):
            oxygen = ones
        else:
            oxygen = zeros
        ones = []
        zeros = []
    for i in range(0, 13):
        if len(co2) == 1:
            co2Value = co2[0]
            break
        for line in co2:
            lst = list(line)
            if lst[i] == "1":
                ones.append(line)
            else:
                zeros.append(line)
        if len(ones) < len(zeros):
            co2 = ones
        else:
            co2 = zeros
        ones = []
        zeros = []

print("oxy: " + oxygenValue)
print("co2: " + co2Value)
print(int(oxygenValue, 2) * int(co2Value, 2))
    