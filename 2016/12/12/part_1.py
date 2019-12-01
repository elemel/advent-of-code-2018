from sys import stdin


def parse_instruction(line):
    op, *arg_strs = line.split()
    args = [s if s.isalpha() else int(s) for s in arg_strs]
    return op, args


def main():
    instructions = [parse_instruction(line.strip()) for line in stdin]
    registers = dict(a=0, b=0, c=0, d=0)
    i = 0

    while 0 <= i < len(instructions):
        op, args = instructions[i]

        if op == 'cpy':
            x, y = args

            if type(x) is str:
                x = registers[x]

            registers[y] = x
            i += 1
        elif op == 'inc':
            [x] = args
            registers[x] += 1
            i += 1
        elif op == 'dec':
            [x] = args
            registers[x] -= 1
            i += 1
        elif op == 'jnz':
            x, y = args

            if type(x) is str:
                x = registers[x]

            if x:
                i += y
            else:
                i += 1

    print(registers['a'])


if __name__ == '__main__':
    main()
