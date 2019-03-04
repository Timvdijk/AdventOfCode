
with open("input.txt") as file:
    chronological = sorted(file, key=lambda s: s[6:17])

timetable = dict()
start_t = None
for line in chronological:
    line = line.strip().split(' ')
    minutes = 0
    if line[2] == "Guard":
        guard_id = int(line[3][1:])
    elif line[2] == "falls":
        start_t = line[1][3:5] if line[1][:2] != "23" else "00"
    elif line[2] == "wakes":
        if guard_id not in timetable:
            timetable[guard_id] = [[0 for i in range(10)] for i in range(6)]
            timetable[guard_id].insert(0, int(line[1][3:5]) - int(start_t))
        else:
            timetable[guard_id][0] += int(line[1][3:5]) - int(start_t)

        for i in range(int(start_t), int(line[1][3:5])):
            timetable[guard_id][int(str(i)[0]) + 1 if i > 10 else 1][(int(str(i)[1]) % 10) if i > 9 else int(str(i)[0])] += 1

most_id = max(timetable, key=lambda x: timetable[x][0])
amount_min = max([max(ten) for ten in timetable[most_id][1:]])
for i, ten in enumerate(timetable[most_id][1:]):
    try:
        minute = i * 10 + ten.index(amount_min)
        break
    except:
        pass

print(len(timetable))
print(most_id, minute,most_id * minute)
