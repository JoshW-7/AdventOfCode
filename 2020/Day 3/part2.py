

with open("input.txt") as file:
    levels = []
    for line in file.readlines():
        line = line.strip("\n")
        levels.append(list(line))

totals = []
for xv,yv in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    count = 0
    x = 0
    y = 0
    height = len(levels)
    width = len(levels[0])
    while y < height:
        value = levels[y][x % width]
        if value == "#":
            count += 1
        x += xv
        y += yv
    totals.append(count)

total = totals[0] * totals[1] * totals[2] * totals[3] * totals[4]
print(total)