from collections import Counter
from sys import stdin


def parse_claim(line):
    digit_line = ''.join(char if char.isdigit() else ' ' for char in line)
    id_, x, y, width, height = [int(word) for word in digit_line.split()]
    return id_, (x, y, width, height)


def main():
    claims = dict(parse_claim(line.strip()) for line in stdin)

    fabric = Counter(
        (x2, y2)
        for x, y, width, height in claims.values()
        for y2 in range(y, y + height)
        for x2 in range(x, x + width))

    print(sum(n >= 2 for n in fabric.values()))


if __name__ == '__main__':
    main()
