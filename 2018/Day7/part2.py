requirements = dict()
with open("input.txt") as file:
    for line in file:
        line = line.strip()

        try:
            requirements[line[36]].add(line[5])
        except:
            requirements[line[36]] = set(line[5])

with open("input.txt") as file:
    for line in file:
        letter = line.strip()[5]

        if letter not in requirements:
            requirements[letter] = []

requirements = sorted([[k, v] for k, v in requirements.items()], key=lambda x: x[0])
working = dict()
count = 0
while requirements:
    if len(working) <= 5:
        for i in range(len(requirements)):
            if not requirements[i][1] and requirements[i][0] not in working:
                working[requirements[i][0]] = ord(requirements[i][0]) - 4

    for letter in set(working):
        working[letter] -= 1

        if working[letter] == 0:
            for i in range(len(requirements)):
                if requirements[i][0] == letter:
                    delete = i
                if letter in requirements[i][1]:
                    requirements[i][1].remove(letter)

            working.pop(letter)
            del requirements[delete]

    count += 1
print(count)
