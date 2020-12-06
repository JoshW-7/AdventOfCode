

with open("input.txt") as file:
    lines = file.read().split("\n")

groups = []
people = []
for line in lines:
    if line == "":
        groups.append(people)
        people = []
    else:
        person = set(line)
        people.append(person)
        
count = 0
for group in groups:
    common = group[0]
    if len(group) > 0:
        for person in group[1:]:
            common.intersection_update(person)
    count += len(common)

print(count)