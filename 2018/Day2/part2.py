
with open("input.txt") as file:
    lines = file.readlines()
    for i, line in enumerate(lines):
        for other in lines[i + 1:]:
            for j, char in enumerate(line):
                if line[:j] + line[j + 1:] == other[:j] + other[j + 1:]:
                    print(line[:j] + line[j + 1:])
