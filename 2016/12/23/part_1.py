from sys import stdin


def parse_instruction(line):
    op, *arg_strs = line.split()
    args = [s if s.isalpha() else int(s) for s in arg_strs]
    return op, args


def main():
    instructions = [parse_instruction(line.strip()) for line in stdin]
    registers = dict(a=7, b=0, c=0, d=0)
    i = 0

    while 0 <= i < len(instructions):
        op, args = instructions[i]

        if op == 'cpy':
            x, y = args

            if type(y) is int:
                i += 1
                continue

            if type(x) is str:
                x = registers[x]

            registers[y] = x
            i += 1
        elif op == 'inc':
            [x] = args

            if type(x) is int:
                i += 1
                continue

            registers[x] += 1
            i += 1
        elif op == 'dec':
            [x] = args

            if type(x) is int:
                i += 1
                continue

            registers[x] -= 1
            i += 1
        elif op == 'jnz':
            x, y = args

            if type(x) is str:
                x = registers[x]

            if type(y) is str:
                y = registers[y]

            if x:
                i += y
            else:
                i += 1
        elif op == 'tgl':
            [x] = args

            if type(x) is str:
                x = registers[x]

            i2 = i + x

            if 0 <= i2 < len(instructions):
                op_2, args_2 = instructions[i2]

                if len(args_2) == 1:
                    op_2 = 'dec' if op_2 == 'inc' else 'inc'
                elif len(args_2) == 2:
                    op_2 = 'cpy' if op_2 == 'jnz' else 'jnz'

                instructions[i2] = op_2, args_2

            i += 1

    print(registers['a'])


if __name__ == '__main__':
    main()
