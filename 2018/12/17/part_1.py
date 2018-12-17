from collections import defaultdict, deque
from sys import stdin


def parse_clay_vein(line):
    for item in line.split(', '):
        key, value = item.split('=')

        if key == 'x':
            min_x = min(int(s) for s in value.split('..'))
            max_x = max(int(s) for s in value.split('..'))
        else:
            min_y = min(int(s) for s in value.split('..'))
            max_y = max(int(s) for s in value.split('..'))

    return min_x, min_y, max_x, max_y


def print_map(map_, min_x, min_y, max_x, max_y):
    for y in range(min_y, max_y + 1):
        print(''.join(map_.get((x, y), ' ') for x in range(min_x, max_x + 1)))


def main():
    def sand_factory():
        return '.'

    map_ = defaultdict(sand_factory)

    for line in stdin:
        min_x, min_y, max_x, max_y = parse_clay_vein(line)

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

        square = map_[x, y]

        above = map_[x, y - 1]
        left = map_[x - 1, y]
        right = map_[x + 1, y]
        below = map_[x, y + 1]

        if square == '.':
            if above in '+|' or left in '->' or right in '-<':
                square = '|'
        elif square == '|':
            if below in '#~':
                square = '-'
        elif square == '-':
            if below in '#~' and left in '#>':
                square = '>'
            elif below in '#~' and right in '#<':
                square = '<'
        elif square == '<':
            if left in '#~>':
                square = '~'
        elif square == '>':
            if right in '#~<':
                square = '~'

        if square != map_[x, y]:
            map_[x, y] = square

            for dx, dy in [(0, -1), (-1, 0), (0, 0), (1, 0), (0, 1)]:
                if y + dy <= max_y:
                    closed.discard((x + dx, y + dy))
                    open_.append((x + dx, y + dy))

    print(sum(
        square in '|~-<>'
        for (_, y), square in map_.items()
        if min_y <= y <= max_y))


if __name__ == '__main__':
    main()
