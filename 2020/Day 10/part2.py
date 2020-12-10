import math


with open("input.txt") as file:
    lines = file.read().split("\n")
    nums = [int(line) for line in lines]
    nums.extend([0, max(nums)+3])
    nums.sort()

counts = {num: 0 for num in nums}
counts[0] = 1

for i,num in enumerate(nums):
    if (i + 1) < len(nums):
        if nums[i+1] - num <= 3:
            counts[nums[i+1]] += counts[num]
    if (i + 2) < len(nums):
        if nums[i+2] - num <= 3:
            counts[nums[i+2]] += counts[num]
    if (i + 3) < len(nums):
        if nums[i+3] - num <= 3:
            counts[nums[i+3]] += counts[num]

print(counts[max(counts)])
