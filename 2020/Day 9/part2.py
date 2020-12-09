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

bad_num = numbers[index]

for i,num in enumerate(numbers):
    total = 0
    j = 0
    sub_nums = []
    while total < bad_num:
        sub_num = numbers[i+j]
        total += numbers[i+j]
        sub_nums.append(sub_num)
        j += 1
    if total == bad_num:
        break

print(min(sub_nums) + max(sub_nums))