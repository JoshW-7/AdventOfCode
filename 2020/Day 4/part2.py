import re


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
    else:
        value = int(pd["byr"])
        if value < 1920 or value > 2002:
            return False
            
    if "iyr" not in pd:
        return False
    else:
        value = int(pd["iyr"])
        if value < 2010 or value > 2020:
            return False

    if "eyr" not in pd:
        return False
    else:
        value = int(pd["eyr"])
        if value < 2020 or value > 2030:
            return False

    if "hgt" not in pd:
        return False
    else:
        num_str = pd["hgt"]
        if num_str.endswith("cm"):
            num = int(num_str[:num_str.find("cm")])
            if num < 150 or num > 193:
                return False
        elif num_str.endswith("in"):
            num = int(num_str[:num_str.find("in")])
            if num < 59 or num > 76:
                return False
        else:
            return False

    if "hcl" not in pd:
        return False
    else:
        hair = pd["hcl"]
        if not hair.startswith("#"):
            return False
        else:
            m = re.match(r"#([a-fA-F0-9]{6})", hair)
            if m:
                for c in m.group(1):
                    if c not in ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        return False
            else:
                return False

    if "ecl" not in pd:
        return False
    else:
        eye = pd["ecl"]
        found = False
        for color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            if color in eye:
                found = True
                break
        if not found:
            return False

    if "pid" not in pd:
        return False
    else:
        pid = pd["pid"]
        m = re.match(r"([0-9]{9})", pid)
        if not m:
            return False
        if len(pid) > 9:
            return False

    return True

count = 0
for line in data:
    pairs = line.split(" ")
    pd = {}
    for pair in pairs:
        key,value = pair.split(":")
        pd[key] = value

    if valid(pd):
        count += 1

print(count)
    