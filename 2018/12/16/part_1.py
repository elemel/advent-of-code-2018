from collections import namedtuple
from sys import stdin


Sample = namedtuple('Sample', ['before', 'instruction', 'after'])


def parse_sample(lines):
    before = tuple(int(s) for s in lines[0][9:19].split(','))
    instruction = tuple(int(s) for s in lines[1].split())
    after = tuple(int(s) for s in lines[2][9:19].split(','))
    return Sample(before=before, instruction=instruction, after=after)


def addr(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] + registers[b]


def addi(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] + b


def mulr(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] * registers[b]


def muli(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] * b


def banr(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] & registers[b]


def bani(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] & b


def borr(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] | registers[b]


def bori(instruction, registers):
    _, a, b, c = instruction
    registers[c] = registers[a] | b


def setr(instruction, registers):
    _, a, _, c = instruction
    registers[c] = registers[a]


def seti(instruction, registers):
    _, a, _, c = instruction
    registers[c] = a


def gtir(instruction, registers):
    _, a, b, c = instruction
    registers[c] = int(a > registers[b])


def gtri(instruction, registers):
    _, a, b, c = instruction
    registers[c] = int(registers[a] > b)


def gtrr(instruction, registers):
    _, a, b, c = instruction
    registers[c] = int(registers[a] > registers[b])


def eqir(instruction, registers):
    _, a, b, c = instruction
    registers[c] = int(a == registers[b])


def eqri(instruction, registers):
    _, a, b, c = instruction
    registers[c] = int(registers[a] == b)


def eqrr(instruction, registers):
    _, a, b, c = instruction
    registers[c] = int(registers[a] == registers[b])


opcodes = dict(
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


def behaves_like(sample, opcode):
    registers = list(sample.before)
    opcodes[opcode](sample.instruction, registers)
    return tuple(registers) == sample.after


def main():
    lines = stdin.read().splitlines()
    i = 0
    samples = []

    while i < len(lines) and lines[i].startswith('Before'):
        samples.append(parse_sample(lines[i:i + 3]))
        i += 4

    print(sum(
        sum(behaves_like(sample, opcode) for opcode in opcodes) >= 3
        for sample in samples))


if __name__ == '__main__':
    main()
