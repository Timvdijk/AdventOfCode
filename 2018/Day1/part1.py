frequency = 0
with open("Day1/input.txt") as file:
    for line in file:
        frequency += int(line)

print(frequency)