valid_count = 0
with open("input.txt") as file:
    for line in file:
        line = line.split()
        position1, position2 = (int(x) for x in line[0].split('-'))
        required_char = line[1][0]
        password = line[2]

        if (password[position1-1] == required_char) != (password[position2-1] == required_char):
            valid_count += 1

print(valid_count)
