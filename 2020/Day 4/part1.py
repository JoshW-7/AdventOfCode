

with open("input.txt") as file:
    data = []
    for line in file.readlines():
        line = line.strip("\n")
        data.append(line)

passports = []
lines = []
for line in data:
    if len(line) > 0:
        lines.append(line)
    else:
        passports.append(lines)
        lines = []

data = []
for p in passports:
    p = " ".join([line for line in p])
    data.append(p)


def valid(line):
    if "byr" not in pd:
        return False
    if "iyr" not in pd:
        return False
    if "eyr" not in pd:
        return False
    if "hgt" not in pd:
        return False
    if "hcl" not in pd:
        return False
    if "ecl" not in pd:
        return False
    if "pid" not in pd:
        return False
    

    return True

count = 0
for line in data:
    pairs = line.split(" ")
    pd = {}
    for pair in pairs:
        key,value = pair.split(":")
        pd[key] = value

    print(pd)
    if valid(pd):
        count += 1
        print("It's valid")

print(count)
    