from collections import defaultdict
possiblePaths = defaultdict(list)
paths = []

def findPaths(visited, node):
    visited.append(node)
    nodePaths = possiblePaths.get(node)
    for nodePath in nodePaths:
        if nodePath == 'end':
            visited.append(nodePath)
            paths.append(visited)
        if nodePath not in visited or nodePath.isupper():
            findPaths(visited.copy(), nodePath)

lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    parts = line.split('-')

    possiblePaths[parts[0]].append(parts[1])
    possiblePaths[parts[1]].append(parts[0])

findPaths([], 'start')
print(len(paths))
#print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in paths]))