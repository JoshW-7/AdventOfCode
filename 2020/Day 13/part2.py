

with open("input.txt") as file:
    lines = file.read().split("\n")

buses = [num for num in lines[1].split(",")]

offsets = {}
for i,bus in enumerate(buses):
    if bus != "x":
        offsets[int(bus)] = i

# Brute-force solution
# Cannot solve puzzle input, but does solve all test cases
t = 0
while True:
    valid = True
    for bus,offset in offsets.items():
        if (t + offset) % bus != 0:
            valid = False
            break
    if valid:
        break
    t += 1
print(t)

