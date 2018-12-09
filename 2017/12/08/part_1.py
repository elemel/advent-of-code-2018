from collections import defaultdict
import operator
from sys import stdin


def main():
    signs = dict(inc=1, dec=-1)

    operators = {
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>': operator.gt,
    }

    registers = defaultdict(int)

    for line in stdin:
        reg, inc_dec, amount, _, cond_reg, cond_op, cond_const = line.split()

        if operators[cond_op](registers[cond_reg], int(cond_const)):
            registers[reg] += signs[inc_dec] * int(amount)

    print(max(registers.values()))


if __name__ == '__main__':
    main()
