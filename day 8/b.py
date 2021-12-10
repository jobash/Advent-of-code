with open('input.txt') as file:
    sum = 0
    for line in file:
        sections = line.split('|')
        digits = sections[1]
        for digit in digits.split():
            if len(digit.rstrip()) in [2, 3, 4, 7]:
                sum += 1
    print(sum)