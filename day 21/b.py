lines = [line.rstrip() for line in open('input.txt')]

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

p1_pos = int(lines[0].split()[-1])
p2_pos = int(lines[1].split()[-1])

p1_score = 0
p2_score = 0

seen_results = {}

def calcAns(p1_pos, p2_pos, p1_score, p2_score):
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)
    if (p1_pos, p2_pos, p1_score, p2_score) in seen_results:
        return seen_results[(p1_pos, p2_pos, p1_score, p2_score)]
    res = (0, 0)
    for die1 in range(1,4):
        for die2 in range(1,4):
            for die3 in range(1,4):
                pos = positions[((p1_pos + die1 + die2 + die3) % 10) - 1]
                score = p1_score + pos

                p1_wins, p2_wins = calcAns(p2_pos, pos, p2_score, score)
                res = (res[0]+p2_wins, res[1]+p1_wins)
    seen_results[(p1_pos, p2_pos, p1_score, p2_score)] = res
    return res

print(max(calcAns(p1_pos, p2_pos, p1_score, p2_score)))
