valid_count = 0
with open("input.txt") as file:
    for line in file:
        line = line.split()
        min_occurance, max_occurance = (int(x) for x in line[0].split('-'))
        required_char = line[1][0]
        password = line[2]

        occurance = password.count(required_char)

        if occurance >= min_occurance and occurance <= max_occurance:
            valid_count += 1
print(valid_count)