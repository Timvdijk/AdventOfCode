with open("input.txt") as file:
    line = file.readline().strip()

def react(string):
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
    return string

line = react(line)
print(min(len(react(line.replace(chr(ord('a') + i), '').replace(chr(ord('A') + i), ''))) for i in range(ord('a') - 97, ord('z') - 97)))
