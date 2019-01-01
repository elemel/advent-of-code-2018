from sys import stdin


def parse_instruction(line):
    op, args_str = line.split(' ', 1)

    if op in ['hlf', 'tpl', 'inc']:
        return op, args_str
    elif op == 'jmp':
        return op, int(args_str)
    else:
        r, offset_str = args_str.split(', ')
        return op, r, int(offset_str)


def main():
    instructions = [parse_instruction(line.strip()) for line in stdin]
    registers = dict(a=1, b=0)
    i = 0

    while i < len(instructions):
        instruction = instructions[i]
        op = instruction[0]

        if op == 'hlf':
            _, r = instruction
            registers[r] //= 2
            i += 1
        elif op == 'tpl':
            _, r = instruction
            registers[r] *= 3
            i += 1
        elif op == 'inc':
            _, r = instruction
            registers[r] += 1
            i += 1
        elif op == 'jmp':
            _, offset = instruction
            i += offset
        elif op == 'jie':
            _, r, offset = instruction
            i = i + offset if registers[r] % 2 == 0 else i + 1
        elif op == 'jio':
            _, r, offset = instruction
            i = i + offset if registers[r] == 1 else i + 1

    print(registers['b'])


if __name__ == '__main__':
    main()
