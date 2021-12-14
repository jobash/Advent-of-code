lines = [line.rstrip() for line in open('input.txt')]
textChars = list(lines[0])

for _ in range(0, 10):
    pairs = []
    for i in range(0, len(textChars) - 1):
        pairs.append((textChars[i] + textChars[i+1], i))
    textChars.clear()
    for pair, index in pairs:
        for line in lines[2:]:
            parts = line.split()
            if pair == parts[0]:
                chars = list(pair)
                if len(textChars) == 0:
                    textChars.append(chars[0])
                textChars.extend([parts[2], chars[1]])
                break

charCounts = {}
for char in textChars:
    charCount = charCounts.get(char)
    if charCount == None:
        charCounts.update({char: 1})
    else:
        charCounts.update({char: charCount + 1})
print(charCounts)
sortedValues = sorted(charCounts.values(), reverse=True)
print(sortedValues[0] - sortedValues[-1])
