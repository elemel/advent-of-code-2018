from itertools import cycle
from sys import stdin


def main():
    sequence = cycle(int(line.strip()) for line in stdin)
    current = 0
    seen = set()

    while current not in seen:
        seen.add(current)
        current += next(sequence)

    print(current)


if __name__ == '__main__':
    main()
