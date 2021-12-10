with open('input.txt') as file:
    for line in file:
        numbers = line.split(',')

        lowest = 9999999999
        for i in range(0, len(numbers)):
            fuel = 0
            for j in range(0, len(numbers)):
                diff = abs(int(numbers[j]) - int(numbers[i]))
                fuel += diff * (diff + 1) / 2
            if fuel < lowest:
                lowest = fuel

        print(lowest)