

with open("input.txt") as file:
    groups = file.read().split("\n\n")

count = 0
for group in groups:
    people = [set(person) for person in group.split("\n")]
    common = people[0]
    if len(people) > 0:
        for person in people:
            common.intersection_update(person)
    count += len(common)

print(count)