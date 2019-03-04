requirements = dict()
with open("Day7/input.txt") as file:
    for line in file:
        line = line.strip()

        try:
            requirements[line[36]].add(line[5])
        except:
            requirements[line[36]] = set(line[5])

with open("Day7/input.txt") as file:
    for line in file:
        letter = line.strip()[5]

        if letter not in requirements:
            requirements[letter] = []

requirements = sorted([[k, v] for k, v in requirements.items()], key=lambda x: x[0])

sequence = ""
while requirements:
    for i in range(len(requirements)):
        if not requirements[i][1]:
            for j in range(len(requirements)):
                if requirements[i][0] in requirements[j][1]:
                    requirements[j][1].remove(requirements[i][0])

            sequence += requirements[i][0]
            del requirements[i]
            break
print(sequence)
