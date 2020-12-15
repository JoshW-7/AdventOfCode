

with open("input.txt") as file:
    lines = file.read().split("\n")
    nums = [int(n) for n in lines[0].split(",")]

numbers = {}
for i,number in enumerate(nums):
    numbers[number] = [i]
    last_number = number

i = len(numbers)
while True:
    if last_number not in numbers:
        next_number = 0
        if next_number in numbers:
            numbers[next_number].append(i)
        else:
            numbers[next_number] = [i]
    else:
        if len(numbers[last_number]) >= 2:
            last_times = numbers[last_number][-2:]
            difference = last_times[1] - last_times[0]
            next_number = difference
            if next_number in numbers:
                numbers[next_number].append(i)
            else:
                numbers[next_number] = [i]
        else:
            next_number = 0
            if next_number in numbers:
                numbers[next_number].append(i)
            else:
                numbers[next_number] = [i]

    last_number = next_number
    i += 1
    if i == 30000000:
        print(last_number)
        break
