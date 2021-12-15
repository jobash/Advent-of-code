from collections import defaultdict, Counter
possiblePaths = defaultdict(list)
paths = []

def findPaths(visited, node):
    visited.append(node)
    nodePaths = possiblePaths.get(node)
    for nodePath in nodePaths:
        if nodePath == 'start':
            continue
        if nodePath == 'end':
            visCopy = visited.copy()
            visCopy.append(nodePath)
            paths.append(visCopy)
            continue
        continuePath = True
        if nodePath.islower():
            c = Counter(visited)
            nodeCount = c.get(nodePath, 0)
            for key, value in c.items():
                if nodeCount > 0 and key.islower() and value > 1:
                    continuePath = False
        if continuePath:
            findPaths(visited.copy(), nodePath)

lines = [line.rstrip() for line in open('input.txt')]
for line in lines:
    parts = line.split('-')

    possiblePaths[parts[0]].append(parts[1])
    possiblePaths[parts[1]].append(parts[0])

findPaths([], 'start')
print(len(paths))
#print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in paths]))