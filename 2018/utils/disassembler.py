from sys import stdin


def print_addr(a, b, c, symbols):
    print('addr', symbols[a], symbols[b], symbols[c])


def print_addi(a, b, c, symbols):
    print('addi', symbols[a], b, symbols[c])


def print_mulr(a, b, c, symbols):
    print('mulr', symbols[a], symbols[b], symbols[c])


def print_muli(a, b, c, symbols):
    print('muli', symbols[a], b, symbols[c])


def print_banr(a, b, c, symbols):
    print('banr', symbols[a], symbols[b], symbols[c])


def print_bani(a, b, c, symbols):
    print('bani', symbols[a], b, symbols[c])


def print_borr(a, b, c, symbols):
    print('borr', symbols[a], symbols[b], symbols[c])


def print_bori(a, b, c, symbols):
    print('bori', symbols[a], b, symbols[c])


def print_setr(a, b, c, symbols):
    print('setr', symbols[a], '_', symbols[c])


def print_seti(a, b, c, symbols):
    print('seti', a, '_', symbols[c])


def print_gtir(a, b, c, symbols):
    print('gtir', a, symbols[b], symbols[c])


def print_gtri(a, b, c, symbols):
    print('gtri', symbols[a], b, symbols[c])


def print_gtrr(a, b, c, symbols):
    print('gtrr', symbols[a], symbols[b], symbols[c])


def print_eqir(a, b, c, symbols):
    print('eqir', a, symbols[b], symbols[c])


def print_eqri(a, b, c, symbols):
    print('eqri', symbols[a], b, symbols[c])


def print_eqrr(a, b, c, symbols):
    print('eqrr', symbols[a], symbols[b], symbols[c])


print_funcs = dict(
    addr=print_addr,
    addi=print_addi,
    mulr=print_mulr,
    muli=print_muli,
    banr=print_banr,
    bani=print_bani,
    borr=print_borr,
    bori=print_bori,
    setr=print_setr,
    seti=print_seti,
    gtir=print_gtir,
    gtri=print_gtri,
    gtrr=print_gtrr,
    eqir=print_eqir,
    eqri=print_eqri,
    eqrr=print_eqrr)


def parse_instruction(line):
    opcode, a, b, c = line.split()
    return opcode, int(a), int(b), int(c)


def main():
    ip_line, *program_lines = stdin.read().splitlines()
    ip = int(ip_line.split()[-1])
    program = [parse_instruction(line) for line in program_lines]
    symbols = list('abcdefghijklmnopqrstuvwxyz')
    symbols[ip] = 'ip'

    for opcode, a, b, c in program:
        func = print_funcs[opcode]
        func(a, b, c, symbols)


if __name__ == '__main__':
    main()
