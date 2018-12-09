from itertools import combinations, starmap
from sys import stdin


def match(a, b):
    return a if a == b else ''


def solve(ids):
    for a, b in combinations(ids, 2):
        if len(a) == len(b):
            common = ''.join(starmap(match, zip(a, b)))

            if len(common) == len(a) - 1:
                return common


def main():
    ids = [line.strip() for line in stdin]
    print(solve(ids))


if __name__ == '__main__':
    main()
