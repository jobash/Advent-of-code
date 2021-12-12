import math

values = { ')': 1, ']': 2, '}': 3, '>': 4}
closingTags = { ')': '(', ']': '[', '}': '{', '>': '<' }

sums = []
lines = [line.rstrip() for line in open('input.txt')]
openTags = []
for line in lines:
    lineSum = 0
    openTags.clear()
    chars = list(line)
    for char in chars:
        if char not in values.keys():
            openTags.append(char)
        else:
            if closingTags.get(char) == openTags[-1]:
                openTags.pop(-1)
            else:
                openTags.clear()
                break
    while len(openTags) > 0:
        tag = openTags.pop(-1)
        for key, value in closingTags.items():
            if value == tag:
                lineSum = lineSum * 5 + values.get(key)
    if lineSum > 0:
        sums.append(lineSum)

sums = sorted(sums)
print(sums[math.floor(len(sums) / 2)])