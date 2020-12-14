

with open("input.txt") as file:
    lines = file.read().split("\n")


memory = {}

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for line in lines:
    if line.startswith("mask"):
        mask = line.split(" = ")[1]
    elif line.startswith("mem"):
        address = int(line[4:line.find("]")])
        value = int(line.split(" = ")[1])

        for i,c in enumerate(reversed(mask)):
            if c in "01":
                if c == "1":
                    value |= (0x1 << i)
                elif c == "0":
                    value &= ~(0x1 << i)
        print(value)
        memory[address] = 0
        for i in range(36):
            memory[address] |= (value & (0x1 << i))

total = 0
for address in memory:
    total += memory[address]
                
print(total)
#print(memory)