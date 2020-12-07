

def count_bags(bag):
    count = 0
    for sub_bag,amount in mapping[bag].items():
        count += amount
        count += amount * count_bags(sub_bag)
    return count
    
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

print(count_bags("shiny gold"))