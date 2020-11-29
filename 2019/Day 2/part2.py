

class CPU:
    def __init__(self):
        self.reset()

    def reset(self):
        self.running = True
        self.position = 0
        with open("input.txt") as file:
            self.bytecode = [int(num) for num in file.readline().split(",")]

    def set_noun(self, value):
        self.bytecode[1] = value

    def set_verb(self, value):
        self.bytecode[2] = value

    def get_result(self):
        while self.running:
            self.decode()
        return self.bytecode[0]

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
result = 0
done = False
while not done:
    for i in range(0, 100):
        if done:
            break
        for j in range(0, 100):
            cpu.reset()
            cpu.set_noun(i)
            cpu.set_verb(j)
            result = cpu.get_result()
            if result == 19690720:
                done = True
                break

print(100 * cpu.bytecode[1] + cpu.bytecode[2])
