from itertools import chain, groupby
from sys import stdin


def main():
    sequence = [int(c) for c in stdin.read().strip()]

    for _ in range(40):
        sequence = list(chain.from_iterable(
            (len(list(g)), k)
            for k, g in groupby(sequence)))

    print(len(sequence))


if __name__ == '__main__':
    main()
