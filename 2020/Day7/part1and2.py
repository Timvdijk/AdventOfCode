rules = dict()
with open("input.txt") as file:
    for line in file:
        rule = line.replace(" bags contain ", '#').replace(" bag, ", '#').replace(" bags, ", '#').replace(" bag.", '').replace(" bags.", '').strip().split('#')
        rules[rule[0]] = dict()
        for i in range(1, len(rule)):
            part = rule[i]
            if part == "no other":
                continue
            rules[rule[0]][part[2:]] = int(part[:1])

def recursiveContains(bag):
    if "shiny gold" in rules[bag].keys():
        return True
    ret = set()
    for b in rules[bag].keys():
        ret.add(recursiveContains(b))
    return True in ret

count = 0
for bag in rules.keys():
    if bag != "shiny gold":
        count += recursiveContains(bag)
print(count)

def recursiveCount(bag):
    count = 0
    for key, value in rules[bag].items():
        count += recursiveCount(key) * value + value
    return count

print(recursiveCount("shiny gold"))
