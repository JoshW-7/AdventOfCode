

with open("input.txt") as file:
    low,high = [int(number) for number in file.readline().split("-")]

count = 0
for number in range(low, high+1):
    chars = list(str(number))
    increasing = True
    prev_char = None
    doubles = {}
    for char in chars:
        if char == prev_char:
            if doubles.get(int(char)) is None:
                doubles[int(char)] = 1
            doubles[int(char)] += 1
        if prev_char is not None and int(char) < int(prev_char):
            increasing = False
            break
        prev_char = char
    if not increasing:
        continue
    elif doubles:
        for num,counter in doubles.items():
            if counter == 2:
                count += 1
                break

print(count)    

    