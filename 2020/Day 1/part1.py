

with open("input.txt") as file:
    entries = [int(line) for line in file.readlines()]

result = 0
for entry in entries:
    for other_entry in entries:
        if entry + other_entry == 2020:
            result = entry * other_entry

print(result)