

with open("input.txt") as file:
    lines = file.read().split("\n")

groups = []
data = set()
for line in lines:
    if line == "":
        groups.append(data)
        data = set()
    else:
        for c in line:
            data.add(c)
        
count = 0
for data in groups:
    count += len(data)

print(count)