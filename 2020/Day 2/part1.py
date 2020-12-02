import re


def password_valid():
    pass


counter = 0
with open("input.txt") as file:
    for line in file.readlines():
        rule,password = line.split(":")
        password = password.lstrip(" ").rstrip("\n")
        
        m = re.match(r"([0-9]*)-([0-9]*)[ ]*([a-zA-Z])", rule)
        low = int(m.group(1))
        high = int(m.group(2))
        letter = m.group(3)
        
        if list(password).count(letter) >= low and list(password).count(letter) <= high:
            counter += 1
            print(line)

print(counter)