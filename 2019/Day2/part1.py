with open("input.txt") as file:
    program = [int(x) for x in file.readline().split(',')]
    program[1] = 12
    program[2] = 2

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

print(program[0])