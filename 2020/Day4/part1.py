passports = []
with open("input.txt") as file:
    passports = file.read().split("\n\n")
for i, passport in enumerate(passports):
    passports[i] = dict()

    passport = passport.replace('\n', ' ')
    for field in passport.split(' '):
        key, value = field.split(':')
        passports[i][key] = value

def countValid(fields):
    count = 0
    for passport in passports:
        for field in fields:
            if field not in passport.keys():
                break
        else:
            count += 1
    return count

print(countValid(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]))