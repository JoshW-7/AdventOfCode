

with open("input.txt") as file:
    cups = [int(c) for c in file.read()]

rounds = 0
index = 0
while True:
    rounds += 1
    if rounds > 100:
        break
    if index >= len(cups):
        index = 0
    current_cup = cups[index]

    print("Cups: ", end="")
    for c in cups:
        if c == current_cup:
            print(f"({c}) ", end="")
        else:
            print(f"{c} ", end="")

    print()

    if (index + 4) >= len(cups):
        difference = (index+4)-len(cups)
        next_cups = []
        i = index + 1
        while i < len(cups):
            next_cups.append(cups.pop(i))
        for i in range(difference):
            next_cups.append(cups.pop(0))
    else:
        next_cups = cups[index+1:index+4]
        for cup in next_cups:
            cups.remove(cup)
    
    destination_cup = current_cup - 1
    if destination_cup == 0:
        destination_cup = max(cups)
    if destination_cup in next_cups:
        while destination_cup in next_cups:
            destination_cup -= 1
            if destination_cup == 0:
                destination_cup = max(cups)

    print("Next Cups: " + ", ".join([str(cup) for cup in next_cups]))
    print("Destination: " + str(destination_cup))

    for i,cup in enumerate(next_cups):
        cups.insert(cups.index(destination_cup)+1+i, cup)
    if cups.index(destination_cup) < index:
        diff = len(cups) - 1 - index
        if diff >= 3:
            diff = 3
        cup_indexes = [[cup, cups.index(cup)-diff] for cup in cups]
        for data in cup_indexes:
            if data[1] < 0:
                data[1] = len(cups) + data[1]
        cups = [None for i in range(len(cups))]
        for data in cup_indexes:
            cups[data[1]] = data[0]

    index += 1
    print()
        
length = len(cups) - 1
start_index = cups.index(1) + 1
i = start_index
count = 0
result = ""
while count < length:
    result += str(cups[i])
    i += 1
    if i >= len(cups):
        i = 0
    count += 1
print(result)
    