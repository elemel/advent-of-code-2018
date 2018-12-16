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


def behaves_like(sample, opcode_name):
    registers = list(sample.before)
    opcodes[opcode_name](sample.instruction, registers)
    return tuple(registers) == sample.after


def main():
    lines = stdin.read().splitlines()
    i = 0
    samples = []

    while i < len(lines) and lines[i].startswith('Before'):
        samples.append(parse_sample(lines[i:i + 3]))
        i += 4

    test_program = [
        tuple(int(s) for s in line.split())
        for line in lines[i:] if line.strip()
    ]

    behaves_like_sets = {opcode_name: set() for opcode_name in opcodes}

    for sample in samples:
        for opcode_name in opcodes:
            if behaves_like(sample, opcode_name):
                opcode_number, _, _, _ = sample.instruction
                behaves_like_sets[opcode_name].add(opcode_number)

    opcode_list = 16 * [None]

    while behaves_like_sets:
        for opcode_name, opcode_set in behaves_like_sets.items():
            if len(opcode_set) == 1:
                opcode_number, = behaves_like_sets.pop(opcode_name)
                opcode_list[opcode_number] = opcode_name

                for opcode_set in behaves_like_sets.values():
                    opcode_set.discard(opcode_number)

                break

    registers = [0, 0, 0, 0]

    for instruction in test_program:
        opcode_number = instruction[0]
        opcode_name = opcode_list[opcode_number]
        opcodes[opcode_name](instruction, registers)

    print(registers[0])


if __name__ == '__main__':
    main()
