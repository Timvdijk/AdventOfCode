with open("input.txt") as file:
    initial_state = file.readline().strip()[15:]
    initial_state = [initial_state[i] for i in range(len(initial_state))]
print(initial_state)
