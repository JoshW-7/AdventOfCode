

with open("input.txt") as file:
    cups = [int(c) for c in file.read()]

for i in range(max(cups)+1, 1000001):
    cups.append(i)

class Cup:
    CUPS = {}

    def __init__(self, value):
        self.value = value
        self.next = None
        Cup.CUPS[self.value] = self
        self.current = False

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"

    @classmethod
    def display(cls, start, length):
        start_cup = Cup.CUPS[start]
        if start_cup.current:
            result = f"({start_cup}) "
        else:
            result = str(start_cup) + " "
        for i in range(length):
            start_cup = start_cup.next
            result += f"({Cup.CUPS[start_cup.value]}) " if start_cup.current else f"{Cup.CUPS[start_cup.value]} "
            
        result = result[:-1]
        return result

linked_cups = []
for cup in cups:
    linked_cups.append(Cup(value=cup))

for i,cup in enumerate(linked_cups):
    if i == len(linked_cups) - 1:
        cup.next = linked_cups[0]
    else:
        cup.next = linked_cups[i+1]

current_cup = linked_cups[0]
current_cup.current = True
rounds = 0
while True:
    # print(Cup.display(3, 8))

    rounds += 1
    if rounds > 10000000:
        break

    # Get the next four cups (last is the next current cup)
    next_cups = []
    start_cup = current_cup
    for i in range(4):
        if i == 3:
            next_cup = start_cup.next
            current_cup.next = next_cup
        else:
            next_cups.append(start_cup.next)
        start_cup = start_cup.next
    
    # print(next_cups)

    # Get the destination
    if (current_cup.value - 1) == 0:
        destination_cup = Cup.CUPS[1000000]
    else:
        destination_cup = Cup.CUPS[current_cup.value - 1]
    while destination_cup in next_cups:
        destination_cup = Cup.CUPS.get(destination_cup.value - 1)
        if destination_cup is None:
            destination_cup = Cup.CUPS[1000000]

    # Insert next cups
    next_cups[-1].next = destination_cup.next
    destination_cup.next = next_cups[0]

    current_cup.current = False
    current_cup = current_cup.next
    current_cup.current = True
    
answer = Cup.display(Cup.CUPS[1].next.value, 1)
answer = int(answer.split(" ")[0]) * int(answer.split(" ")[1])
print(answer)