from itertools import combinations


# Get input as a list of integers
with open("input.txt") as file:
    lines = file.read().split("\n")
    numbers = [int(line) for line in lines]

# Get the first set of numbers in the preamble
index = 25
preamble = set(numbers[index-25:index])
while True:
    valid = False

    # Find a combination of two numbers in the preamble that sum to the current index being checked
    for a,b in combinations(preamble, 2):
        s = a + b

        # If there's a valid sum, increment the index and create the new preamble
        if s == numbers[index]:
            valid = True
            index += 1
            preamble = set(numbers[index-25:index])
            break

    # If there wasn't a valid sum for the last index, we're done
    if not valid:
        break

# The answer for part 1
bad_num = numbers[index]

for i,num in enumerate(numbers):
    total = 0
    j = 0
    sub_nums = []

    # Sum the numbers from index until they become larger than bad_num and add them to a list
    while total < bad_num:
        sub_num = numbers[i+j]
        total += numbers[i+j]
        sub_nums.append(sub_num)
        j += 1

    # If the sum was equal to bad_num, we're done
    if total == bad_num:
        break

# The answer for part 2
print(min(sub_nums) + max(sub_nums))