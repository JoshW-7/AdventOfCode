

with open("input.txt") as file:
    lines = file.read().split("\n")




acc = 0
pc = 0

program = []
for line in lines:
    op, num = line.split(" ")
    num = int(num)
    program.append((op, num))


def decode(line):
    global acc, pc
    op = line[0]
    num = line[1]
    pc_add = 1
    if op == "acc":
        acc += num
    if op == "jmp":
        pc_add = num

    return pc_add

used_indexes = []

while True:
    print(program[pc])
    if pc in used_indexes:
        break
    used_indexes.append(pc)
    pc += decode(program[pc])
    

print(acc)
