buckets = [0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('input.txt') as file:
    for line in file:
        numbers = line.split(',')
        for num in numbers:
            buckets[int(num)] += 1
        
        for _ in range (0, 80):
            zeros = buckets[0]
            for i in range(0, 8):
                buckets[i] = buckets[i+1]
            buckets[6] += zeros
            buckets[8] = zeros

print(sum(buckets))
