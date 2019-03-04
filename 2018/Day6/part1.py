with open("Day6/input.txt") as file:
    points = []
    x = set()
    y = set()
    for line in file:
        line = line.strip().split(", ")
        points.append(line)
        x.add(int(line[0]))
        y.add(int(line[1]))

# set grid according to highest x and highest y
grid = [['.' for i in range(max(y))] for i in range(max(x))]

# add the points to the grid
for i, line in enumerate(points):
    grid[int(line[0]) - 1][int(line[1]) - 1] = i

# determine closest distance to another point for each point
for x in range(len(grid)):
    for y in range(len(grid[x])):
        sort = sorted([((abs(x - int(point[0]))) + abs(y - int(point[1])), point)
                       for point in points], key=lambda x: x[0])
        grid[x][y] = grid[int(sort[0][1][0]) - 1][int(sort[0]
                                                      [1][1]) - 1] if sort[0][0] != sort[1][0] else '.'

# determine infinite area's (numbers on the edge of the grid)
infinite = set()
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if x == 0 or x == len(grid) - 1 or y == 0 or y == len(grid[x]) - 1:
            infinite.add(grid[x][y])

# count all non infinte area's
d = dict()
for x in range(len(grid)):
    for y in range(len(grid[x])):
        try:
            if grid[x][y] not in infinite:
                d[grid[x][y]] += 1
        except:
            d[grid[x][y]] = 1

print(max(d.values()))
