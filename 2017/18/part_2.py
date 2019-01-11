from collections import defaultdict, deque
from sys import stdin


class Program:
    def __init__(self, instructions, p):
        self.instructions = instructions
        self.registers = defaultdict(int)
        self.registers['p'] = p
        self.i = 0
        self.queue = deque()
        self.send_count = 0
        self.other = None

    def read_value(self, arg):
        return arg if type(arg) is int else self.registers[arg]

    def step(self):
        if not 0 <= self.i < len(self.instructions):
            return False

        op, args = self.instructions[self.i]

        if op == 'snd':
            [x] = args
            self.other.queue.append(self.read_value(x))
            self.send_count += 1
        elif op == 'set':
            x, y = args
            self.registers[x] = self.read_value(y)
        elif op == 'add':
            x, y = args
            self.registers[x] += self.read_value(y)
        elif op == 'mul':
            x, y = args
            self.registers[x] *= self.read_value(y)
        elif op == 'mod':
            x, y = args
            self.registers[x] %= self.read_value(y)
        elif op == 'rcv':
            if not self.queue:
                return False

            [x] = args
            self.registers[x] = self.queue.popleft()
        elif op == 'jgz':
            x, y = args

            if self.read_value(x) > 0:
                self.i += self.read_value(y) - 1
        else:
            raise ValueError(f'Invalid instruction: {op}')

        self.i += 1
        return True


def parse_instruction(line):
    op, *args = line.split()
    args = [arg if arg.isalpha() else int(arg) for arg in args]
    return op, args


def main():
    instructions = [parse_instruction(line.strip()) for line in stdin]

    program_0 = Program(instructions, 0)
    program_1 = Program(instructions, 1)

    program_0.other = program_1
    program_1.other = program_0

    running_0 = running_1 = True

    while running_0 or running_1:
        running_0 = program_0.step()
        running_1 = program_1.step()

    print(program_1.send_count)


if __name__ == '__main__':
    main()
