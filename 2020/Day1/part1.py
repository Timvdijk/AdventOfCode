expense_report = []
with open("input.txt") as file:
    for line in file:
        expense_report.append(int(line.strip()))

for i, e in enumerate(expense_report):
    for i2 in range(i, len(expense_report)):
        if (e + expense_report[i2]) == 2020:
            print(e * expense_report[i2])