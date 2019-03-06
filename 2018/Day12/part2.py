pot_0_i = 5
with open("input.txt") as file:
    pots = "....." + file.readline().strip()[15:] + "....."

    rules = set()
    for line in file:
        if len(line.strip()):
            rules.add((line.strip()[0:5], line.strip()[-1]))

print(pots)
previous = 0
for gen in range(1, 201):
    new_pots = pots

    for pot in range(2, len(pots)):
        plants = pots[pot - 2: pot + 3]

        for rule in rules:
            if plants == rule[0]:
                new_pots = new_pots[:pot] + rule[1] + new_pots[pot + 1:]
                break
        else:
            new_pots = new_pots[:pot] + '.' + new_pots[pot + 1:]


    for pot in range(-1, -len(rule[0]) - 1, -1):
        if new_pots[pot] == '#':
            new_pots = new_pots + "." * -(pot)
            break

    for pot in range(len(rule)):
        if new_pots[pot] == '#':
            pots = "." * pot + new_pots
            pot_0_i += pot
            break
    else:
        pots = new_pots

    s = sum(pot_i - pot_0_i if pot == '#' else 0 for pot_i, pot in enumerate(list(pots)))
    print(s, s - previous)
    if gen != 200:
        previous = s

print((50000000000 - gen) * (s - previous) + sum(pot_i - pot_0_i if pot == '#' else 0 for pot_i, pot in enumerate(list(pots))))