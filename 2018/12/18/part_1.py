from sys import stdin


def print_map(map_):
    for row in map_:
        print(row)


def change_acre(map_, x, y):
    width = len(map_[0])
    height = len(map_)

    adjacent = ''.join(sorted(
        map_[y2][x2]
        for y2 in range(max(0, y - 1), min(y + 2, height))
        for x2 in range(max(0, x - 1), min(x + 2, width))
        if (x2, y2) != (x, y)))

    acre = map_[y][x]

    if acre == '.':
        if '|||' in adjacent:
            acre = '|'
    elif acre == '|':
        if '###' in adjacent:
            acre = '#'
    elif acre == '#':
        if '#' not in adjacent or '|' not in adjacent:
            acre = '.'

    return acre


def get_resource_value(map_):
    wooded_acres = sum(acre == '|' for row in map_ for acre in row)
    lumberyards = sum(acre == '#' for row in map_ for acre in row)
    return wooded_acres * lumberyards


def main():
    map_ = [line.strip() for line in stdin if line.strip()]

    for minute in range(0, 10):
        map_ = [
            ''.join(change_acre(map_, x, y) for x, _ in enumerate(row))
            for y, row in enumerate(map_)
        ]

    # print_map(map_)

    print(get_resource_value(map_))


if __name__ == '__main__':
    main()
