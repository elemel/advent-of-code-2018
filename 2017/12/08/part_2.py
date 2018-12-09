from collections import defaultdict
import operator
from sys import stdin


def main():
    mod_ops = dict(inc=1, dec=-1)

    cond_ops = {
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>': operator.gt,
    }

    regs = defaultdict(int)
    max_value = 0

    for line in stdin:
        mod, cond = line.split(' if ')
        mod_reg, mod_op, mod_const = mod.split()
        cond_reg, cond_op, cond_const = cond.split()

        if cond_ops[cond_op](regs[cond_reg], int(cond_const)):
            regs[mod_reg] += mod_ops[mod_op] * int(mod_const)
            max_value = max(max_value, regs[mod_reg])

    print(max_value)


if __name__ == '__main__':
    main()
