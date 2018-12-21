from collections import deque
from sys import stdin


def parse_clay_vein(line):
    x_str, y_str = sorted(line.split(', '))
    xs = [int(s) for s in x_str[2:].split('..')]
    ys = [int(s) for s in y_str[2:].split('..')]
    return min(xs), min(ys), max(xs), max(ys)


def print_map(map_, min_x, min_y, max_x, max_y):
    for y in range(min_y, max_y + 1):
        print(''.join(map_.get((x, y), '.') for x in range(min_x, max_x + 1)))


def main():
    clay_veins = [parse_clay_vein(line) for line in stdin]

    map_ = {}

    for min_x, min_y, max_x, max_y in clay_veins:
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                map_[x, y] = '#'

    min_x = min(x for x, _ in map_)
    min_y = min(y for _, y in map_)
    max_x = max(x for x, _ in map_)
    max_y = max(y for _, y in map_)

    map_[500, 0] = '+'

    open_ = deque([(500, 1)])
    closed = set()

    while open_:
        x, y = open_.popleft()

        if (x, y) in closed:
            continue

        closed.add((x, y))

        square = map_.get((x, y), '.')

        above = map_.get((x, y - 1), '.')
        left = map_.get((x - 1, y), '.')
        right = map_.get((x + 1, y), '.')
        below = map_.get((x, y + 1), '.')

        if square == '.':
            if above in '+|' or left in '->' or right in '-<':
                square = '|'

        if square == '|':
            if below in '#~':
                square = '-'

        if square == '-':
            if left in '#>':
                square = '>'
            elif right in '#<':
                square = '<'

        if square == '<':
            if left in '#~>':
                square = '~'
        elif square == '>':
            if right in '#~<':
                square = '~'

        if square != map_.get((x, y), '.'):
            map_[x, y] = square

            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                if y + dy <= max_y:
                    closed.discard((x + dx, y + dy))
                    open_.append((x + dx, y + dy))

    # print_map(map_, min_x - 1, 0, max_x + 1, max_y)

    print(sum(
        square == '~'
        for (_, y), square in map_.items()
        if min_y <= y <= max_y))


if __name__ == '__main__':
    main()
