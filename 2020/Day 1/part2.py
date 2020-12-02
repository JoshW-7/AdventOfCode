import itertools as it


with open("input.txt") as file:
    entries = [int(line) for line in file.readlines()]

combos = it.combinations(entries, 3)
for first,second,third in combos:
    if first + second + third == 2020:
        result = first * second * third
        break

print(result)