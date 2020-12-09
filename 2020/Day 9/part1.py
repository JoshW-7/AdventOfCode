from itertools import combinations



with open("input.txt") as file:
    lines = file.read().split("\n")
    numbers = [int(line) for line in lines]

preamble = set(numbers[0:25])

index = 25
while True:
    valid = False
    for a,b in combinations(preamble, 2):
        s = a + b
        if s == numbers[index]:
            valid = True
            index += 1
            preamble = set(numbers[index-25:index])
    if not valid:
        break

print(numbers[index])