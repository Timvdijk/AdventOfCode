result = 0;
with open("input.txt") as file:
    for line in file:
        mass = int(line.strip())
        fuel = int(mass / 3) - 2
        result += fuel

        while True:
            fuel = int(fuel / 3) - 2
            if fuel <= 0:
                break
            result += fuel


print(result)