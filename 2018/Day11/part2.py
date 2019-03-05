serial_num = 3628

grid = [[int(str((y * (x + 10) + serial_num) * (x + 10))[-3]) - 5 if len(str((y * (x + 10) + serial_num) * (x + 10))) >= 3 else 0 for y in range(1, 301)] for x in range(1, 301)]

max_powers = []
for size in range(1, 15):
    total_power = [[sum(grid[x + s_x][y + s_y] for s_y in range(size) for s_x in range(size)) for y in range(0, 300 - (size - 1))] for x in range(0, 300 - (size - 1))]
    max_x = total_power.index(max(total_power, key=lambda x: max(x)))
    max_y = total_power[max_x].index(max(total_power[max_x]))

    max_powers.append((max_x, max_y, size, total_power[max_x][max_y]))
    print(size)

max_p = max(max_powers, key=lambda p: p[-1])

print(max_p[0] + 1, max_p[1] + 1, max_p[2:])
