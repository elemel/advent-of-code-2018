from sys import argv, stdin


def format_addr(a, b, c, symbols):
    return f'addr {symbols[a]} {symbols[b]} {symbols[c]}'


def format_addi(a, b, c, symbols):
    return f'addi {symbols[a]} {b} {symbols[c]}'


def format_mulr(a, b, c, symbols):
    return f'mulr {symbols[a]} {symbols[b]} {symbols[c]}'


def format_muli(a, b, c, symbols):
    return f'muli {symbols[a]} {b} {symbols[c]}'


def format_banr(a, b, c, symbols):
    return f'banr {symbols[a]} {symbols[b]} {symbols[c]}'


def format_bani(a, b, c, symbols):
    return f'bani {symbols[a]} {b} {symbols[c]}'


def format_borr(a, b, c, symbols):
    return f'borr {symbols[a]} {symbols[b]} {symbols[c]}'


def format_bori(a, b, c, symbols):
    return f'bori {symbols[a]} {b} {symbols[c]}'


def format_setr(a, b, c, symbols):
    return f'setr {symbols[a]} _ {symbols[c]}'


def format_seti(a, b, c, symbols):
    return f'seti {a} _ {symbols[c]}'


def format_gtir(a, b, c, symbols):
    return f'gtir {a} {symbols[b]} {symbols[c]}'


def format_gtri(a, b, c, symbols):
    return f'gtri {symbols[a]} {b} {symbols[c]}'


def format_gtrr(a, b, c, symbols):
    return f'gtrr {symbols[a]} {symbols[b]} {symbols[c]}'


def format_eqir(a, b, c, symbols):
    return f'eqir {a} {symbols[b]} {symbols[c]}'


def format_eqri(a, b, c, symbols):
    return f'eqri {symbols[a]} {b} {symbols[c]}'


def format_eqrr(a, b, c, symbols):
    return f'eqrr {symbols[a]} {symbols[b]} {symbols[c]}'


default_format_funcs = dict(
    addr=format_addr,
    addi=format_addi,
    mulr=format_mulr,
    muli=format_muli,
    banr=format_banr,
    bani=format_bani,
    borr=format_borr,
    bori=format_bori,
    setr=format_setr,
    seti=format_seti,
    gtir=format_gtir,
    gtri=format_gtri,
    gtrr=format_gtrr,
    eqir=format_eqir,
    eqri=format_eqri,
    eqrr=format_eqrr)


def c_format_addr(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} += {symbols[b]}'
    elif b == c:
        return f'{symbols[c]} += {symbols[a]}'
    else:
        return f'{symbols[c]} = {symbols[a]} + {symbols[b]}'


def c_format_addi(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} += {b}'
    else:
        return f'{symbols[c]} = {symbols[a]} + {b}'


def c_format_mulr(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} *= {symbols[b]}'
    elif b == c:
        return f'{symbols[c]} *= {symbols[a]}'
    else:
        return f'{symbols[c]} = {symbols[a]} * {symbols[b]}'


def c_format_muli(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} *= {b}'
    else:
        return f'{symbols[c]} = {symbols[a]} * {b}'


def c_format_banr(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} &= {symbols[b]}'
    elif b == c:
        return f'{symbols[c]} &= {symbols[a]}'
    else:
        return f'{symbols[c]} = {symbols[a]} & {symbols[b]}'


def c_format_bani(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} &= {b}'
    else:
        return f'{symbols[c]} = {symbols[a]} & {b}'


def c_format_borr(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} |= {symbols[b]}'
    elif b == c:
        return f'{symbols[c]} |= {symbols[a]}'
    else:
        return f'{symbols[c]} = {symbols[a]} | {symbols[b]}'


def c_format_bori(a, b, c, symbols):
    if a == c:
        return f'{symbols[c]} |= {b}'
    else:
        return f'{symbols[c]} = {symbols[a]} | {b}'


def c_format_setr(a, b, c, symbols):
    return f'{symbols[c]} = {symbols[a]}'


def c_format_seti(a, b, c, symbols):
    return f'{symbols[c]} = {a}'


def c_format_gtir(a, b, c, symbols):
    return f'{symbols[c]} = {a} > {symbols[b]}'


def c_format_gtri(a, b, c, symbols):
    return f'{symbols[c]} = {symbols[a]} > {b}'


def c_format_gtrr(a, b, c, symbols):
    return f'{symbols[c]} = {symbols[a]} > {symbols[b]}'


def c_format_eqir(a, b, c, symbols):
    return f'{symbols[c]} = {a} == {symbols[b]}'


def c_format_eqri(a, b, c, symbols):
    return f'{symbols[c]} = {symbols[a]} == {b}'


def c_format_eqrr(a, b, c, symbols):
    return f'{symbols[c]} = {symbols[a]} == {symbols[b]}'


c_format_funcs = dict(
    addr=c_format_addr,
    addi=c_format_addi,
    mulr=c_format_mulr,
    muli=c_format_muli,
    banr=c_format_banr,
    bani=c_format_bani,
    borr=c_format_borr,
    bori=c_format_bori,
    setr=c_format_setr,
    seti=c_format_seti,
    gtir=c_format_gtir,
    gtri=c_format_gtri,
    gtrr=c_format_gtrr,
    eqir=c_format_eqir,
    eqri=c_format_eqri,
    eqrr=c_format_eqrr)


def parse_instruction(line):
    opcode, a, b, c = line.split()
    return opcode, int(a), int(b), int(c)


def main():
    ip_line, *program_lines = stdin.read().splitlines()
    ip = int(ip_line.split()[-1])
    program = [parse_instruction(line) for line in program_lines]
    symbols = list('abcdefghijklmnopqrstuvwxyz')
    symbols[ip] = 'ip'
    line_number_width = len(str(len(program) - 1))
    format_funcs = c_format_funcs if '--format=c' in argv else default_format_funcs

    for i, (opcode, a, b, c) in enumerate(program):
        instruction_str = format_funcs[opcode](a, b, c, symbols)
        line = f'{i:0{line_number_width}d}  {instruction_str}'
        print(line)


if __name__ == '__main__':
    main()
