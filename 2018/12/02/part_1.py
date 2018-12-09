import itertools
import sys


def main():
    twos = 0
    threes = 0

    for line in sys.stdin:
        id = line.strip()
        groups = itertools.groupby(sorted(list(id)))
        counts = [len(list(v)) for k, v in groups]

        if 2 in counts:
            twos += 1

        if 3 in counts:
            threes += 1

    print(twos * threes)


if __name__ == '__main__':
    main()
