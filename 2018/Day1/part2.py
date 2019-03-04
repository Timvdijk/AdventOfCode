frequency = 0
freq_list = {frequency}
stop = False

while not stop:
    with open("input.txt") as file:
        for line in file.readlines():
            frequency += int(line)
            if frequency in freq_list:
                stop = True
                break
            freq_list.add(frequency)

print(frequency)
