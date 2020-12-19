passports = []
with open("input.txt") as file:
    passports = file.read().split("\n\n")
for i, passport in enumerate(passports):
    passports[i] = dict()

    passport = passport.replace('\n', ' ')
    for field in passport.split(' '):
        key, value = field.split(':')
        passports[i][key] = value

def arePresent(fields, passport):
    for field in fields:
        if field not in passport.keys():
            break
    else:
        return True
    return False

import re

def countValid():
    count = 0
    for passport in passports:
        if not arePresent(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], passport):
            continue
        if not len(passport["byr"]) == 4 or not int(passport["byr"]) >= 1920 or not int(passport["byr"]) <= 2002:
            continue
        if not len(passport["iyr"]) == 4 or not int(passport["iyr"]) >= 2010 or not int(passport["iyr"]) <= 2020:
            continue
        if not len(passport["eyr"]) == 4 or not int(passport["eyr"]) >= 2020 or not int(passport["eyr"]) <= 2030:
            continue

        if passport["hgt"][-2:].strip() == "cm":
            if not int(passport["hgt"][:-2]) >= 150 or not int(passport["hgt"][:-2]) <= 193:
                continue
        elif passport["hgt"][-2:].strip() == "in":
            if not int(passport["hgt"][:-2]) >= 59 or not int(passport["hgt"][:-2]) <= 76:
                continue
        else:
            continue

        if not len(passport["hcl"]) == 7 or not re.search("#[a-z0-9]*", passport["hcl"]):
            continue

        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        try:
            if not len(passport["pid"]) == 9:
                continue
            int(passport["pid"])
        except RuntimeError:
            continue

        count += 1
    return count

print(countValid())