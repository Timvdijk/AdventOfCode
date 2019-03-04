with open("Day8/input.txt") as file:
    line = [int(i) for i in file.readline().strip().split(' ')]

queue = [[line[0], line[1]]]
position = 0
metadata_sum = 0

while queue:
    position += 2

    if queue[0][0]:
        queue[0][0] -= 1
        queue.insert(0, [line[position], line[position + 1]])
    else:
        metadata_count = queue.pop(0)[1]
        metadata_sum += sum(line[position:position + metadata_count])
        position += metadata_count - 2

print(metadata_sum)
