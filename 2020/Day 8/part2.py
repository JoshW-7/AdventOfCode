from copy import deepcopy


class CPU:
    def __init__(self, program=[]):
        self.pc = 0
        self.accumulator = 0
        self.program = program
        self.memory_size = len(self.program)
        self.used_indexes = set()
        self.running = True
        self.valid = False

    def decode(self):
        self.used_indexes.add(self.pc)
        op, args = self.program[self.pc]

        if func := getattr(self, op):
            func(args)
        else:
            print(f"Unsupported opcode: {op}")

        if self.pc in self.used_indexes:
            self.running = False
            return
        if self.pc >= self.memory_size:
            self.valid = True
            self.running = False

    def nop(self, args):
        self.pc += 1

    def acc(self, args):
        self.accumulator += int(args[0])
        self.pc += 1

    def jmp(self, args):
        self.pc += int(args[0])
        
with open("input.txt") as file:
    lines = file.read().split("\n")
    program = []
    for line in lines:
        op, *args = line.split(" ")
        program.append([op, args])

    jmp_lines = [i for i,line in enumerate(program) if line[0] == "jmp"]
    for index in jmp_lines:
        temp_program = deepcopy(program)
        temp_program[index][0] = "nop"
        cpu = CPU(program=temp_program)
        while cpu.running:
            cpu.decode()
        if cpu.valid:
            print(cpu.accumulator)

    nop_lines = [i for i,line in enumerate(program) if line[0] == "nop"]
    for index in nop_lines:
        temp_program = deepcopy(program)
        temp_program[index][0] = "jmp"
        cpu = CPU(program=temp_program)
        while cpu.running:
            cpu.decode()
        if cpu.valid:
            print(cpu.accumulator)