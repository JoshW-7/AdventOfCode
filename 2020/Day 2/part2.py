import re


counter = 0
with open("input.txt") as file:
    for line in file.readlines():
        m = re.match(r"([0-9]*)-([0-9]*)[ ]*([a-zA-Z]): ([a-zA-Z]*)", line)
        low = int(m.group(1))
        high = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        
        letter_count = 0
        if password[low-1] == letter:
            letter_count += 1
        if password[high-1] == letter:
            letter_count += 1
        if letter_count == 1:
            counter += 1

print(counter)