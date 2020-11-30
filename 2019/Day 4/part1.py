

with open("input.txt") as file:
    low,high = [int(number) for number in file.readline().split("-")]

count = 0
for number in range(low, high):
    chars = list(str(number))
    found_double = False
    increasing = True
    prev_char = None
    for char in chars:
        if char == prev_char:
            found_double = True
        if prev_char is not None and int(char) < int(prev_char):
            increasing = False
            break
        prev_char = char
    if found_double and increasing:
        count += 1

print(count)