from collections import defaultdict
from itertools import chain
from sys import stdin


def parse_claim(line):
    digit_line = ''.join(c if c.isdigit() else ' ' for c in line)
    id_, x, y, width, height = [int(s) for s in digit_line.split()]
    return id_, (x, y, width, height)


def main():
    claims = dict(parse_claim(line.strip()) for line in stdin)
    fabric = defaultdict(list)

    for id_, (x, y, width, height) in claims.items():
        for y2 in range(y, y + height):
            for x2 in range(x, x + width):
                fabric[x2, y2].append(id_)

    overlapping_ids = set(chain.from_iterable(
        ids
        for ids in fabric.values()
        if len(ids) >= 2))

    [intact_id] = set(claims) - overlapping_ids
    print(intact_id)


if __name__ == '__main__':
    main()
