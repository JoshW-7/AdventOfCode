

class CPU:
    def __init__(self):
        self.running = True
        self.position = 0
        with open("input.txt") as file:
            self.bytecode = [int(num) for num in file.readline().split(",")]

    def fix(self):
        self.bytecode[1] = 12
        self.bytecode[2] = 2

    def run(self):
        while self.running:
            self.decode()

    def decode(self):
        opcode = self.bytecode[self.position]
        if opcode == 99:
            self.running = False
        elif opcode == 1:
            location_1 = self.bytecode[self.position+1]
            location_2 = self.bytecode[self.position+2]
            location_3 = self.bytecode[self.position+3]
            self.bytecode[location_3] = self.bytecode[location_1] + self.bytecode[location_2]
        elif opcode == 2:
            location_1 = self.bytecode[self.position+1]
            location_2 = self.bytecode[self.position+2]
            location_3 = self.bytecode[self.position+3]
            self.bytecode[location_3] = self.bytecode[location_1] * self.bytecode[location_2]
        self.position += 4

cpu = CPU()
cpu.fix()
cpu.run()

print(cpu.bytecode[0])