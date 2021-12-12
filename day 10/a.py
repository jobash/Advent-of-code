values = { ')': 3, ']': 57, '}': 1197, '>': 25137}
closingTags = { ')': '(', ']': '[', '}': '{', '>': '<' }

sum = 0
lines = [line.rstrip() for line in open('input.txt')]
openTags = []
for line in lines:
    openTags.clear()
    chars = list(line)
    for char in chars:
        if char not in values.keys():
            openTags.append(char)
        else:
            if closingTags.get(char) == openTags[-1]:
                openTags.pop(-1)
            else:
                sum += values.get(char)
                break
print(sum)