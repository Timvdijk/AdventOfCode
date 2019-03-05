with open("input.txt") as file:
    lines = [(int(line[10:16]), int(line[18:24]), int(line[36:38]), int(line[40:42])) for line in file]

previous = None
t = 0
while True:
    t += 1
    min_x = min(x + t *  vel_x for (x, y, vel_x, vel_y) in lines)
    max_x = max(x + t *  vel_x for (x, y, vel_x, vel_y) in lines)
    min_y = min(y + t *  vel_y for (x, y, vel_x, vel_y) in lines)
    max_y = max(y + t *  vel_y for (x, y, vel_x, vel_y) in lines)

    size = (max_x - min_x) * (max_y - min_y)
    if previous and previous < size:
        t -= 1
        break

    previous = size

print(t, previous)
grid = [[' '] * 200 for j in range(25)]
for (x, y, vel_x, vel_y) in lines:
    grid[y + t  * vel_y - 185][x + t * vel_x - 300] = '#'

for g in grid:
    print(''.join(g))