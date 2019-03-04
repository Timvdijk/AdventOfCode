with open("Day5/input.txt") as file:
    string = file.readline().strip()

changes = True
while changes:
    changes = 0
    for i in range(len(string)):
        try:
            if ord(string[i]) - ord(string[i + 1]) == 32 or ord(string[i + 1]) - ord(string[i]) == 32:
                string = string[:i] + string[i + 2:]
                changes += 1
        except IndexError:
            break

print(len(string), string)