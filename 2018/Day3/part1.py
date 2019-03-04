import re

fabric = [[0 for i in range(1500)] for i in range(1500)]

with open("input.txt") as file:
    for line in file:
        line = re.split(": | @ |,|x| ", line.strip('#').strip())
        for x in range(int(line[1]), int(line[1]) + int(line[3])):
            for y in range(int(line[2]), int(line[2]) + int(line[4])):
                fabric[x][y] = line[0] if fabric[x][y] == 0 else-1

count = 0
for x in range(len(fabric)):
    for y in range(len(fabric[x])):
        count += 1 if fabric[x][y] == -1 else 0
print(count)
