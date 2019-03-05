from collections import deque
with open("input.txt") as file:
    line = file.read().strip().split(' ')

max_players, max_points = int(line[0]), int(line[-2] * 100)

marbles = deque([0])
current = 0
player = 0
scores = dict()

for marble in range(1, max_points + 1):
    if player == max_players:
        player = 0

    if marble % 23 == 0:
        if player not in scores:
            scores[player] = 0

        scores[player] += marble
        marbles.rotate(-7)
        scores[player] += marbles.pop()
    else:
        marbles.rotate(2)
        marbles.append(marble)

    player += 1

print(max(scores.values()))