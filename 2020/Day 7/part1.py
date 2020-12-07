

def contains_bag(bag_type, bag):
    if bag_type in mapping[bag]:
        return True
    else:
        for sub_bag,amount in mapping[bag].items():
            if contains_bag(bag_type, sub_bag):
                return True
    return False

with open("input.txt") as file:
    lines = file.read().split("\n")
    mapping = {}
    for line in lines:
        bag_type = line[0:line.find(" bags")]
        contains = line[line.find(" contain ")+len(" contain "):]
        bags = []
        if not contains.startswith("no"):
            bags = contains.split(", ")
        mapping[bag_type] = {}
        for text in bags:
            amount = int(text[0])
            other_bag = text[2:text.find(" bag")]
            mapping[bag_type][other_bag] = amount

count = 0
for bag_type,data in mapping.items():
    if contains_bag("shiny gold", bag_type):
        count += 1

print(count)
