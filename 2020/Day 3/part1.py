

with open("input.txt") as file:
    levels = []
    for line in file.readlines():
        line = line.strip("\n")
        levels.append(list(line))

x = 0
y = 0
xv = 3
yv = 1
count = 0
while y < len(levels):
    if x >= len(levels[0]):
        x = (x - len(levels[0]))
    value = levels[y][x]
    if value == "#":
        count += 1
    x += xv
    y += yv

print(count)