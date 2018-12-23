# ElfCode disassembler


from sys import argv, stdin


def format_instruction_elfcode(i, opcode, a, b, c, symbols):
    if opcode == 'addr':
        return f'addr {symbols[a]} {symbols[b]} {symbols[c]}'
    elif opcode == 'addi':
        return f'addi {symbols[a]} {b} {symbols[c]}'
    elif opcode == 'mulr':
        return f'mulr {symbols[a]} {symbols[b]} {symbols[c]}'
    elif opcode == 'muli':
        return f'muli {symbols[a]} {b} {symbols[c]}'
    elif opcode == 'banr':
        return f'banr {symbols[a]} {symbols[b]} {symbols[c]}'
    elif opcode == 'bani':
        return f'bani {symbols[a]} {b} {symbols[c]}'
    elif opcode == 'borr':
        return f'borr {symbols[a]} {symbols[b]} {symbols[c]}'
    elif opcode == 'bori':
        return f'bori {symbols[a]} {b} {symbols[c]}'
    elif opcode == 'setr':
        return f'setr {symbols[a]} _ {symbols[c]}'
    elif opcode == 'seti':
        return f'seti {a} _ {symbols[c]}'
    elif opcode == 'gtir':
        return f'gtir {a} {symbols[b]} {symbols[c]}'
    elif opcode == 'gtri':
        return f'gtri {symbols[a]} {b} {symbols[c]}'
    elif opcode == 'gtrr':
        return f'gtrr {symbols[a]} {symbols[b]} {symbols[c]}'
    elif opcode == 'eqir':
        return f'eqir {a} {symbols[b]} {symbols[c]}'
    elif opcode == 'eqri':
        return f'eqri {symbols[a]} {b} {symbols[c]}'
    elif opcode == 'eqrr':
        return f'eqrr {symbols[a]} {symbols[b]} {symbols[c]}'
    else:
        raise ValueError(f'Unknown opcode: {opcode}')


def format_instruction_c(i, opcode, a, b, c, symbols):
    if opcode == 'addr':
        if a == c:
            if symbols[c] == 'ip':
                return f'if ({symbols[b]} == 1) goto i{i + 2};'
            else:
                return f'{symbols[c]} += {symbols[b]};'
        elif b == c:
            if symbols[c] == 'ip':
                return f'if ({symbols[a]} == 1) goto i{i + 2};'
            else:
                return f'{symbols[c]} += {symbols[a]};'
        else:
            return f'{symbols[c]} = {symbols[a]} + {symbols[b]};'
    elif opcode == 'addi':
        if a == c:
            if symbols[c] == 'ip':
                return f'goto i{i + b + 1};'
            else:
                return f'{symbols[c]} += {b};'
        else:
            return f'{symbols[c]} = {symbols[a]} + {b};'
    elif opcode == 'mulr':
        if a == c:
            return f'{symbols[c]} *= {symbols[b]};'
        elif b == c:
            return f'{symbols[c]} *= {symbols[a]};'
        else:
            return f'{symbols[c]} = {symbols[a]} * {symbols[b]};'
    elif opcode == 'muli':
        if a == c:
            return f'{symbols[c]} *= {b};'
        else:
            return f'{symbols[c]} = {symbols[a]} * {b};'
    elif opcode == 'banr':
        if a == c:
            return f'{symbols[c]} &= {symbols[b]};'
        elif b == c:
            return f'{symbols[c]} &= {symbols[a]};'
        else:
            return f'{symbols[c]} = {symbols[a]} & {symbols[b]};'
    elif opcode == 'bani':
        if a == c:
            return f'{symbols[c]} &= {b};'
        else:
            return f'{symbols[c]} = {symbols[a]} & {b};'
    elif opcode == 'borr':
        if a == c:
            return f'{symbols[c]} |= {symbols[b]};'
        elif b == c:
            return f'{symbols[c]} |= {symbols[a]};'
        else:
            return f'{symbols[c]} = {symbols[a]} | {symbols[b]};'
    elif opcode == 'bori':
        if a == c:
            return f'{symbols[c]} |= {b};'
        else:
            return f'{symbols[c]} = {symbols[a]} | {b};'
    elif opcode == 'setr':
        return f'{symbols[c]} = {symbols[a]};'
    elif opcode == 'seti':
        if symbols[c] == 'ip':
            return f'goto i{a + 1};'
        else:
            return f'{symbols[c]} = {a};'
    elif opcode == 'gtir':
        return f'{symbols[c]} = {a} > {symbols[b]} ? 1 : 0;'
    elif opcode == 'gtri':
        return f'{symbols[c]} = {symbols[a]} > {b} ? 1 : 0;'
    elif opcode == 'gtrr':
        return f'{symbols[c]} = {symbols[a]} > {symbols[b]} ? 1 : 0;'
    elif opcode == 'eqir':
        return f'{symbols[c]} = {a} == {symbols[b]} ? 1 : 0;'
    elif opcode == 'eqri':
        return f'{symbols[c]} = {symbols[a]} == {b} ? 1 : 0;'
    elif opcode == 'eqrr':
        return f'{symbols[c]} = {symbols[a]} == {symbols[b]} ? 1 : 0;'
    else:
        raise ValueError(f'Unknown opcode: {opcode}')


def format_instruction(target, i, opcode, a, b, c, symbols):
    if target == 'elfcode':
        return format_instruction_elfcode(i, opcode, a, b, c, symbols)
    elif target == 'c' or target == 'python':
        return format_instruction_c(i, opcode, a, b, c, symbols)
    else:
        raise ValueError(f'Unknown target: {target}')


def parse_instruction(line):
    opcode, a, b, c = line.split()
    return opcode, int(a), int(b), int(c)


def main():
    ip_line, *program_lines = stdin.read().splitlines()
    ip = int(ip_line.split()[-1])
    program = [parse_instruction(line) for line in program_lines]
    symbols = list('abcdefghijklmnopqrstuvwxyz')
    symbols[ip] = 'ip'

    numbered = '--number' in argv
    number_width = max(1, len(str(len(program) - 1)))

    labeled = '--label' in argv
    target = 'elfcode'

    if '--target=c' in argv:
        target = 'c'

    if '--target=python' in argv:
        target = 'python'

    commented = '--comment' in argv

    for i, (opcode, a, b, c) in enumerate(program):
        number = ''
        label = ''
        instruction = format_instruction(target, i, opcode, a, b, c, symbols)
        comment = ''

        if numbered:
            number = f'{i:0{number_width}}  '

        if labeled:
            if target == 'c':
                label = f'i{i}: '
            elif target == 'python':
                label = f'label.i{i}; '

        if commented:
            if opcode == 'addi' and a == ip and c == ip:
                comment = f' // break {i + b + 1}'
            elif opcode == 'addr' and a == ip and c == ip:
                comment = f' // branch'
            elif opcode == 'addr' and b == ip and c == ip:
                comment = f' // branch'
            elif opcode == 'seti' and c == ip:
                if a > i:
                    comment = f' // break {a + 1}'
                else:
                    comment = f' // continue {a + 1}'

        print(f'{number}{label}{instruction}{comment}')


if __name__ == '__main__':
    main()
