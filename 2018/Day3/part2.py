import re

fabric = [[0 for i in range(1500)] for i in range(1500)]

with open("Day3/input.txt") as file:
    for line in file:
        line = re.split(": | @ |,|x| ", line.strip('#').strip())
        for x in range(int(line[1]), int(line[1]) + int(line[3])):
            for y in range(int(line[2]), int(line[2]) + int(line[4])):
                fabric[x][y] = int(line[0]) if fabric[x][y] == 0 else-1

with open("Day3/input.txt") as file:
    for line in file:
        line = re.split(": | @ |,|x| ", line.strip('#').strip())
        for x in range(int(line[1]), int(line[1]) + int(line[3])):
            if -1 in fabric[x][int(line[2]):int(line[2]) + int(line[4])]:
                break
        else:
            print(line[0])
            break
