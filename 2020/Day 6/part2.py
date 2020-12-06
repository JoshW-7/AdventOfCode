

with open("input.txt") as file:
    count = 0
    for group in file.read().split("\n\n"):
        people = [set(person) for person in group.split("\n")]
        common = people[0]
        if len(people) > 0:
            common.intersection_update(*people[1:])
        count += len(common)

print(count)