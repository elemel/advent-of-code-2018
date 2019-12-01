from collections import Counter
from sys import stdin


def change_acre(map_, x, y):
    acre = map_[y][x]

    min_x = max(0, x - 1)
    min_y = max(0, y - 1)
    max_x = min(x + 1, len(map_[0]) - 1)
    max_y = min(y + 1, len(map_) - 1)

    adjacent = Counter(
        map_[y2][x2]
        for y2 in range(min_y, max_y + 1)
        for x2 in range(min_x, max_x + 1)
        if (x2, y2) != (x, y))

    if acre == '.':
        if adjacent['|'] >= 3:
            acre = '|'
    elif acre == '|':
        if adjacent['#'] >= 3:
            acre = '#'
    elif acre == '#':
        if '#' not in adjacent or '|' not in adjacent:
            acre = '.'

    return acre


def print_map(map_):
    for row in map_:
        print(row)


def main():
    map_ = tuple(line.strip() for line in stdin if line.strip())

    for minute in range(0, 10):
        map_ = tuple(
            ''.join(change_acre(map_, x, y) for x, _ in enumerate(row))
            for y, row in enumerate(map_))

    # print_map(map_)

    resources = Counter(acre for row in map_ for acre in row)
    print(resources['|'] * resources['#'])


if __name__ == '__main__':
    main()
