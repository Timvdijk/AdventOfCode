with open("input.txt") as file:
    groups = file.read().split("\n\n")

def countAnswersYes(group):
    answers = group.replace('\n', '')
    return len(set(list(answers)))

def countAnswersAllYes(group):
    answers = group.split('\n')
    verifier = set()
    for i, answer in enumerate(answers):
        if i == 0:
            verifier = set(list(answer))
            continue
        verifier &= set(list(answer))
    return len(verifier)

print(sum(countAnswersYes(group) for group in groups))
print(sum(countAnswersAllYes(group) for group in groups))