from sys import stdin


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

    print(sum(
        get_region_type(x, y)
        for y in range(0, target_y + 1)
        for x in range(0, target_x + 1)))


if __name__ == '__main__':
    main()
