import ast

lines = [line.rstrip() for line in open('input.txt')]

result = ast.literal_eval(lines[0])

def explode(array):
    if len(array) < 2:
        return False
    if type(array[0]) == list:
        print('is list', array[0])
    return False

def split(array):
    return False

for line in lines[1:]:
    new_array = [result, ast.literal_eval(line)]
    while True:
        if explode(new_array):
            continue
        if split(new_array):
            continue
        break
    result = new_array
    print(new_array)
    break

