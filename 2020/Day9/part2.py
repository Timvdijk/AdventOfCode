with open("input.txt") as file:
    lines = file.readlines()

    i = 0
    while i < len(lines):
        highi = i + 1
        s = int(lines[i]) + int(lines[highi])

        while s < 393911906:
            highi = min(len(lines) - 1, highi + 1)
            s += int(lines[highi])

        if s == 393911906:
            contingent = lines[i:highi+1]
            smallest = int(min(contingent, key=lambda x: int(x)))
            largest = int(max(contingent, key=lambda x: int(x)))
            print(smallest + largest)
            break
        i += 1
