
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
        try:
            timetable[guard_id][0] += int(line[1][3:5]) - int(start_t)

            for i in range(int(start_t), int(line[1][3:5])):
                timetable[guard_id][int(str(i)[0]) + 1 if i > 10 else 1][(int(str(i)[1]) % 10) if i > 9 else int(str(i)[0])] += 1
        except KeyError:
            timetable[guard_id] = [[0 for i in range(10)] for i in range(6)]
            timetable[guard_id].insert(0, int(line[1][3:5]) - int(start_t))

            for i in range(int(start_t), int(line[1][3:5])):
                timetable[guard_id][int(str(i)[0]) + 1 if i > 10 else 1][(int(str(i)[1]) % 10) if i > 9 else int(str(i)[0])] += 1


max_pair = max(([max([max(ten) for ten in timetable[k][1:]]), k] for k in timetable), key=lambda x: x[0])

for i, ten in enumerate(timetable[max_pair[1]][1:]):
    try:
        minute = i * 10 + ten.index(max_pair[0])
        break
    except:
        pass

print(max_pair, minute, max_pair[1] * minute)