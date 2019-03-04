import time

t = time.time()
two = 0
three = 0
with open("input.txt") as file:
    for line in file.readlines():
        chars = dict()
        for char in line:
            try:
                chars[char] += 1
            except:
                chars[char] = 1

        for k, v in chars.items():
            if v == 2:
                two += 1
                break

        for k, v in chars.items():
            if v == 3:
                three += 1
                break
print(two*three)
print(time.time() - t)