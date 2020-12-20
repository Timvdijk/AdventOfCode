import queue

def findSum(q, num):
    for fi, first in enumerate(q):
        for si in range(fi + 1, len(q)):
            if (first + q[si]) == num:
                return True
    else:
        return False


with open("input.txt") as file:
    lines = file.readlines()

    i = 0
    preamble = queue.Queue()
    for line in lines:
        number = int(line.strip())
        if i < 25:
            preamble.put(number)
            i += 1
            continue

        if not findSum(preamble.queue, number):
            print(number)
            break

        preamble.get()
        preamble.put(number)
        i += 1

print(preamble.queue)
