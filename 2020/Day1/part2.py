expense_report = []
with open("input.txt") as file:
    for line in file:
        expense_report.append(int(line.strip()))

for i, e in enumerate(expense_report):
    for i2 in range(i, len(expense_report)):
        e2 = expense_report[i2]
        for i3 in range(i2, len(expense_report)):
            if (e + e2 + expense_report[i3]) == 2020:
                print(e * e2 * expense_report[i3])