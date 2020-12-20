with open("input.txt") as file:
    lines = file.readlines()

accumulator = 0
i = 0
history = set()
while i < len(lines):
    instruction = lines[i]
    operation = instruction[:3]
    argument = instruction[4:]

    if (instruction, i) in history:
        print(accumulator)
        break
    history.add((instruction, i))

    if operation == "acc":
        accumulator += eval(argument)
    elif operation == "jmp":
        i += eval(argument)
        continue
    elif operation == "nop":
        pass

    i += 1