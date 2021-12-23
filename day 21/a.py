lines = [line.rstrip() for line in open('input.txt')]

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

p1_pos = int(lines[0].split()[-1])
p2_pos = int(lines[1].split()[-1])

p1_score = 0
p2_score = 0

counter = 1
player_one = True
roll_count = 0
while p1_score < 1000 and p2_score < 1000:
    for _ in range(3):
        if counter > 100:
            counter = 1
        if player_one:
            p1_pos += counter
        else:
            p2_pos += counter
        counter += 1
        roll_count += 1
    if player_one:
        p1_pos = positions[(p1_pos % 10) - 1]
        p1_score += p1_pos
    else:
        p2_pos = positions[(p2_pos % 10) - 1]
        p2_score += p2_pos
    player_one = not player_one
    
print(roll_count * (p1_score if player_one else p2_score))