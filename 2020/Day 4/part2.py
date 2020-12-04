import re


def passport_valid(d):
    for attribute in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if attribute not in d:
            return False

    for key,value in d.items():
        valid = {
            "byr": lambda value: 1920 <= int(value) <= 2002,
            "iyr": lambda value: 2010 <= int(value) <= 2020,
            "eyr": lambda value: 2020 <= int(value) <= 2030,
            "hgt": lambda value: 150 <= int(value[:-2]) <= 193 if value.endswith("cm") else (59 <= int(value[:-2]) <= 76 if value.endswith("in") else False),
            "hcl": lambda value: value.startswith("#") and len(value[1:]) == 6 and bool(re.match(r"#[0-9a-f]{6}", value)),
            "ecl": lambda value: value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "pid": lambda value: len(value) == 9 and value.isdigit(),
            "cid": lambda value: True,
        }[key](value)
        if not valid:
            return False
    return True

with open("input.txt") as file:
    lines = file.read().split("\n")
    passports = []
    data = ""
    for line in lines:
        if len(line) == 0:
            passports.append(data.rstrip(" "))
            data = ""
        else:
            data += f"{line} "
    
    count = 0
    for data in passports:
        attributes = data.split(" ")
        d = {}
        for attribute in attributes:
            key,value = attribute.split(":")
            d[key] = value

        if passport_valid(d):
            count += 1
    
print(count)