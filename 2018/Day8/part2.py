with open("input.txt") as file:
    line = iter(map(int, file.readline().strip().split(' ')))

def read_tree():
    next_child, next_metadata = next(line), next(line)
    children, metadata = [], []

    for i in range(next_child):
        children.append(read_tree())
    for i in range(next_metadata):
        metadata.append(next(line))

    return (children, metadata)

def value(node):
    if not node[0]:
        return sum(node[1])
    else:
        count = 0

        for m in node[1]:
            if 1 <= m <= len(node[0]):
                count += value(node[0][m - 1])

        return count


print(value(read_tree()))