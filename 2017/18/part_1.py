from collections import defaultdict
from sys import stdin


def parse_instruction(line):
    op, *args = line.split()
    args = [arg if arg.isalpha() else int(arg) for arg in args]
    return op, args


def read_value(registers, arg):
    return arg if type(arg) is int else registers[arg]


def main():
    instructions = [parse_instruction(line.strip()) for line in stdin]
    registers = defaultdict(int)
    i = 0
    sound = 0

    while 0 <= i < len(instructions):
        op, args = instructions[i]

        if op == 'snd':
            [x] = args
            sound = read_value(registers, x)
        elif op == 'set':
            x, y = args
            registers[x] = read_value(registers, y)
        elif op == 'add':
            x, y = args
            registers[x] += read_value(registers, y)
        elif op == 'mul':
            x, y = args
            registers[x] *= read_value(registers, y)
        elif op == 'mod':
            x, y = args
            registers[x] %= read_value(registers, y)
        elif op == 'rcv':
            [x] = args

            if sound != 0:
                print(sound)
                return
        elif op == 'jgz':
            x, y = args

            if read_value(registers, x) > 0:
                i += read_value(registers, y) - 1
        else:
            raise ValueError(f'Invalid instruction: {op}')

        i += 1


if __name__ == '__main__':
    main()
