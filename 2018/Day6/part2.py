with open("input.txt") as file:
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

region_count = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        count = 0
        for point in points:
            count += abs(x - int(point[0])) + abs(y - int(point[1]))
        if count < 10000:
            region_count += 1
print(region_count)
