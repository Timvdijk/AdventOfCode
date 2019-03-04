with open("Day8/input.txt") as file:
    line = [int(i) for i in file.readline().strip().split(' ')]

queue = [[line[0], line[1]]]
position = 0