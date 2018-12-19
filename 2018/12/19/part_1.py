from sys import stdin


def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]


def addi(registers, a, b, c):
    registers[c] = registers[a] + b


def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]


def muli(registers, a, b, c):
    registers[c] = registers[a] * b


def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]


def bani(registers, a, b, c):
    registers[c] = registers[a] & b


def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]


def bori(registers, a, b, c):
    registers[c] = registers[a] | b


def setr(registers, a, b, c):
    registers[c] = registers[a]


def seti(registers, a, b, c):
    registers[c] = a


def gtir(registers, a, b, c):
    registers[c] = int(a > registers[b])


def gtri(registers, a, b, c):
    registers[c] = int(registers[a] > b)


def gtrr(registers, a, b, c):
    registers[c] = int(registers[a] > registers[b])


def eqir(registers, a, b, c):
    registers[c] = int(a == registers[b])


def eqri(registers, a, b, c):
    registers[c] = int(registers[a] == b)


def eqrr(registers, a, b, c):
    registers[c] = int(registers[a] == registers[b])


opcode_funcs = dict(
    addr=addr,
    addi=addi,
    mulr=mulr,
    muli=muli,
    banr=banr,
    bani=bani,
    borr=borr,
    bori=bori,
    setr=setr,
    seti=seti,
    gtir=gtir,
    gtri=gtri,
    gtrr=gtrr,
    eqir=eqir,
    eqri=eqri,
    eqrr=eqrr)


def parse_instruction(line):
    opcode, a, b, c = line.split()
    return opcode, int(a), int(b), int(c)


def main():
    ip_line, *program_lines = stdin.read().splitlines()
    ip = int(ip_line.split()[-1])
    program = [parse_instruction(line) for line in program_lines]

    registers = [0, 0, 0, 0, 0, 0]

    while 0 <= registers[ip] < len(program):
        opcode, a, b, c = program[registers[ip]]
        func = opcode_funcs[opcode]
        func(registers, a, b, c)
        registers[ip] += 1

    print(registers[0])


if __name__ == '__main__':
    main()
