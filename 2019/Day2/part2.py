with open("input.txt") as file:
    init_program = [int(x) for x in file.readline().split(',')]

def Intcode(program):
    index = 0

    while program[index] != 99:
        code = program[index:index+4]

        if code[0] == 1:
            program[code[3]] = program[code[1]] + program[code[2]]
        elif code[0] == 2:
            program[code[3]] = program[code[1]] * program[code[2]]
        else:
            print("something went wrong!")
            exit()

        index += 4

    return program

for noun in range(1, 99):
    for verb in range(1, 99):
        p = init_program.copy()
        p[1] = noun
        p[2] = verb

        if Intcode(p)[0] == 19690720:
            print(100 * noun + verb)
            break