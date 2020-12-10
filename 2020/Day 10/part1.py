

with open("input.txt") as file:
    lines = file.read().split("\n")
    nums = [int(line) for line in lines]
    nums.sort()

max_num = max(nums)
max_voltage = max_num + 3


differences = []
current_voltage = 0
for num in nums:
    differences.append(num - current_voltage)
    current_voltage = num
differences.append(3)


difference_1 = 0
difference_3 = 0
for difference in differences:
    if difference == 1:
        difference_1 += 1
    if difference == 3:
        difference_3 += 1

print(difference_1)
print(difference_3)

print(difference_1 * difference_3)