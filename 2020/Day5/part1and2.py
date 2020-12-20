with open("input.txt") as file:
    passes = file.readlines()

import math

def seat(bpass):
    ret = dict()
    lower = 0
    upper = 127
    for i in range(7):
        c = bpass[i]
        if c == 'F':
            upper = math.floor((lower + upper) / 2)
        if c == 'B':
            lower = math.ceil((lower + upper) / 2)
    ret["row"] = lower

    lower = 0
    upper = 7
    for i in range(3):
        c = bpass[i + 7]
        if c == 'L':
            upper = math.floor((lower + upper) / 2)
        if c == 'R':
            lower = math.ceil((lower + upper) / 2)
    ret["col"] = lower

    return ret

highest = 0
seats = []
ids = []
for bpass in passes:
    s = seat(bpass)
    seats.append(s)
    id = (s["row"] * 8 + s["col"])
    ids.append(id)
    if id > highest:
        highest = id

ids.sort()
print(sorted(set(range(ids[0], ids[-1])) - set(ids)))
print(highest)