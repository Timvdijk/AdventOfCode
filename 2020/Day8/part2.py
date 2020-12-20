with open("input.txt") as file:
    lines = file.readlines()


def terminates(l):
    accumulator = 0
    i = 0
    history = set()
    while i < len(l):
        instruction = l[i]
        operation = instruction[:3]
        argument = instruction[4:]

        if (instruction, i) in history:
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
    else:
        print("completed", accumulator)
        return True
    return False

for i in range(len(lines)):
    c = lines.copy()
    inst = c[i]
    o = inst[:3]
    a = inst[3:]

    if o == "jmp":
        c[i] = "nop" + a
    elif o == "nop":
        c[i] = "jmp" + a
    else:
        continue

    if terminates(c):
        print("above answer terminates")
        break
