from sys import maxsize, stdin


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


def rfind(list_, value):
    for i in range(len(list_) - 1, -1, -1):
        if list_[i] == value:
            return i

    return -1


def main():
    map_ = [line.strip() for line in stdin if line.strip()]

    resource_values = []
    cycle_length = 0
    matches = 0

    for minute in range(0, maxsize):
        resource_value = get_resource_value(map_)

        if (cycle_length and
            resource_value == resource_values[minute - cycle_length]):

            matches += 1
        else:
            old_minute = rfind(resource_values, resource_value)
            cycle_length = 0 if old_minute == -1 else minute - old_minute
            matches = 0

        resource_values.append(resource_value)

        if matches > cycle_length:
            break

        map_ = [
            ''.join(change_acre(map_, x, y) for x, _ in enumerate(row))
            for y, row in enumerate(map_)
        ]

    cycle_start = len(resource_values) - cycle_length
    cycle_offset = (1000000000 - cycle_start) % cycle_length
    print(resource_values[cycle_start + cycle_offset])


if __name__ == '__main__':
    main()
