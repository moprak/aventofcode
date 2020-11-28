from collections import defaultdict
class Intcode:
    def __init__(self, program, inputs = []):
        self.program = program[:]
        self.ptr = 0
        self.inputs = inputs
        self.outputs = []
        self.input_count = 0
        self.produced_output = False
        self.halted = False
        self.memory = {}
        self.relative_base = 0
        self.input_func = None
    def add_input(self, d):
        self.inputs = [d] + self.inputs
    def get(self, idx):
        if idx < len(self.program):
            return self.program[idx]
        return self.memory.get(idx,0)
    def set(self, idx, value):
        if idx < len(self.program):
            self.program[idx] = value
        else:
            self.memory[idx] = value
    def get_params(self, ptr, nargs):
        params = []
        for i in range(nargs):
            mode = (self.get(self.ptr)//int(10**(2+i)))%10
            if mode == 1:
                params.append(self.ptr+i+1)
            elif mode == 2:
                params.append(self.get(self.ptr + i + 1) + self.relative_base)
            else:
                params.append(self.get(self.ptr + i + 1))
        return params
    def run(self):
        while not self.halted and not self.produced_output:
            opcode = self.get(self.ptr)%100
            if opcode == 99:
                self.halted = True
            elif opcode == 1:
                params = self.get_params(self.ptr, 3)
                self.set(params[2] , self.get(params[0]) + self.get(params[1]))
                self.ptr += 4
            elif opcode == 2:
                params = self.get_params(self.ptr, 3)
                self.set(params[2] , self.get(params[0]) * self.get(params[1]))
                self.ptr += 4
            elif opcode == 3:
                params = self.get_params(self.ptr, 1)
                self.input_count += 1
                if self.inputs:
                    self.set(params[0] , self.inputs.pop())
                elif self.input_func:
                    self.set(params[0] , self.input_func())
                else:
                    self.set(params[0] , int(input('enter input: ')))
                self.ptr +=2
            elif opcode == 4:
                params = self.get_params(self.ptr, 1)
                self.outputs.append(self.get(params[0]))
                self.produced_output = True
                self.ptr +=2
            elif opcode == 5:
                params = self.get_params(self.ptr, 2)
                if self.get(params[0]):
                    self.ptr = self.get(params[1])
                else:
                    self.ptr +=3
            elif opcode == 6:
                params = self.get_params(self.ptr, 2)
                if not self.get(params[0]):
                    self.ptr = self.get(params[1])
                else:
                    self.ptr +=3
            elif opcode == 7:
                params = self.get_params(self.ptr, 3)
                self.set(params[2] , int(self.get(params[0]) < self.get(params[1])))
                self.ptr += 4
            elif opcode == 8:
                params = self.get_params(self.ptr, 3)
                self.set(params[2] , int(self.get(params[0]) == self.get(params[1])))
                self.ptr += 4
            elif opcode == 9:
                params = self.get_params(self.ptr, 1)
                self.relative_base += self.get(params[0])
                self.ptr += 2
