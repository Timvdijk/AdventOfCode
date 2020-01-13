result = 0;
with open("input.txt") as file:
    for line in file:
        line = line.strip();
        result += int(int(line) / 3) - 2

print(result)