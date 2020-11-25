class Intcode:
    def __init__(self, program, inputs = []):
        self.program = program[:]
        self.ptr = 0
        self.inputs = inputs
        self.outputs = []
        self.input_count = 0
    def get(self, idx):
        return self.program[idx]
    def set(self, idx, value):
        self.program[idx] = value
    def get_params(self, ptr, nargs):
            params = [ self.ptr+i+1 if (self.program[self.ptr]//int(10**(2+i)))%10 else self.program[self.ptr+i+1] for i in range(nargs)]
            return params
    def run(self):
        while self.program[self.ptr] != 99:
            opcode = self.program[self.ptr]%100
            if opcode == 1:
                params = self.get_params(self.ptr, 3)
                self.program[params[2]] = self.program[params[0]] + self.program[params[1]]
                self.ptr += 4
            elif opcode == 2:
                params = self.get_params(self.ptr, 3)
                self.program[params[2]] = self.program[params[0]] * self.program[params[1]]; self.ptr += 4
            elif opcode == 3:
                params = self.get_params(self.ptr, 1)
                self.input_count += 1
                print(self.inputs)
                if self.inputs:
                    self.program[params[0]] = self.inputs.pop()
                else:
                    self.program[params[0]] = int(input('enter input: '))
                self.ptr +=2
            elif opcode == 4:
                params = self.get_params(self.ptr, 1)
                self.outputs.append(self.program[params[0]])
                self.ptr +=2
            elif opcode == 5:
                params = self.get_params(self.ptr, 2)
                if self.program[params[0]]:
                    self.ptr = self.program[params[1]]
                else:
                    self.ptr +=3
            elif opcode == 6:
                params = self.get_params(self.ptr, 2)
                if not self.program[params[0]]:
                    self.ptr = self.program[params[1]]
                else:
                    self.ptr +=3
            elif opcode == 7:
                params = self.get_params(self.ptr, 3)
                self.program[params[2]] = int(self.program[params[0]] < self.program[params[1]]); self.ptr += 4
            elif opcode == 8:
                params = self.get_params(self.ptr, 3)
                self.program[params[2]] = int(self.program[params[0]] == self.program[params[1]]); self.ptr += 4
