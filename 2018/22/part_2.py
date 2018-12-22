from heapq import heappop, heappush
from sys import maxsize, stdin


ROCKY = 0
WET = 1
NARROW = 2


NEITHER = 0
TORCH = 1
CLIMBING_GEAR = 2


region_tools = {
    ROCKY: {TORCH, CLIMBING_GEAR},
    WET: {NEITHER, CLIMBING_GEAR},
    NARROW: {NEITHER, TORCH},
}


def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def main():
    depth_line, target_line = stdin.read().splitlines()
    depth = int(depth_line.split(':')[-1])
    target_x, target_y = [int(s) for s in target_line.split(':')[-1].split(',')]

    geological_indices = {}

    def get_geological_index(x, y):
        if (x, y) in geological_indices:
            return geological_indices[x, y]

        if (x, y) in [(0, 0), (target_x, target_y)]:
            index = 0
        elif y == 0:
            index = x * 16807
        elif x == 0:
            index = y * 48271
        else:
            index = get_erosion_level(x - 1, y) * get_erosion_level(x, y - 1)

        geological_indices[x, y] = index
        return index

    def get_erosion_level(x, y):
        return (get_geological_index(x, y) + depth) % 20183

    def get_region_type(x, y):
        return get_erosion_level(x, y) % 3

    def print_map(min_x, min_y, max_x, max_y):
        def get_char(x, y):
            if (x, y) == (0, 0):
                return 'M'

            if (x, y) == (target_x, target_y):
                return 'T'

            type_ = get_region_type(x, y)
            return '.=|'[type_]

        for y in range(min_y, max_y + 1):
            print(''.join(get_char(x, y) for x in range(min_x, max_x + 1)))

    # print_map(0, 0, target_x, target_y)

    open_ = []
    heappush(open_, (target_x + target_y, 0, 0, 0, TORCH))
    closed = {}

    while open_:
        th, t, x, y, tool = heappop(open_)

        if t >= closed.get((x, y, tool), maxsize):
            continue

        closed[x, y, tool] = t

        if (x, y) == (target_x, target_y) and tool == TORCH:
            print(t)
            return

        type_ = get_region_type(x, y)

        for other_tool in region_tools[type_]:
            if other_tool != tool:
                heappush(open_, (th + 7, t + 7, x, y, other_tool))

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if x + dx >= 0 and y + dy >= 0:
                adjacent_type = get_region_type(x + dx, y + dy)

                if tool in region_tools[adjacent_type]:
                    h = manhattan_distance(x + dx, y + dy, target_x, target_y)
                    heappush(open_, (t + 1 + h, t + 1, x + dx, y + dy, tool))


if __name__ == '__main__':
    main()
