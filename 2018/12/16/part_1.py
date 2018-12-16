from collections import namedtuple
from sys import stdin


Sample = namedtuple('Sample', ['before', 'instruction', 'after'])


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


def behaves_like(sample, opcode_name):
    registers = list(sample.before)
    _, a, b, c = sample.instruction
    func = opcode_funcs[opcode_name]
    func(registers, a, b, c)
    return tuple(registers) == sample.after


def main():
    lines = stdin.read().splitlines()
    lines.reverse()

    samples = []

    while lines and lines[-1].startswith('Before'):
        before = tuple(int(s) for s in lines.pop()[9:19].split(','))
        instruction = tuple(int(s) for s in lines.pop().split())
        after = tuple(int(s) for s in lines.pop()[9:19].split(','))
        lines.pop()

        sample = Sample(before=before, instruction=instruction, after=after)
        samples.append(sample)

    print(sum(
        sum(behaves_like(sample, name) for name in opcode_funcs) >= 3
        for sample in samples))


if __name__ == '__main__':
    main()
