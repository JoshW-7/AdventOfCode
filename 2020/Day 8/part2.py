

class CPU:
    def __init__(self, program=[]):
        self.pc = 0
        self.acc = 0
        self.program = program
        self.used_indexes = set()
        self.running = True
        self.valid = False

    def decode(self):
        self.used_indexes.add(self.pc)
        op, num = self.program[self.pc]

        if op == "nop":
            self.pc += 1
        if op == "acc":
            self.acc += num
            self.pc += 1
        if op == "jmp":
            self.pc += num

        if self.pc in self.used_indexes:
            self.running = False
            return
        if self.pc >= len(self.program):
            self.valid = True
            self.running = False
        
        
with open("input.txt") as file:
    lines = file.read().split("\n")
    program = []
    for line in lines:
        op, num = line.split(" ")
        num = int(num)
        program.append([op, num])

    jmp_lines = [i for i,line in enumerate(program) if line[0] == "jmp"]
    for index in jmp_lines:
        temp_program = [[op,num] for op,num in program]
        temp_program[index][0] = "nop"
        cpu = CPU(program=temp_program)
        while cpu.running:
            cpu.decode()
        if cpu.valid:
            print(cpu.acc)

    nop_lines = [i for i,line in enumerate(program) if line[0] == "nop"]
    for index in nop_lines:
        temp_program = [[op,num] for op,num in program]
        temp_program[index][0] = "jmp"
        cpu = CPU(program=temp_program)
        while cpu.running:
            cpu.decode()
        if cpu.valid:
            print(cpu.acc)