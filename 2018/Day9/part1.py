with open("input.txt") as file:
    line = file.read().strip().split(' ')

max_players, max_points = int(line[0]), int(line[-2])

circle = [0, 2, 1]
current_m_i = 1
lowest_num_m = 3
scores = dict()
current_p = 2

while True:
    if lowest_num_m == max_points:
        break

    if current_p == max_players:
        current_p = 0

    if lowest_num_m % 23 == 0:
        if current_p not in scores:
            scores[current_p] = 0

        scores[current_p] += lowest_num_m
        scores[current_p] += circle.pop(current_m_i - 7)
        current_m_i = current_m_i - 6
        current_p += 1
        lowest_num_m += 1
        continue

    if current_m_i + 2 > len(circle):
        current_m_i = 1
    else:
        current_m_i += 2

    circle.insert(current_m_i, lowest_num_m)

    lowest_num_m += 1
    current_p += 1

print(max(scores.values()))

# too high 428577
