
top = 1
topRight = 2
bottomRight = 4
bottom = 8
bottomLeft = 16
topLeft = 32
middle = 64

values = { 63:0, 6:1, 91:2, 79:3, 102:4, 109:5, 125:6, 7:7, 127:8, 111:9 }
segments = { }
zero = one = two = three = four = five = six = seven = eight = nine = ""

def setKnown(line: str):
    parts = line.split()
    global one, four, seven, eight
    for part in parts:
        if len(part) == 2:
            one = part
        elif len(part) == 3:
            seven = part
        elif len(part) == 4:
            four = part
        elif len(part) == 7:
            eight = part

def getTop():
    chars = list(one)
    for ch in list(seven):
        if ch not in chars:
            segments.update({ch: top})
            break

def getRightSide(line: str):
    parts = line.split()
    global six
    for part in parts:
        if len(part) == 6:
            ch = list(one)
            chars = list(part)
            if ch[0] not in chars and ch[1] in chars:
                six = part
                segments.update({ch[0]: topRight, ch[1]: bottomRight})
                break
            elif ch[0] in chars and ch[1] not in chars:
                six = part
                segments.update({ch[1]: topRight, ch[0]: bottomRight})
                break

def getBottom(line: str):
    parts = line.split()
    global four, six, nine
    for part in parts:
        if len(part) == 6 and part != six:
            chars = set(part)
            ch = set(four)
            if ch.issubset(chars):
                nine = part
                for char in chars:
                    if char not in segments and char not in ch:
                        segments.update({char: bottom})
    
def getMiddle(line: str):
    parts = line.split()
    global nine, three, one
    for part in parts:
        if len(part) == 5:
            chars = set(part)
            ch = set(nine)
            if chars.issubset(ch) and chars.issuperset(set(one)):
                three = part
                for char in chars:
                    if char not in segments:
                        segments.update({char: middle})
                        break

def getRight(line: str):
    parts = line.split()
    global eight, nine
    for part in parts:
        if len(part) == 5 and part != three:
            chars = set(part)
            ch = set(nine)
            if chars.issubset(ch):
                for char in chars:
                    if char not in segments:
                        segments.update({char: topLeft})
                        break
    for char in set(eight):
        if char not in segments:
            segments.update({char: bottomLeft})

with open('input.txt') as file:
    sum = 0
    for line in file:
        zero = one = two = three = four = five = six = seven = eight = nine = ""
        sections = line.split('|')
        setKnown(sections[0])
        getTop()
        getRightSide(sections[0])
        getBottom(sections[0])
        getMiddle(sections[0])
        getRight(sections[0])
        digits = sections[1]
        code = 0
        multiplier = 1000
        for digit in digits.split():
            segmentSum = 0
            for number in list(digit):
                segmentSum += segments[number]
            code = code + (multiplier * values[segmentSum])
            multiplier = multiplier / 10
        sum += code
        segments.clear()

    print(sum)