

with open("input.txt") as file:
    cups = [int(c) for c in file.read()]

# Add the ~million extra cups
for i in range(max(cups)+1, 1000001):
    cups.append(i)


class Cup:
    CUPS = {}

    def __init__(self, value):
        self.value = value
        self.next = None
        self.current = False

        Cup.CUPS[self.value] = self

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"

    # Display a segment of the circle of cups starting at cup with value "start" and the next "length" cups in sequence
    @classmethod
    def display(cls, start, length):
        start_cup = Cup.CUPS[start]
        if start_cup.current:
            result = f"({start_cup}) "
        else:
            result = str(start_cup) + " "
        for _ in range(length):
            start_cup = start_cup.next
            result += f"({Cup.CUPS[start_cup.value]}) " if start_cup.current else f"{Cup.CUPS[start_cup.value]} "
        result = result[:-1]
        return result

# Generate a linked list of cups
linked_cups = []
for cup in cups:
    linked_cups.append(Cup(value=cup))
for i,cup in enumerate(linked_cups):
    if i == len(linked_cups) - 1:
        cup.next = linked_cups[0]
    else:
        cup.next = linked_cups[i+1]

debug = False
current_cup = linked_cups[0]
current_cup.current = True
rounds = 0
while True:
    if debug:
        print("Cups: " + Cup.display(3, 8))

    rounds += 1
    if rounds > 10000000:
        break

    # Get the next four cups (last is the next current cup)
    next_cups = []
    start_cup = current_cup
    for i in range(4):
        if i == 3:
            current_cup.next = start_cup.next
        else:
            next_cups.append(start_cup.next)
        start_cup = start_cup.next

    # Get the destination
    # If we go below 1, wrap around to 1000000
    if (current_cup.value - 1) == 0:
        destination_cup = Cup.CUPS[1000000]
    else:
        destination_cup = Cup.CUPS[current_cup.value - 1]

    # Make sure the destination cup isn't in our next cups
    # While it is, subtract one until it isn't
    while destination_cup in next_cups:
        destination_cup = Cup.CUPS.get(destination_cup.value - 1)
        if destination_cup is None:
            destination_cup = Cup.CUPS[1000000]

    if debug:
        print("Next: " + str(next_cups))
        print("Destination: " + str(destination_cup))
        print()

    # Insert next cups
    next_cups[-1].next = destination_cup.next
    destination_cup.next = next_cups[0]

    # Update which cup is the currently selected one
    current_cup.current = False
    current_cup = current_cup.next
    current_cup.current = True
    
answer = Cup.display(Cup.CUPS[1].next.value, 1)
answer = int(answer.split(" ")[0]) * int(answer.split(" ")[1])
print(answer)