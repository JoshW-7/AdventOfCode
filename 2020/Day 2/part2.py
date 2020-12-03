import re


counter = 0
with open("input.txt") as file:
    for line in file.readlines():
        m = re.match(r"(?P<low>[0-9]*)-(?P<high>[0-9]*)[\s]*(?P<letter>[a-zA-Z]):[\s]*(?P<password>[a-zA-Z]*)", line)
        low = int(m.group("low"))
        high = int(m.group("high"))
        letter = m.group("letter")
        password = m.group("password")
        
        letter_count = 0
        if password[low-1] == letter:
            letter_count += 1
        if password[high-1] == letter:
            letter_count += 1
        if letter_count == 1:
            counter += 1

print(counter)