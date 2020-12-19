terrain = []
with open("input.txt") as file:
    for line in file:
        terrain.append(line.strip())


def slope(right, down):
    tree_count = 0
    x = 0
    for y in range(down, len(terrain), down):
        x = x + right
        if terrain[y][x % 31] == '#':
            tree_count += 1
    return tree_count

print(slope(3, 1))
print(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2))
