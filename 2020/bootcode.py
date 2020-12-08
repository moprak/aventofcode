class Bootcode:
    def __init__(self, program, mod_ptr = -1):
        self.program = program
        self.reset(mod_ptr)

    def step(self):
        op, arg = self.program[self.ptr]
        if( self.ptr == self.mod_ptr ):
            op, arg = self.do_mod(op, arg)
        if op == 'acc':
            self.acc += arg
            self.ptr += 1
        elif op == 'jmp':
            self.ptr += arg
        elif op == 'nop':
            self.ptr += 1

    def run(self):
        while not (self.halted or self.looped):
            if self.ptr in self.call_stack:
                self.looped = True
            elif self.ptr == len(self.program):
                self.halted = True
            else:
                self.call_stack.append(self.ptr)
                self.step()
        return self.acc

    def do_mod(self, op, arg):
        if op == 'jmp':
            return 'nop', arg
        elif op == 'nop':
            return 'jmp', arg
        return op, arg

    def reset(self, mod_ptr = -1):
        self.ptr = 0
        self.acc = 0
        self.halted = False
        self.looped = False
        self.call_stack = []
        self.mod_ptr = mod_ptr
