

with open("input.txt") as file:
    entries = [int(line) for line in file.readlines()]

result = 0
for entry in entries:
    for second_entry in entries:
        for third_entry in entries:
            if entry + second_entry + third_entry == 2020:
                result = entry * second_entry * third_entry
                
print(result)