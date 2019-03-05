serial_num = 3628

grid = [[int(str((y * (x + 10) + serial_num) * (x + 10))[-3]) - 5 if len(str((y * (x + 10) + serial_num) * (x + 10))) >= 3 else 0 for y in range(1, 301)] for x in range(1, 301)]


total_power = [[sum(grid[x + s_x][y + s_y] for s_y in range(3) for s_x in range(3)) for y in range(0, 298)] for x in range(0, 298)]
max_x = total_power.index(max(total_power, key=lambda x: max(x)))
max_y = total_power[max_x].index(max(total_power[max_x]))

print(max_x + 1, max_y + 1, total_power[max_x][max_y])
