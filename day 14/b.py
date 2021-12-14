lines = [line.rstrip() for line in open('input.txt')]
insertRules = {}
textChars = list(lines[0])
for line in lines[2:]:
    parts = line.split()
    insertRules.update({parts[0]: parts[2]})
charCounts = {}
for char in textChars:
    charCounts[char] = charCounts.get(char, 0) + 1
pairs = {}
for i in range(0, len(textChars) - 1):
    pairs.update({(textChars[i] + textChars[i+1]): 1})

for _ in range(0, 40):
    newPairs = {}
    for pair, count in pairs.items():
        rule = insertRules.get(pair)
        chars = list(pair)
        newPairs[(chars[0] + rule)] = newPairs.get((chars[0] + rule), 0) + count
        newPairs[(rule + chars[1])] = newPairs.get((rule + chars[1]), 0) + count
        
        charCounts[rule] = charCounts.get(rule, 0) + count
    pairs = newPairs


sortedValues = sorted(charCounts.values(), reverse=True)
print(sortedValues[0] - sortedValues[-1])
